<template>
  <Row :gutter="{ xs: 8, sm: 16, md: 24, lg: 32 }">
    <Col class="gutter-row" :span="18">
      <Collapse :items="extraCollapseItems" v-model:active-key="extraActiveKey">
        <template #extra="{ key }">
          <StarFilled v-if="key === '1'" @click.stop="handleClick(key)" />
          <StarOutlined v-if="key === '3'" @click.stop="handleClick(key)" />
        </template>
      </Collapse>
    </Col>
    <Col class="gutter-row" :span="6">
      <Scrollbar style="max-height: 500px" @scroll="onScroll" @scrollend="onScrollEnd">
        <List>
          <ListItem v-for="(data, index) in extraCollapseItems" :key="index" :title="data.title">
            <template #description>
              {{ data.header }}
            </template>
          </ListItem>
        </List>
      </Scrollbar>
    </Col>
  </Row>
</template>

<script setup lang="ts">
  import { ref, watchEffect } from 'vue'
  import { StarOutlined, StarFilled } from '@ant-design/icons-vue'
  import type { CollapseProps, CollapseItem } from 'vue-amazing-ui'
  const extraCollapseItems = ref<CollapseItem[]>([
    {
      key: '1',
      header: 'This is panel header 1',
      content:
        'A dog is a type of domesticated animal. Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.'
    },
    {
      key: '2',
      header: 'This is panel header 2',
      extra: 'Extra',
      content:
        'A dog is a type of domesticated animal. Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.'
    },
    {
      key: '3',
      header: 'This is panel header 3',
      content:
        'A dog is a type of domesticated animal. Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.'
    },
    {
      key: '4',
      header: 'This is panel header 1',
      content:
        'A dog is a type of domesticated animal. Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.'
    },
    {
      key: '5',
      header: 'This is panel header 2',
      extra: 'Extra',
      content:
        'A dog is a type of domesticated animal. Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.'
    },
    {
      key: '6',
      header: 'This is panel header 3',
      content:
        'A dog is a type of domesticated animal. Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.'
    }
  ])
  const extraActiveKey = ref<CollapseProps['activeKey']>(['1'])
  watchEffect(() => {
    console.log('extraActiveKey', extraActiveKey.value)
  })
  function handleClick(key: string | number) {
    console.log('key', key)
  }

    function onScroll(e: Event, direction: 'left' | 'right' | 'top' | 'bottom') {
    console.log('scroll', e, direction)
    }
    function onScrollEnd(e: Event, direction: 'left' | 'right' | 'top' | 'bottom') {
    console.log('scrollend', e, direction)
    }
</script>

<style scoped lang="scss">
</style>