<template>
  <div :class="['learn-test', theme]">
    <header class="page-header">
      <div>
        <p class="eyebrow">Vue3 Demo</p>
        <h1>学习与测试</h1>
        <p class="subtitle">一个简洁的页面，用来展示响应式、计算属性、条件渲染和表单交互。</p>
      </div>
      <div class="header-actions">
        <button class="secondary theme-toggle" @click="toggleTheme">
          切换到 {{ theme === 'light' ? '深色' : '浅色' }} 模式
        </button>
        <span class="status-chip">测试页面</span>
      </div>
    </header>

    <main class="dashboard-grid">
      <section class="panel">
        <div class="panel-title">
          <h2>响应式计数器</h2>
          <span class="badge">Reactive</span>
        </div>
        <p class="panel-text">
          当前计数：<strong>{{ count }}</strong>
        </p>
        <div class="button-row">
          <button class="primary" @click="increment">+1</button>
          <button class="secondary" @click="clear_count">清零</button>
        </div>
      </section>

      <section class="panel">
        <div class="panel-title">
          <h2>计算属性</h2>
          <span class="badge">Books</span>
        </div>
        <p class="panel-text">
          书籍状态：<strong>{{ publishedBooksMessage }}</strong>
        </p>
        <button class="primary" @click="change_book_status">切换书籍状态</button>
      </section>

      <section class="panel">
        <div class="panel-title">
          <h2>动态样式</h2>
          <span class="badge">Style</span>
        </div>
        <p class="panel-text">当前演示按钮会在蓝色和红色之间切换。</p>
        <button class="style-demo" @click="change_style" :style="styleObject">改变样式</button>
      </section>

      <section class="panel">
        <div class="panel-title">
          <h2>条件渲染</h2>
          <span class="badge">v-if</span>
        </div>
        <div class="switch-row">
          <button class="secondary" @click="awesome = !awesome">切换展示</button>
          <span class="status-text">{{ awesome ? 'Vue 非常棒！' : 'Oh no 😢' }}</span>
        </div>
      </section>

      <section class="panel wide-panel">
        <div class="panel-title">
          <h2>对象列表</h2>
          <span class="badge">Reactive Object</span>
        </div>
        <ul class="info-list">
          <li v-for="(value, key, index) in myObject" :key="key">
            <strong>{{ index + 1 }}.</strong> {{ key }}: {{ value }}
          </li>
        </ul>
        <button class="primary" @click="change_myObject">切换对象内容</button>
      </section>

      <section class="panel">
        <div class="panel-title">
          <h2>实时输入</h2>
          <span class="badge">v-model</span>
        </div>
        <p class="panel-text">
          当前内容：<strong>{{ formmessage }}</strong>
        </p>
        <input v-model="formmessage" placeholder="在这里输入内容..." />
      </section>

      <section class="panel">
        <div class="panel-title">
          <h2>图片组件测试</h2>
          <span class="badge">Image</span>
        </div>
        <div class="image-preview" v-if="imageVisible">
          <img
            :src="imageSrc"
            alt="测试图片"
            @load="imageLoaded = true"
            @error="imageLoaded = false"
          />
          <p class="panel-text">{{ imageLoaded ? '图片加载成功' : '正在加载图片...' }}</p>
        </div>
        <p v-else class="panel-text">图片已隐藏</p>
        <div class="button-row">
          <button class="primary" @click="toggleImageVisible">
            {{ imageVisible ? '隐藏图片' : '显示图片' }}
          </button>
          <button class="secondary" @click="switchImage">切换图片</button>
        </div>
      </section>

      <section class="panel wide-panel">
        <div class="panel-title">
          <h2>提交任务</h2>
          <span class="badge">API</span>
        </div>
        <div class="form-grid">
          <input v-model="name" placeholder="名字" />
          <input v-model="time" placeholder="持续时间（分钟）" />
          <input v-model="content" placeholder="任务内容" />
        </div>
        <button class="primary" @click="submitData">提交任务</button>
      </section>

      <section class="panel wide-panel panel-tasks">
        <div class="panel-title">
          <h2>任务列表</h2>
          <span class="badge">Fetch</span>
        </div>
        <button class="secondary" @click="fetchTasks">查询任务</button>
        <ul v-if="tasks.length" class="task-list">
          <li v-for="task in tasks" :key="task.id">
            <strong>#{{ task.name }}</strong>
            <span>{{ task.params.duration }} 秒</span>
            <span>状态：{{ task.status }}</span>
            <span>创建时间: {{ task.created_at }}</span>
            <span v-if="task.completed_at">完成时间: {{ task.completed_at }}</span>
          </li>
        </ul>
        <p v-else class="empty-state">暂无任务数据，点击按钮加载</p>
      </section>
    </main>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive, computed } from 'vue'
