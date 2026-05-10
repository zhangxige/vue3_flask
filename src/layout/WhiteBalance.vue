<script lang="ts" setup>
//页面内容来源： https://bigmodel.cn/dev/guidelines/VideoGeneration
import { ref, onMounted, nextTick } from 'vue'

// 目录数据
interface TocItem {
  id: string
  text: string
  level: number
}
const tocList = ref<TocItem[]>([])
const activeSection = ref('')
const articleRef = ref<HTMLElement | null>(null)

// 生成目录
const generateTOC = () => {
  if (!articleRef.value) {
    return
  }
  const headings = articleRef.value.querySelectorAll('h2, h3') as NodeListOf<HTMLElement>
  tocList.value = Array.from(headings).map((heading) => ({
    id: heading.id,
    text: heading.innerText,
    level: parseInt(heading.tagName.substring(1)),
  }))
}

// 平滑滚动到指定位置
let scrolling = false
const scrollTo = async (id: string) => {
  const target = document.getElementById(id)
  if (target) {
    scrolling = true
    activeSection.value = id
    target.scrollIntoView({
      behavior: 'smooth',
      block: 'start',
    })

    // 等待滚动结束
    await new Promise<void>((resolve) => {
      const scrollContainer = target.parentElement?.parentElement
      if (scrollContainer) {
        scrollContainer.addEventListener('scrollend', () => resolve(), { once: true })
      } else {
        resolve()
      }
    })

    scrolling = false
  }
}

// 处理滚动事件
const handleScroll = () => {
  if (scrolling) {
    // 点击目录滚动中
    return
  }
  if (!articleRef.value) {
    return
  }
  const headings = articleRef.value.querySelectorAll('h2, h3') as NodeListOf<HTMLElement>
  headings.forEach((heading) => {
    const rect = heading.getBoundingClientRect()
    if (rect.top > 100 && rect.top < 200) {
      // 约151px 的顶部偏移
      activeSection.value = heading.id
    }
  })
}

onMounted(() => {
  nextTick(() => {
    generateTOC()
  })
})

const textTableData = [
  {
    prompt:
      '比得兔（主体）开小汽车（主体描述），<br>游走在马路上（环境描述），<br>脸上的表情充满开心喜悦（氛围设定）',
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/4d81e8a7-b6c5-5658-b3d2-95656903476d_0.mp4',
  },
  {
    prompt: '一个金发碧眼的女人站在水里（环境描述），<br>一群粉红色的水母从水里游向天空（动作）',
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/ea6590b2-cc71-5a3b-b728-6322fda5d5b4_0.mp4',
  },
  {
    prompt:
      '夜晚的丛林中，一只猫头鹰站在枯树枝上（环境描述），<br>猫头鹰的眼睛在月光下闪闪发亮（动作）。<br>背景是一片寂静的森林。',
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/cb850ab9-fe6b-5745-9eeb-2895d08eb9a3_0.mp4',
  },
  {
    prompt: '深海里（环境描述）的一艘沉船（主体），<br>电影质感，由远到近（镜头语言）',
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/1aa1515f-1193-58bf-83d7-3bd62b765f62_0.mp4',
  },
]
const imageTableData = [
  {
    prompt: '星空缓慢旋转',
    imageUrl: 'https://cdn.bigmodel.cn/static/platform/images/usage-guide/cogvideo/1.png',
    videoUrl: 'https://cdn.bigmodel.cn/static/platform/videos/usage-guide/cogvideo/1.mp4',
  },
  {
    prompt: '风吹动她的头发',
    imageUrl: 'https://cdn.bigmodel.cn/static/platform/images/usage-guide/cogvideo/2.png',
    videoUrl: 'https://cdn.bigmodel.cn/static/platform/videos/usage-guide/cogvideo/3.mp4',
  },
  {
    prompt: '鸭子在游动',
    imageUrl: 'https://cdn.bigmodel.cn/static/platform/images/usage-guide/cogvideo/3.png',
    videoUrl: 'https://cdn.bigmodel.cn/static/platform/videos/usage-guide/cogvideo/2.mp4',
  },
]
</script>

