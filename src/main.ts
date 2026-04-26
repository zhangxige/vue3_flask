
import { createApp } from 'vue'
// import App from './layout/AppLayout.vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import { createPinia } from 'pinia'
import Viewer from 'v-viewer'
import 'viewerjs/dist/viewer.css'
import router from './router'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const pinia = createPinia()
const app = createApp(App)
app.use(ElementPlus)  // 此时 ElementPlus 的使用在根组件的挂载之前，是正确的；
app.use(Viewer)
app.use(pinia)
app.use(router)
app.mount('#app')

// 注册 Element Plus 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}