// src\router\index.ts
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'


const routes:RouteRecordRaw[] = [
  {
    path: '/Color',
    name: 'Color',
    component: () => import('@/layout/Color.vue')
  },
  {
    path: '/Image',
    name: 'Image',
    component: () => import('@/layout/Image.vue')
  },
  {
    path: '/Brightness',
    name: 'Brightness',
    component: () => import('@/layout/Brightness.vue')
  },
  {
    path: '/Clarity',
    name: 'Clarity',
    component: () => import('@/layout/Clarity.vue')
  },
  {
    path: '/Noise',
    name: 'Noise',
    component: () => import('@/layout/Noise.vue')
  },
  {
    path: '/Contrast',
    name: 'Contrast',
    component: () => import('@/layout/Contrast.vue')
  },
  {
    path: '/Exposure',
    name: 'Exposure',
    component: () => import('@/layout/Exposure.vue')
  },
  {
    path: '/Saturation',
    name: 'Saturation',
    component: () => import('@/layout/Saturation.vue')
  },
  {
    path: '/Sharpness',
    name: 'Sharpness',
    component: () => import('@/layout/Sharpness.vue')
  },
  {
    path: '/WhiteBalance',
    name: 'WhiteBalance',
    component: () => import('@/layout/WhiteBalance.vue')
  },
  {
    path: '/Hue',
    name: 'Hue',
    component: () => import('@/layout/Hue.vue')
  },
  {
    path: '/Interactive',
    name: 'Interactive',
    component: () => import('@/layout/Interactive.vue')
  },
  {
    path: '/Learn_Test',
    name: 'Learn_Test',
    component: () => import('@/layout/Learn_Test.vue')
  },
]

const router = createRouter({
  // history: createWebHashHistory(), // hash 路由模式
  history: createWebHistory(), // history 路由模式
  routes // 路由规则
})

export default router