# FastAPI Backend Service

> 基于 FastAPI 的后端服务，提供任务调度、深度学习模型推理（人脸分割）及工具实验能力。

---

## 技术栈

| 技术 | 说明 |
|------|------|
| **Python >=3.10** | 运行环境 |
| **FastAPI** | 高性能异步 Web 框架 |
| **uv** | Python 包管理器 |
| **PyTorch + TorchVision** | 深度学习框架 |
| **HuggingFace Hub** | 模型权重下载 |
| **OpenCV** | 图像处理 |
| **Loguru** | 日志记录 |
| **TQDM** | 进度条 |
| **Ruff** | 代码格式化与检查 |
| **Pydantic** | 数据验证 |

---

## 目录结构

```
fastapi_server/
├── main.py                    # FastAPI 应用入口（含任务调度系统）
├── pyproject.toml              # 项目配置与依赖
├── uv.lock                     # 依赖锁定文件
├── .python-version             # Python 版本配置
├── README.md                   # 本文件
└── weights/                    # 模型权重文件
    └── convnext_celeba_512/    # ConvNeXt 人脸分割模型
```

---

## 快速开始

### 环境要求

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/)（推荐）或 pip

### 安装与运行

```bash
cd fastapi_server

# 安装依赖
uv sync

# 启动 FastAPI 开发服务器
uv run fastapi dev

# 或使用传统方式
pip install .
fastapi dev
```

### 运行测试

```bash
python -m unittest test_main.py
```

---

## 核心组件

### 任务调度系统（`main.py`）

基于 FastAPI 的线程安全、可扩展的任务调度系统：

| 类 | 说明 |
|------|------|
| `BaseTask` | 抽象基类，定义任务接口 |
| `Task` | 具体任务实现 |
| `Worker` | 工作线程，执行任务 |
| `TaskScheduler` | 任务调度器，管理任务生命周期 |

### 深度学习模型（`test_torch.py`）

人脸分割模型，支持多种骨干网络：

- ConvNeXt
- Swin Transformer
- ResNet
- 自定义网络层

---

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| `POST` | `/tasks` | 创建新任务 |
| `GET` | `/tasks` | 获取所有任务状态 |
| `GET` | `/tasks/{task_id}` | 获取指定任务详情 |
| `DELETE` | `/tasks/{task_id}` | 删除指定任务 |

---

## 开发指南

### 代码规范

```bash
# 格式化代码
ruff format .

# 代码检查
ruff check .
```

### 创建新任务

```python
class MyTask(BaseTask):
    def run(self, *args, **kwargs):
        # 任务逻辑
        pass

scheduler.add_task(name="my_task", method=MyTask(), ...)
```

### 运行模型推理

```bash
python test_torch.py
```

### 下载模型权重

```bash
python test_download_huggingface
```

---

## 项目约定

- **线程安全**: 使用 `ThreadSafeDefaultDict` 管理并发状态
- **任务系统**: 继承 `BaseTask` 实现新任务类型，通过 `TaskScheduler` 注册
- **模型权重**: 下载至 `weights/` 目录，按路径加载
- **日志**: 统一使用 `loguru` 记录日志
- **忽略文件**: `__pycache__/`, `*.py[oc]`, `build/`, `dist/`, `.venv`, `*.egg-info`

---

## 相关文档

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [uv + FastAPI 集成指南](https://uv.doczh.com/guides/integration/fastapi/)
- [PyTorch 文档](https://pytorch.org/docs/)
- [HuggingFace Hub](https://huggingface.co/docs/hub/)

---

## 补充说明

- 项目无顶层包目录，所有脚本位于项目根目录
- 如需自定义 PyTorch 版本，可在 `pyproject.toml` 中配置索引源
- 前端项目详见根目录 [`README.md`](../README.md)
