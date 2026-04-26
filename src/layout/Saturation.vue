<template>
  <Flex vertical>
    <Radio :options="sizeOptions" v-model:value="size" button button-style="solid" />
    <Steps :items="minStepsItems" :size="size" :current="current" />
  </Flex>
</template>

<script setup lang="ts">
    import { ref, watchEffect } from 'vue'
    import type { StepsItem } from 'vue-amazing-ui'
    const minStepsItems = ref<StepsItem[]>([
    {
        title: 'Step 1'
    },
    {
        title: 'Step 2'
    },
    {
        title: 'Step 3'
    }
    ])
    const sizeOptions = [
    {
        label: 'default',
        value: 'default'
    },
    {
        label: 'small',
        value: 'small'
    }
    ]
    const size = ref('small')
    const current = ref(2)
    watchEffect(() => {
    console.log('current', current.value)
    })
</script>
