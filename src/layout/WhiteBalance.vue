<script setup>
//页面内容来源： https://bigmodel.cn/dev/guidelines/VideoGeneration
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'
// 防抖
import { debounce } from 'lodash';
 
// 目录数据
const tocList = ref([])
const activeSection = ref('')
const articleRef = ref(null)
 
// 生成目录
const generateTOC = () => {
  const headings = articleRef.value.querySelectorAll('h2, h3')
  tocList.value = Array.from(headings).map(heading => ({
    id: heading.id,
    text: heading.innerText,
    level: parseInt(heading.tagName.substring(1))
  }))
}
 
// 平滑滚动到指定位置
let scrolling = false
const scrollTo = async (id) => {
  const target = document.getElementById(id)
  if (target) {
    scrolling = true
    activeSection.value = id
    target.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
 
    // 等待滚动结束
    await new Promise(resolve => {
        const scrollContainer = target.parentElement.parentElement;
        scrollContainer.addEventListener('scrollend', resolve, { once: true });
    });
    
    scrolling = false
  }
}
 
// 处理滚动事件
const handleScroll = (ev) => {
    if (scrolling) {// 点击目录滚动中
        return;
    }
  const headings = articleRef.value.querySelectorAll('h2, h3')
  headings.forEach(heading => {
    const rect = heading.getBoundingClientRect()
    if (rect.top > 100 && rect.top < 200) { // 约151px 的顶部偏移
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
    {prompt: '比得兔（主体）开小汽车（主体描述），<br>游走在马路上（环境描述），<br>脸上的表情充满开心喜悦（氛围设定）', 
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/4d81e8a7-b6c5-5658-b3d2-95656903476d_0.mp4'},
    {prompt: '一个金发碧眼的女人站在水里（环境描述），<br>一群粉红色的水母从水里游向天空（动作）', 
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/ea6590b2-cc71-5a3b-b728-6322fda5d5b4_0.mp4'},
    {prompt: '夜晚的丛林中，一只猫头鹰站在枯树枝上（环境描述），<br>猫头鹰的眼睛在月光下闪闪发亮（动作）。<br>背景是一片寂静的森林。', 
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/cb850ab9-fe6b-5745-9eeb-2895d08eb9a3_0.mp4'},
    {prompt: '深海里（环境描述）的一艘沉船（主体），<br>电影质感，由远到近（镜头语言）', 
    videoUrl: 'https://sfile.chatglm.cn/testpath/video/1aa1515f-1193-58bf-83d7-3bd62b765f62_0.mp4'},
]
const imageTableData = [
    {
        prompt:'星空缓慢旋转', 
        imageUrl:'https://cdn.bigmodel.cn/static/platform/images/usage-guide/cogvideo/1.png',
        videoUrl: 'https://cdn.bigmodel.cn/static/platform/videos/usage-guide/cogvideo/1.mp4'
    },
     {
        prompt:'风吹动她的头发', 
        imageUrl:'https://cdn.bigmodel.cn/static/platform/images/usage-guide/cogvideo/2.png',
        videoUrl: 'https://cdn.bigmodel.cn/static/platform/videos/usage-guide/cogvideo/3.mp4'
    },
     {
        prompt:'鸭子在游动', 
        imageUrl:'https://cdn.bigmodel.cn/static/platform/images/usage-guide/cogvideo/3.png',
        videoUrl: 'https://cdn.bigmodel.cn/static/platform/videos/usage-guide/cogvideo/2.mp4'
    },
]
</script>
 
<template>
  <el-container class="main-container">
    <!-- 文章内容 -->
    <el-main class="content" @scroll="handleScroll">
        <h1 id="toc-0">视频生成模型 Prompt工程</h1>
        <article ref="articleRef">
            <h2 id="toc-1">提示词元素</h2>
            <p>提示词的精确度与细节水平直接影响视频内容的质量。采用<strong>结构化提示词</strong>可以极大提升视频内容的符合度和专业性。<br>
    以下是构建提示词的关键组成部分：</p>
            <p><strong>提示词 = (镜头语言 +景别角度+ 光影) + 主体 (主体描述) + 主体运动 +场景 (场景描述) + (氛围)</strong></p>
            <ul>
                <li><strong>镜头语言</strong>: 通过镜头的各种应用以及镜头之间的衔接和切换来传达故事或信息，
                并创造出特定的视觉效果和情感氛围。如镜头平移，推近、拉远、升降拍摄、摇摄、跟随拍摄、手持拍摄、无人机航拍等;</li>
                <li><strong>景别角度</strong>：控制相机与被摄对象之间距离和角度，实现不同的视觉效果和情感表达。如大全景、中景、近景 、鸟瞰视角 、跟随视角、鱼眼效果等;</li>
                <li><strong>光影</strong>: 光影是赋予摄影作品灵魂的关键元素，光影的运用可以使照片更具深度，
                更具情感，我们可以通过光影创造出富有层次感和情感表达力的作品。如自然光、丁达尔效应、柔和散射、硬光直射 、逆光剪影、三点布光等;</li>
                <li><strong>主体</strong>: 主体是视频中的主要表现对象。如儿童、狮子、向日葵，汽车、城堡等;</li>
                <li><strong>主体描述</strong>: 对主体外貌细节和肢体姿态等的描述，如人物的服饰、动物的毛色、植物的颜色、物体的状态和建筑的风格;</li>
                <li><strong>主体运动</strong>: 对主体运动状态的描述，包括静止和运动等，运动状态不宜过于复杂，符合6s视频内可以展现的画面即可，</li>
                <li><strong>场景</strong>: 场景是主体所处的环境，包括前景、背景等;</li>
                <li><strong>场景描述</strong>: 对主体所处环境的细节描述。如都市环境、乡村风光、工业区等;</li>
                <li><strong>氛围</strong>: 对预期视频画面的氛围描述。如喧嚣繁忙、悬疑惊悚、宁静舒适等;</li>
            </ul>
 
            <h2 id="toc-2">提示词技巧</h2>
            <ul>
    <li><strong>关键词重复</strong>：在提示的不同部分重复或强化关键词有助于提高输出的一致性。如摄像机以<strong>超高速</strong>镜头<strong>快速</strong>飞过森林。</li>
    <li><strong>聚焦内容</strong>：提示词应集中在视频中应有的内容上。如：冷清的街道，而不是“没有人的街道”。</li>
    <li><strong>使用智能体</strong>：使用 <a href="https://chatglm.cn/main/gdetail/669911fe0bef38883947d3c6" target="_blank">提示词智能体</a> 帮助你生成专业提示词。</li>
            </ul>
 
            <h2 id="toc-3">文生视频示例</h2>
            <el-table :data="textTableData" border style="width: 100%">
                <el-table-column prop="prompt" label="Prompt" width="350">
                    <template #default="{ row }">
                        <div v-html="row.prompt"></div>
                    </template>
                </el-table-column>
                <el-table-column prop="videoUrl" label="视频" >
                    <template #default="{ row }">
                        <video :src="row.videoUrl" controls loading="lazy" width="480"></video>
                    </template>
                </el-table-column>
            </el-table>
 
            <h2 id="toc-4">图生视频示例</h2>
            <p>CogVideoX 可以将用户提供的静态图像转化为6秒的动态视频。为达到最佳效果，推荐上传比例为<strong>3:2</strong>的图片，
            并且文件格式为 PNG 或 JPEG，文件大小不超过5MB。<strong>提示词建议使用“主体（背景）+ 运动描述”的表达方式。</strong>
            </p>
            <el-table :data="imageTableData" border style="width: 100%">
                <el-table-column prop="prompt" label="Prompt" width="350">
                    <template #default="{ row }">
                        <el-image class="w-320" :src="row.imageUrl" :preview-src-list="[row.imageUrl]" lazy />
                        <p>{{ row.prompt }}</p>
                    </template>
                </el-table-column>
                <el-table-column prop="videoUrl" label="视频" >
                    <template #default="{ row }">
                        <video :src="row.videoUrl" controls loading="lazy" width="480"></video>
                    </template>
                </el-table-column>
            </el-table>
        </article>
      
    </el-main>
    <!-- 侧边目录 -->
    <el-aside width="150px">
      <div class="toc-container">
        <h3 class="toc-heading mb-15">教程目录</h3>
        <ul class="toc-items">
            <li v-for="(item, index) in tocList" :key="index" class="toc-item">
                <!-- :href="'#'+item.id" -->
                <a :class="{ 'active': activeSection === item.id, 'toc-link': true}"  @click="scrollTo(item.id)">{{ item.text }}</a>
            </li>
        </ul>
      </div>
    </el-aside>
  </el-container>
</template>
 
<style scoped>
/* 计算高度 */
.main-container {
  height: calc(100vh - 100px);
}
.main-container h1 {
    font-size: 32px;
    margin-bottom: 40px;
}
.main-container h2 {
    font-size: 24px;
    margin: 65px 0 32px 0;
    border: none;
}
.toc-container {
    margin-left: 2.5rem;
}
 
article {
  line-height: 1.7;
}
.toc-items {
    list-style: none;
    padding: 0;
    margin: 12px 0 0;
    line-height: 1.6;
}
.toc-items .toc-item {
    margin-top: 10px;
    font-size: 12px;
}
.toc-item .toc-link {
    position: relative;
    color: var(--el-color-info);
    transition: color var(--el-transition-duration);
}
.toc-item .toc-link.active {
    color: var(--el-text-color-primary);
}
/* 活跃目录添加虚拟边框 */
.toc-item .toc-link.active:before {
    content: "";
    position: absolute;
    left: -6px;
    border-left: 4px solid var(--el-color-primary);
    top: 50%;
    -webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    transform: translateY(-50%);
    height: 60%;
}
</style>