import axios from 'axios'

interface Task {
  id: string
  name: string
  duration: number
  status: string
  params: {
    duration: string
    param2: number
  }
  created_at: string | null
  completed_at: string | null
}

const count = ref(0)
const increment = () => {
  count.value++
}
const clear_count = () => {
  count.value = 0
}

const author = reactive({
  name: 'John Doe',
  books: ['Vue 2 - Advanced Guide', 'Vue 3 - Basic Guide', 'Vue 4 - The Mystery'],
})

const publishedBooksMessage = computed(() => (author.books.length === 3 ? 'Yes' : 'No'))
const change_book_status = () => {
  if (author.books.length === 3) {
    author.books.push('Vue 4 - The Mystery')
  } else {
    author.books.pop()
  }
}

const styleObject = reactive({
  color: 'red',
  fontSize: '30px',
})
const style_mark = ref(false)
const change_style = () => {
  style_mark.value = !style_mark.value
  styleObject.color = style_mark.value ? 'red' : 'blue'
  styleObject.fontSize = style_mark.value ? '30px' : '20px'
}
const awesome = ref(true)

const myObject = reactive({
  title: 'How to do lists in Vue',
  author: 'Jane Doe',
  publishedAt: '2016-04-10',
})
const change_myObject = () => {
  if (myObject.title === 'How to do lists in Vue') {
    myObject.title = 'teaching in Vue 3'
    myObject.author = 'Jane Jone'
    myObject.publishedAt = '2025-05-10'
  } else {
    myObject.title = 'How to do lists in Vue'
    myObject.author = 'John Doe'
    myObject.publishedAt = '2020-01-01'
  }
}
const formmessage = ref('Hello Vue 3!')

const name = ref('example name')
const time = ref('10')
const content = ref('example content')

const submitData = async () => {
  try {
    const response = await axios.post('http://localhost:8000/posttask', {
      name: name.value,
      duration: parseInt(time.value, 10),
      param1: 'content.value',
      param2: 3,
    })
    console.log('提交成功:', response.data)
  } catch (error) {
    console.error('提交失败:', error)
  }
}

const tasks = ref<Task[]>([])
const fetchTasks = async () => {
  try {
    const response = await axios.get('http://localhost:8000/posttask')
    tasks.value = response.data.tasks
    console.log('获取任务成功:', tasks.value)
  } catch (error) {
    console.error('获取任务失败:', error)
  }
}

const theme = ref<'light' | 'dark'>('light')
const toggleTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}

const imageVisible = ref(true)
const imageLoaded = ref(false)
const imageIndex = ref(0)
const imageSources = [
  'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 250%22%3E%3Crect width=%22400%22 height=%22250%22 fill=%22%236d28d9%22/%3E%3Ctext x=%22200%22 y=%22130%22 font-family=%22sans-serif%22 font-size=%2232%22 fill=%22%23ffffff%22 text-anchor=%22middle%22%3EVue 图片测试%3C/text%3E%3C/svg%3E',
  'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 250%22%3E%3Cdefs%3E%3ClinearGradient id=%22g%22 x1=%220%25%22 y1=%220%25%22 x2=%22100%25%22 y2=%22100%25%22%3E%3Cstop offset=%220%25%22 stop-color=%22%23813be0%22/%3E%3Cstop offset=%22100%25%22 stop-color=%22%2358b5ff%22/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width=%22400%22 height=%22250%22 fill=%22url(%23g)%22/%3E%3Ctext x=%22200%22 y=%22130%22 font-family=%22sans-serif%22 font-size=%2232%22 fill=%22%23ffffff%22 text-anchor=%22middle%22%3E图片切换%3C/text%3E%3C/svg%3E',
]
const imageSrc = ref(imageSources[imageIndex.value])
const switchImage = () => {
  imageIndex.value = (imageIndex.value + 1) % imageSources.length
  imageSrc.value = imageSources[imageIndex.value]
  imageLoaded.value = false
}
const toggleImageVisible = () => {
  imageVisible.value = !imageVisible.value
}
</script>