<template>
  <el-container class="main-container">
    <el-main class="content" @scroll="handleScroll">
      <div class="page-header">
        <div class="page-meta">
          <p class="eyebrow">视频生成模型</p>
          <h1 id="toc-0">Prompt 工程与示例指南</h1>
          <p class="subtitle">结构化提示词写法提升文生视频与图生视频质量，示例直观易懂。</p>
        </div>
        <div class="summary-cards">
          <div class="card mini-card">
            <span>提示词结构</span>
            <strong>镜头 + 主体 + 场景 + 氛围</strong>
          </div>
          <div class="card mini-card">
            <span>图生视频建议</span>
            <strong>3:2 比例 / PNG-JPEG / 5MB 内</strong>
          </div>
        </div>
      </div>

      <article ref="articleRef">
        <section class="section-block">
          <h2 id="toc-1">提示词元素</h2>
          <p>
            提示词的精确度与细节水平直接影响视频内容的质量。采用<strong>结构化提示词</strong>可以极大提升视频内容的符合度和专业性。
          </p>
          <p class="highlight-text">
            <strong
              >提示词 = (镜头语言 + 景别角度 + 光影) + 主体 (主体描述) + 主体运动 + 场景 (场景描述)
              + (氛围)</strong
            >
          </p>
          <ul>
            <li>
              <strong>镜头语言</strong>:
              通过镜头的应用与切换传达故事，创造视觉效果与情感氛围，如平移、推近、拉远、跟随、航拍等。
            </li>
            <li>
              <strong>景别角度</strong>:
              控制相机与主体的距离与角度，实现不同视觉表达，如大全景、中景、近景、鸟瞰、跟随视角。
            </li>
            <li>
              <strong>光影</strong>:
              光影打造层次与氛围，如自然光、柔光、逆光剪影、丁达尔效应、三点布光等。
            </li>
            <li><strong>主体</strong>: 视频中的核心表现对象，如人物、动物、建筑、景物等。</li>
            <li><strong>主体描述</strong>: 细化主体外貌、姿态、状态与风格。</li>
            <li>
              <strong>主体运动</strong>:
              描述主体的移动或姿态变化，合理控制动作复杂度，适配短视频节奏。
            </li>
            <li><strong>场景</strong>: 主体所在的环境，包括前景、背景与空间氛围。</li>
            <li><strong>场景描述</strong>: 描述环境细节，如城市、乡村、工业区、夜景等。</li>
            <li><strong>氛围</strong>: 设定画面情绪，如宁静、悬疑、梦幻、活力等。</li>
          </ul>
        </section>

        <section class="section-block">
          <h2 id="toc-2">提示词技巧</h2>
          <ul>
            <li>
              <strong>关键词重复</strong
              >：不同段落中重复重点关键词有助输出一致性，例如“超高速镜头快速飞过森林”。
            </li>
            <li>
              <strong>聚焦内容</strong
              >：提示词应集中在关键元素上，避免模糊描述，例如“冷清的街道”胜过“没有人的街道”。
            </li>
            <li>
              <strong>使用智能体</strong>：借助
              <a href="https://chatglm.cn/main/gdetail/669911fe0bef38883947d3c6" target="_blank"
                >提示词智能体</a
              >
              生成更专业的表达。
            </li>
          </ul>
        </section>

        <section class="section-block">
          <div class="section-title-row">
            <h2 id="toc-3">文生视频示例</h2>
            <span class="label">Prompt → Video</span>
          </div>
          <div class="table-wrapper">
            <el-table :data="textTableData" border style="width: 100%" class="demo-table">
              <el-table-column prop="prompt" label="Prompt" width="360">
                <template #default="{ row }">
                  <div v-html="row.prompt" class="prompt-text"></div>
                </template>
              </el-table-column>
              <el-table-column prop="videoUrl" label="视频">
                <template #default="{ row }">
                  <video :src="row.videoUrl" controls loading="lazy" class="demo-video"></video>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </section>

        <section class="section-block">
          <div class="section-title-row">
            <h2 id="toc-4">图生视频示例</h2>
            <span class="label">Image → Video</span>
          </div>
          <p>
            CogVideoX 可将静态图像转为 6 秒动态视频。推荐 3:2 比例图片，格式为
            PNG/JPEG，文件大小不超过 5MB。
          </p>
          <div class="table-wrapper">
            <el-table :data="imageTableData" border style="width: 100%" class="demo-table">
              <el-table-column prop="prompt" label="Prompt" width="360">
                <template #default="{ row }">
                  <div class="image-cell">
                    <el-image
                      class="demo-image"
                      :src="row.imageUrl"
                      :preview-src-list="[row.imageUrl]"
                      lazy
                    />
                    <p>{{ row.prompt }}</p>
                  </div>
                </template>
              </el-table-column>
              <el-table-column prop="videoUrl" label="视频">
                <template #default="{ row }">
                  <video :src="row.videoUrl" controls loading="lazy" class="demo-video"></video>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </section>
      </article>
    </el-main>

    <el-aside width="260px" class="toc-aside">
      <div class="toc-container">
        <h3 class="toc-heading">章节导航</h3>
        <ul class="toc-items">
          <li v-for="(item, index) in tocList" :key="index" class="toc-item">
            <button
              type="button"
              class="toc-link"
              :class="{ active: activeSection === item.id }"
              @click="scrollTo(item.id)"
            >
              {{ item.text }}
            </button>
          </li>
        </ul>
      </div>
    </el-aside>
  </el-container>
</template>

