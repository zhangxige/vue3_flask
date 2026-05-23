# -*- coding: utf-8 -*-
import copy
import datetime
import threading
import time
import uuid
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from pydantic import BaseModel, Field


class BaseTask(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass


class ExampleTask(BaseTask):
    def run(self, *args, **kwargs):
        duration = kwargs.get("duration", 5)
        logger.info(f"Executing ExampleTask for {duration} seconds...")
        time.sleep(duration)
        logger.info("ExampleTask completed.")


_tasks: dict[str, dict] = {}
_lock = threading.Lock()


def _now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _insert_task(task_id: str, name: str, task_type: str, params: dict) -> None:
    with _lock:
        if task_id in _tasks:
            raise ValueError(f"Task id '{task_id}' already exists")
        for t in _tasks.values():
            if t["name"] == name:
                raise ValueError(f"Task name '{name}' already exists")
        _tasks[task_id] = {
            "id": task_id,
            "name": name,
            "task_type": task_type,
            "status": "pending",
            "params": params,
            "result": None,
            "error": None,
            "created_at": _now(),
            "started_at": None,
            "completed_at": None,
            "updated_at": _now(),
        }


def _claim_task():
    with _lock:
        pending = [t for t in _tasks.values() if t["status"] == "pending"]
        if not pending:
            return None
        pending.sort(key=lambda t: t["created_at"])
        task = pending[0]
        task["status"] = "running"
        task["started_at"] = _now()
        task["updated_at"] = _now()
        return copy.deepcopy(task)


def _complete_task(task_id: str, result: dict | None = None) -> None:
    with _lock:
        task = _tasks.get(task_id)
        if task:
            task["status"] = "completed"
            task["result"] = result
            task["completed_at"] = _now()
            task["updated_at"] = _now()


def _fail_task(task_id: str, error: str) -> None:
    with _lock:
        task = _tasks.get(task_id)
        if task:
            task["status"] = "failed"
            task["error"] = error
            task["completed_at"] = _now()
            task["updated_at"] = _now()


def _get_task_by_name(name: str):
    with _lock:
        for t in _tasks.values():
            if t["name"] == name:
                return copy.deepcopy(t)
        return None


def _list_tasks(status: str | None = None):
    with _lock:
        tasks = list(_tasks.values())
        if status:
            tasks = [t for t in tasks if t["status"] == status]
        tasks.sort(key=lambda t: t["created_at"], reverse=True)
        return copy.deepcopy(tasks)


def _delete_task(task_id: str) -> bool:
    with _lock:
        if task_id in _tasks:
            del _tasks[task_id]
            return True
        return False


def _delete_task_by_name(name: str) -> bool:
    with _lock:
        for t in _tasks.values():
            if t["name"] == name:
                del _tasks[t["id"]]
                return True
        return False


class DbTaskScheduler:
    def __init__(self, num_workers: int = 2, poll_interval: float = 1.0):
        self.num_workers = num_workers
        self.poll_interval = poll_interval
        self._running = False
        self._workers: list[Worker] = []
        self._task_methods: dict[str, BaseTask] = {}

    def register_task_type(self, name: str, method: BaseTask):
        self._task_methods[name] = method

    def start(self):
        self._running = True
        for i in range(self.num_workers):
            worker = Worker(i + 1, self)
            worker.start()
            self._workers.append(worker)
        logger.info(f"Scheduler started with {self.num_workers} workers")

    def stop(self):
        self._running = False
        logger.info("Scheduler stopped")


class Worker(threading.Thread):
    def __init__(self, worker_id: int, scheduler: DbTaskScheduler):
        super().__init__(daemon=True)
        self.worker_id = worker_id
        self.scheduler = scheduler

    def run(self):
        while self.scheduler._running:
            task_data = _claim_task()
            if task_data:
                logger.info(
                    f"Worker {self.worker_id} claimed task: {task_data['name']}"
                )
                method = self.scheduler._task_methods.get(task_data["task_type"])
                if method:
                    try:
                        method.run(**task_data["params"])
                        _complete_task(task_data["id"], {"status": "success"})
                        logger.info(
                            f"Worker {self.worker_id} completed task: {task_data['name']}"
                        )
                    except Exception as e:
                        _fail_task(task_data["id"], str(e))
                        logger.error(
                            f"Worker {self.worker_id} task {task_data['name']} failed: {e}"
                        )
                else:
                    _fail_task(
                        task_data["id"], f"Unknown task type: {task_data['task_type']}"
                    )
            else:
                time.sleep(self.scheduler.poll_interval)


class TaskCreate(BaseModel):
    name: str | None = None
    task_type: str = "example"
    duration: int = Field(default=5, ge=0)
    param1: str = "abc"
    param2: int = 3


class TaskSchedulerAPI:
    def __init__(self):
        self.scheduler = DbTaskScheduler(num_workers=2)
        self.default_task = ExampleTask()

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            self.scheduler.register_task_type("example", self.default_task)
            self.scheduler.start()
            yield
            self.scheduler.stop()

        self.app = FastAPI(title="UV Task Scheduler", lifespan=lifespan)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:5173"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.add_api_route("/posttask", self.create_task, methods=["POST"])
        self.app.add_api_route("/posttask", self.list_tasks, methods=["GET"])
        self.app.add_api_route("/tasks/{task_name}", self.get_task, methods=["GET"])
        self.app.add_api_route(
            "/tasks/{task_name}", self.delete_task_handler, methods=["DELETE"]
        )

    def create_task(self, task: TaskCreate) -> dict:
        task_id = uuid.uuid4().hex
        task_name = task.name or f"task_{uuid.uuid4().hex[:8]}"
        params = {
            "duration": task.duration,
            "param1": task.param1,
            "param2": task.param2,
        }
        try:
            _insert_task(task_id, task_name, task.task_type, params)
        except ValueError as e:
            logger.error(f"Error creating task: {e}")
            raise HTTPException(status_code=400, detail=str(e))
        logger.info(f"Task '{task_name}' created (id={task_id})")
        return {"message": "task created", "task_id": task_id, "task_name": task_name}

    def list_tasks(self, status: str | None = None):
        tasks = _list_tasks(status)
        return {"tasks": tasks}

    def get_task(self, task_name: str):
        task = _get_task_by_name(task_name)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def delete_task_handler(self, task_name: str):
        if not _delete_task_by_name(task_name):
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": f"Task '{task_name}' deleted"}


def main_test():
    scheduler = DbTaskScheduler(num_workers=2)
    scheduler.register_task_type("example", ExampleTask())
    scheduler.start()

    _insert_task(
        uuid.uuid4().hex,
        "task_name1",
        "example",
        {"duration": 7, "param1": "abc", "param2": 3},
    )
    _insert_task(
        uuid.uuid4().hex,
        "task_name2",
        "example",
        {"duration": 4, "param1": "abc", "param2": 3},
    )
    _insert_task(
        uuid.uuid4().hex,
        "task_name3",
        "example",
        {"duration": 10, "param1": "abc", "param2": 3},
    )
    _insert_task(
        uuid.uuid4().hex,
        "task_name4",
        "example",
        {"duration": 9, "param1": "abc", "param2": 3},
    )

    logger.warning("Tasks inserted. Workers will pick them up...")
    time.sleep(20)
    all_tasks = _list_tasks()
    logger.warning("Final task statuses:")
    for t in all_tasks:
        logger.info(f"  [{t['status']}] {t['name']} ({t['created_at']})")


if __name__ == "__main__":
    main_test()
else:
    api = TaskSchedulerAPI()
    app = api.app