<style scoped>
.learn-test {
  min-height: 100vh;
  padding: 24px;
  background:
    radial-gradient(circle at top left, rgba(121, 97, 255, 0.18), transparent 35%),
    linear-gradient(180deg, #f5f7ff 0%, #eef2ff 100%);
  color: #1f2a44;
}

.learn-test.dark {
  background:
    radial-gradient(circle at top left, rgba(56, 189, 248, 0.15), transparent 35%),
    linear-gradient(180deg, #0f172a 0%, #111827 100%);
  color: #e2e8f0;
}

.learn-test.light {
  --panel: #ffffff;
  --panel-border: rgba(148, 163, 184, 0.16);
  --text: #1f2a44;
  --subtitle: #475569;
  --badge-bg: rgba(99, 102, 241, 0.1);
  --badge-text: #4f46e5;
  --button-secondary: #eef2ff;
  --button-secondary-text: #3730a3;
  --input-bg: #f8fafc;
  --input-border: rgba(148, 163, 184, 0.24);
  --panel-shadow: 0 18px 50px rgba(15, 23, 42, 0.06);
  --status-bg: rgba(79, 70, 229, 0.12);
  --status-text: #4338ca;
  --status-alt: #1e3a8a;
  --panel-alt: #fafbff;
}

.learn-test.dark {
  --panel: #111827;
  --panel-border: rgba(148, 163, 184, 0.24);
  --text: #e2e8f0;
  --subtitle: #94a3b8;
  --badge-bg: rgba(59, 130, 246, 0.15);
  --badge-text: #bfdbfe;
  --button-secondary: #1e293b;
  --button-secondary-text: #cbd5e1;
  --input-bg: #0f172a;
  --input-border: rgba(148, 163, 184, 0.28);
  --panel-shadow: 0 18px 50px rgba(15, 23, 42, 0.48);
  --status-bg: rgba(59, 130, 246, 0.18);
  --status-text: #bfdbfe;
  --status-alt: #93c5fd;
  --panel-alt: #151f2f;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
  gap: 16px;
}

.eyebrow {
  margin: 0 0 8px;
  color: #7c89d9;
  font-size: 0.88rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.page-header h1 {
  margin: 0;
  font-size: clamp(2rem, 2.4vw, 2.6rem);
  line-height: 1.05;
}

.subtitle {
  margin: 12px 0 0;
  max-width: 600px;
  color: #4a5568;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.theme-toggle {
  min-width: 180px;
}

.status-chip {
  display: inline-flex;
  align-items: center;
  padding: 10px 16px;
  border-radius: 999px;
  background: var(--status-bg);
  color: var(--status-text);
  font-weight: 600;
  letter-spacing: 0.02em;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
}

.panel {
  background: var(--panel);
  border: 1px solid var(--panel-border);
  border-radius: 24px;
  padding: 22px;
  box-shadow: var(--panel-shadow);
}

.wide-panel {
  grid-column: span 2;
}

.panel-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.panel-title h2 {
  margin: 0;
  font-size: 1.1rem;
}

.badge {
  display: inline-flex;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 700;
  background: var(--badge-bg);
  color: var(--badge-text);
}

.panel-text {
  margin: 0 0 16px;
  color: var(--subtitle);
}

.button-row,
.switch-row,
.form-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

button,
input {
  border: none;
  outline: none;
  font: inherit;
}

button {
  cursor: pointer;
  border-radius: 14px;
  padding: 12px 18px;
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease,
    background-color 0.2s ease;
}

button:hover {
  transform: translateY(-1px);
}

button.primary {
  background: linear-gradient(135deg, #6d28d9, #2563eb);
  color: #fff;
  box-shadow: 0 14px 30px rgba(37, 99, 235, 0.18);
}

button.secondary {
  background: var(--button-secondary);
  color: var(--button-secondary-text);
}

button.style-demo {
  min-width: 180px;
  background: rgba(79, 70, 229, 0.08);
  color: inherit;
}

input {
  flex: 1 1 150px;
  min-width: 160px;
  padding: 12px 14px;
  border: 1px solid var(--input-border);
  border-radius: 14px;
  background: var(--input-bg);
  color: var(--text);
}

.info-list,
.task-list {
  list-style: none;
  padding: 0;
  margin: 0 0 16px;
}

.info-list li,
.task-list li {
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid var(--panel-border);
  margin-bottom: 10px;
  color: var(--text);
  display: grid;
  grid-template-columns: 1fr;
  gap: 6px;
  background: var(--panel-alt);
}

.task-list li {
  grid-template-columns: auto 1fr auto;
  align-items: center;
}

.task-list li span {
  display: inline-block;
  color: var(--subtitle);
}

.empty-state {
  margin: 16px 0 0;
  color: #64748b;
}

.status-text {
  display: inline-flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 999px;
  background: var(--button-secondary);
  color: var(--status-alt);
  font-weight: 600;
}

.image-preview {
  display: grid;
  gap: 12px;
  margin-bottom: 14px;
}

.image-preview img {
  width: 100%;
  max-width: 100%;
  height: auto;
  border-radius: 18px;
  border: 1px solid var(--panel-border);
  background: var(--panel-alt);
}

@media (max-width: 980px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }

  .wide-panel {
    grid-column: span 1;
  }
}

@media (max-width: 640px) {
  .learn-test {
    padding: 16px;
  }

  .page-header {
    flex-direction: column;
    align-items: stretch;
  }

  .button-row,
  .switch-row,
  .form-grid {
    flex-direction: column;
  }
}
</style>
