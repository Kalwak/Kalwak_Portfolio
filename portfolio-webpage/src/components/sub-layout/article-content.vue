<template>
  <div>
    <template v-for="(block, index) in blocks">
      <template v-if="block.type === 'header'">
        <heading  :level="block.data.level" :text="block.data.text" :key="index" />
      </template>
      <template v-if="block.type === 'paragraph'">
        <p :key="index" v-html="block.data.text" class="post__paragraph"></p>
      </template>
      <template v-if="block.type === 'image'">
        <img :key="index" :src="block.data.file.url" alt="" class="post__image" />
        <p  :key="'image-caption-' + index" class="post__image-caption" v-if="block.data.caption" v-html="block.data.caption"></p>
      </template>
      <template v-if="block.type === 'list' && block.data.style === 'ordered'">
        <ol class="post__list" :key="index">
          <li 
          v-for="(item, itemIndex) in block.data.items"
          :key="itemIndex"
          >
            {{ item }}
          </li>
        </ol>
      </template>
      <template v-if="block.type === 'list' && block.data.style === 'unordered'">
        <ul class="post__list" :key="index">
          <li 
          v-for="(item, itemIndex) in block.data.items"
          :key="itemIndex"
          >
            {{ item }}
          </li>
        </ul>
      </template>
      <template v-if="block.type === 'code'">
        <code class="post__code" :key="index">
        <pre>
{{ block.data.code }}
        </pre>
        </code>
      </template>
    </template>
  </div>
</template>

<script>
// component to where the post content data will be render 
import Heading from './utils/post-heading.js';



// @vuese
export default {
  name: 'article-content',
  props: {
    content: {
      type: Object,
      required: true
    }
  },

  components: {
    Heading
  },

  computed: {
    blocks() {
      return this.content.blocks;
    }
  },
};
</script>