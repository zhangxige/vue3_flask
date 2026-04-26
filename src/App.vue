<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
        @select="handleSelect"
      >
        <el-menu-item index="0">
          <img
            style="width: 100px"
            src="./images/element-plus-logo.svg"
            alt="Element logo"
          />
        </el-menu-item>
        <el-menu-item index="1">Processing Center</el-menu-item>
        <el-sub-menu index="2">
          <template #title>Workspace</template>
          <el-menu-item index="2-1">item one</el-menu-item>
          <el-menu-item index="2-2">item two</el-menu-item>
          <el-menu-item index="2-3">item three</el-menu-item>
          <el-sub-menu index="2-4">
            <template #title>item four</template>
            <el-menu-item index="2-4-1">item one</el-menu-item>
            <el-menu-item index="2-4-2">item two</el-menu-item>
            <el-menu-item index="2-4-3">item three</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
      </el-menu>
      </el-header>
      <el-container>
        <el-aside width="300px">
            <el-row class="tac">
              <el-col :span="12">
                <h5 class="mb-2" style="text-align: left;">
                  <el-icon><Expand /></el-icon>Navigator
                </h5>
                <el-menu
                  active-text-color="#ffd04b"
                  background-color="#ffffff"
                  class="el-menu-vertical-demo"
                  default-active="1"
                  text-color="#000"
                  router="true"
                  @open="handleOpen"
                  @close="handleClose"
                >
                  <el-sub-menu index="1">
                    <template #title>
                      <el-icon><location /></el-icon>
                      <span>Navigator One</span>
                    </template>
                    <el-menu-item-group title="Group One">
                      <el-menu-item index="/WhiteBalance">WhiteBalance</el-menu-item>
                      <el-menu-item index="/Hue">Hue</el-menu-item>
                      <el-menu-item index="/Interactive">Interactive</el-menu-item>
                    </el-menu-item-group>
                    <el-menu-item-group title="Group Two">
                      <el-menu-item index="/Sharpness">Sharpness</el-menu-item>
                      <el-menu-item index="/Contrast">Contrast</el-menu-item>
                    </el-menu-item-group>
                    <el-sub-menu index="1-4">
                      <template #title>item four</template>
                      <el-menu-item index="/Noise">item one</el-menu-item>
                    </el-sub-menu>
                    <el-sub-menu index="1-5">
                      <template #title>Learn_Test</template>
                      <el-menu-item index="/Learn_Test">Learn_Test</el-menu-item>
                    </el-sub-menu>
                  </el-sub-menu>
                  <el-menu-item index="2">
                    <el-icon><icon-menu /></el-icon>
                    <span>Navigator Two</span>
                  </el-menu-item>
                  <el-menu-item index="3">
                    <el-icon><document /></el-icon>
                    <span>Navigator Three</span>
                  </el-menu-item>
                  <el-menu-item index="4">
                    <el-icon><setting /></el-icon>
                    <span>Navigator Four</span>
                  </el-menu-item>
                  <el-menu-item index="5">
                    <el-icon><setting /></el-icon>
                    <span>Navigator Five</span>
                  </el-menu-item>
                  <el-menu-item index="6">
                    <el-icon><setting /></el-icon>
                    <span>Navigator Six</span>
                  </el-menu-item>
                </el-menu>
              </el-col>
            </el-row>
        </el-aside>
        <el-main>
           <RouterView />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>


<script lang="ts" setup>
import {
  Document,
  Expand,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
import {ref} from 'vue'

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.el-menu--horizontal > .el-menu-item:nth-child(1) {
  margin-right: auto;
}
.h5{
  margin: 10px;
  padding: 10px;
  border-spacing: 10px;
  font-size: 20px;
  text-align: center;
}
</style>






