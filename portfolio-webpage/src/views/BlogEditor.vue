<template>
  <div class="col-12">
    <post-editor />
  </div>
</template>

<script>
// editor view, which has an editor component to create blog posts
import PostEditor from '../components/editor/editor';


export default {
  name: 'blog-editor',
  components: {
    PostEditor
  }
}
</script>