<style scoped>
/* 页面整体 */
.main-container {
  height: calc(100vh - 60px);
  min-height: 720px;
  border-radius: 24px;
  overflow: hidden;
  background: linear-gradient(180deg, #f8fbff 0%, #eef2ff 100%);
  box-shadow: 0 28px 60px rgba(31, 41, 55, 0.08);
}

.content {
  padding: 32px 30px 30px;
  overflow-y: auto;
  background: transparent;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 24px;
  margin-bottom: 28px;
  flex-wrap: wrap;
}

.page-meta {
  max-width: 720px;
}

.eyebrow {
  margin: 0 0 12px;
  color: #5b63d3;
  font-size: 0.85rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.page-meta h1 {
  margin: 0;
  font-size: clamp(2.4rem, 2.9vw, 3.2rem);
  line-height: 1.05;
  color: #12204e;
}

.subtitle {
  margin: 16px 0 0;
  color: #475569;
  font-size: 1rem;
  max-width: 680px;
}

.summary-cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  width: 100%;
  max-width: 420px;
}

.card {
  border-radius: 20px;
  padding: 20px 18px;
  background: #ffffff;
  border: 1px solid rgba(96, 103, 191, 0.14);
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.06);
}

.mini-card span {
  display: block;
  margin-bottom: 12px;
  color: #6b7280;
  font-size: 0.88rem;
}

.mini-card strong {
  display: block;
  color: #1e223a;
  font-size: 0.98rem;
  line-height: 1.4;
}

article {
  line-height: 1.8;
  color: #334155;
}

.section-block {
  margin-bottom: 32px;
  padding: 28px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(148, 163, 184, 0.18);
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.05);
}

.section-title-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 18px;
  flex-wrap: wrap;
}

.section-block h2 {
  margin: 0;
  font-size: 1.6rem;
  color: #0f172a;
}

.highlight-text {
  margin: 18px 0;
  padding: 18px;
  border-radius: 18px;
  background: #eef2ff;
  color: #1e3a8a;
  font-weight: 600;
}

.section-block ul {
  margin: 0;
  padding-left: 1.25rem;
}

.section-block ul li {
  margin-bottom: 14px;
}

.section-block a {
  color: #3b82f6;
  text-decoration: none;
}

.section-block a:hover {
  text-decoration: underline;
}

.table-wrapper {
  margin-top: 16px;
}

.demo-table {
  border-radius: 20px;
  overflow: hidden;
}

:deep(.demo-table .el-table__body-wrapper) {
  min-height: 180px;
}

.prompt-text {
  font-size: 0.96rem;
  color: #1f2937;
  line-height: 1.7;
}

.image-cell {
  display: grid;
  gap: 14px;
  align-items: start;
}

.demo-image {
  width: 100%;
  border-radius: 16px;
  min-height: 190px;
  object-fit: cover;
}

.demo-video {
  width: 100%;
  min-height: 220px;
  border-radius: 18px;
  background: #000;
}

.toc-aside {
  background: rgba(255, 255, 255, 0.92);
  border-left: 1px solid rgba(148, 163, 184, 0.18);
  padding: 32px 24px;
}

.toc-container {
  position: sticky;
  top: 24px;
}

.toc-heading {
  margin: 0 0 18px 0;
  font-size: 1.05rem;
  color: #0f172a;
}

.toc-items {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-item {
  margin-bottom: 14px;
}

.toc-link {
  width: 100%;
  text-align: left;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 0.95rem;
  color: #475569;
  background: transparent;
  border: none;
  padding: 8px 12px;
  border-radius: 14px;
  cursor: pointer;
  transition:
    background-color 0.2s ease,
    color 0.2s ease;
}

.toc-link:hover {
  background: rgba(59, 130, 246, 0.08);
}

.toc-link.active {
  color: #1e3a8a;
  background: rgba(59, 130, 246, 0.15);
}

.toc-link.active:before {
  content: '';
  width: 4px;
  height: 100%;
  background: #2563eb;
  border-radius: 999px;
  margin-right: 8px;
}

@media (max-width: 1100px) {
  .main-container {
    height: auto;
  }

  .page-header,
  .summary-cards {
    grid-template-columns: 1fr;
  }

  .toc-aside {
    width: 100% !important;
    order: 2;
    border-left: none;
    border-top: 1px solid rgba(148, 163, 184, 0.18);
    padding-top: 28px;
  }
}

@media (max-width: 840px) {
  .page-header {
    flex-direction: column;
  }

  .summary-cards {
    grid-template-columns: 1fr;
  }

  .section-block {
    padding: 24px 20px;
  }

  .toc-aside {
    padding: 24px 20px;
  }
}

@media (max-width: 640px) {
  .main-container {
    border-radius: 0;
    box-shadow: none;
  }

  .content {
    padding: 20px;
  }

  .demo-video,
  .demo-image {
    min-height: 180px;
  }
}
</style>
