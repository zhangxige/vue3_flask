# Vue3 + FastAPI Full-Stack Application

> Vue 3 前端 + FastAPI 后端全栈项目，支持任务调度与深度学习模型推理。

---

## 技术栈

### 前端

| 技术 | 说明 |
|------|------|
| **Vue 3** | 渐进式 JavaScript 框架 |
| **TypeScript** | 类型安全的 JavaScript 超集 |
| **Vite** | 下一代前端构建工具 |
| **Pinia** | 状态管理 |
| **Vue Router** | 路由管理 |
| **Element Plus** | 桌面端 UI 组件库 |
| **Axios** | HTTP 请求库 |
| **ESLint + Prettier** | 代码规范与格式化 |

### 后端

| 技术 | 说明 |
|------|------|
| **FastAPI** | 高性能 Python Web 框架 |
| **uv** | Python 包管理器 |
| **Loguru** | 日志记录 |
| **OpenCV** | 图像处理 |
| **PyTorch** | 深度学习框架 |
| **HuggingFace Hub** | 模型权重下载 |

---

## 目录结构

```
vue3_flask/
├── src/                   # 前端源码
│   ├── api/               # API 接口
│   ├── images/            # 静态资源
│   ├── layout/            # 布局组件
│   ├── router/            # 路由配置
│   ├── stores/            # Pinia 状态管理
│   ├── App.vue            # 根组件
│   └── main.ts            # 入口文件
├── fastapi_server/        # 后端服务
│   ├── main.py            # FastAPI 应用入口
│   ├── pyproject.toml     # Python 依赖配置
│   └── uv.lock            # 依赖锁定文件
├── public/                # 公共资源
├── index.html             # HTML 入口
├── package.json           # 前端依赖配置
├── vite.config.ts         # Vite 配置
├── tsconfig.json          # TypeScript 配置
└── eslint.config.ts       # ESLint 配置
```

---

## 快速开始

### 前端

```bash
# 安装依赖
npm install

# 启动开发服务器（热重载）
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

### 代码检查与格式化

```bash
# ESLint 代码检查（自动修复）
npm run lint

# Prettier 代码格式化
npm run format

# TypeScript 类型检查
npm run type-check
```

### 后端

详见 [`fastapi_server/README.md`](fastapi_server/README.md)。

```bash
cd fastapi_server

# 安装依赖（使用 uv）
uv sync

# 启动 FastAPI 开发服务器
uv run fastapi dev
```

---

## 开发命令速查

| 命令 | 说明 |
|------|------|
| `npm run dev` | 启动前端开发服务器 |
| `npm run build` | 构建生产版本（含类型检查） |
| `npm run lint` | ESLint 代码检查 |
| `npm run format` | Prettier 格式化 |
| `npm run type-check` | TypeScript 类型检查 |
| `uv run fastapi dev` | 启动后端开发服务器 |

---

## 推荐 IDE 配置

- [VSCode](https://code.visualstudio.com/)
- [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)（Vue 3 官方插件，请禁用 Vetur）
- [ESLint 插件](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Prettier 插件](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

---

## 相关文档

- [Vite 配置参考](https://vite.dev/config/)
- [Vue 3 官方文档](https://vuejs.org/)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Element Plus 文档](https://element-plus.org/)
- [Pinia 文档](https://pinia.vuejs.org/)
