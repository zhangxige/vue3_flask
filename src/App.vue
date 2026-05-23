<template>
  <div class="app-container">
    <el-container class="main-container">
      <el-header class="app-header">
        <div class="header-left">
          <div class="logo-section">
            <img
              style="width: 100px"
              src="./images/element-plus-logo.svg"
              alt="Element logo"
            />
            <span class="logo-text">ImageLab</span>
          </div>
        </div>
        <div class="header-right">
          <span class="app-tagline">Professional Image Processing Suite</span>
        </div>
      </el-header>
      <el-container class="body-container">
        <el-aside :width="isCollapse ? '64px' : '260px'" class="app-aside">
          <div class="aside-toggle" @click="toggleCollapse">
            <el-icon :size="20">
              <Expand v-if="isCollapse" />
              <Fold v-else />
            </el-icon>
          </div>
          <el-scrollbar class="aside-scrollbar">
            <el-menu
              :default-active="route.path"
              :collapse="isCollapse"
              :collapse-transition="true"
              background-color="transparent"
              text-color="rgba(255,255,255,0.75)"
              active-text-color="#ffffff"
              router
              class="side-menu"
            >
              <template v-for="group in navGroups" :key="group.label">
                <el-sub-menu :index="group.label">
                  <template #title>
                    <el-icon><component :is="group.icon" /></el-icon>
                    <span>{{ group.label }}</span>
                  </template>
                  <el-menu-item
                    v-for="item in group.children"
                    :key="item.path"
                    :index="item.path"
                  >
                    <el-icon><component :is="item.icon" /></el-icon>
                    <span>{{ item.name }}</span>
                  </el-menu-item>
                </el-sub-menu>
              </template>
            </el-menu>
          </el-scrollbar>
        </el-aside>
        <el-main class="app-main">
          <div class="page-wrapper">
            <RouterView />
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import {
  Expand,
  Fold,
  Sunny,
  Moon,
  Histogram,
  MagicStick,
  PictureFilled,
  Aim,
  ColdDrink,
  SetUp,
  BrushFilled,
  Filter,
  DataAnalysis,
} from '@element-plus/icons-vue'

const route = useRoute()
const isCollapse = ref(false)

const toggleCollapse = () => {
  isCollapse.value = !isCollapse.value
}

interface NavItem {
  path: string
  name: string
  icon: object
}

interface NavGroup {
  label: string
  icon: object
  children: NavItem[]
}

const navGroups: NavGroup[] = [
  {
    label: 'Color & Tone',
    icon: BrushFilled,
    children: [
      { path: '/Color', name: 'Color', icon: BrushFilled },
      { path: '/WhiteBalance', name: 'White Balance', icon: Sunny },
      { path: '/Hue', name: 'Hue', icon: Filter },
      { path: '/Saturation', name: 'Saturation', icon: ColdDrink },
    ],
  },
  {
    label: 'Lighting',
    icon: Sunny,
    children: [
      { path: '/Brightness', name: 'Brightness', icon: Sunny },
      { path: '/Exposure', name: 'Exposure', icon: Histogram },
      { path: '/Contrast', name: 'Contrast', icon: DataAnalysis },
    ],
  },
  {
    label: 'Detail',
    icon: MagicStick,
    children: [
      { path: '/Sharpness', name: 'Sharpness', icon: Aim },
      { path: '/Clarity', name: 'Clarity', icon: MagicStick },
      { path: '/Noise', name: 'Noise', icon: SetUp },
    ],
  },
  {
    label: 'Others',
    icon: PictureFilled,
    children: [
      { path: '/Image', name: 'Image', icon: PictureFilled },
      { path: '/Interactive', name: 'Interactive', icon: Moon },
      { path: '/Learn_Test', name: 'Learn Test', icon: SetUp },
    ],
  },
]
</script>

<style>
html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #f0f2f5;
}

.app-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-container {
  height: 100%;
}

.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px !important;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding: 0 24px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  z-index: 100;
}

.header-left {
  display: flex;
  align-items: center;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-section img {
  filter: brightness(0) invert(1);
  opacity: 0.9;
}

.logo-text {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 1px;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.app-tagline {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 0.5px;
}

.body-container {
  height: calc(100vh - 60px);
}

.app-aside {
  background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
  border-right: 1px solid rgba(255, 255, 255, 0.06);
  transition: width 0.3s ease;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.aside-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  cursor: pointer;
  color: rgba(255, 255, 255, 0.6);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.aside-toggle:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.05);
}

.aside-scrollbar {
  flex: 1;
}

.aside-scrollbar .el-scrollbar__view {
  height: 100%;
}

.side-menu {
  border-right: none !important;
  padding: 8px 0;
}

.side-menu .el-sub-menu__title {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.5px;
  height: 48px;
  line-height: 48px;
}

.side-menu .el-sub-menu__title:hover {
  background: rgba(255, 255, 255, 0.06) !important;
}

.side-menu .el-menu-item {
  height: 42px;
  line-height: 42px;
  font-size: 13px;
  border-radius: 0 20px 20px 0;
  margin: 2px 16px 2px 0;
  padding-left: 56px !important;
}

.side-menu .el-menu-item:hover {
  background: rgba(255, 255, 255, 0.08) !important;
}

.side-menu .el-menu-item.is-active {
  background: linear-gradient(90deg, rgba(64, 158, 255, 0.25) 0%, transparent 100%) !important;
  color: #ffffff !important;
  font-weight: 600;
  border-right: 3px solid #409eff;
}

.side-menu .el-sub-menu.is-active > .el-sub-menu__title {
  color: rgba(255, 255, 255, 0.95) !important;
}

.app-main {
  background: #f0f2f5;
  padding: 0;
  overflow: auto;
}

.page-wrapper {
  min-height: 100%;
}
</style>
