<template>
  <div class="blog-posts-cards-slider">
    <div class="posts-cards__container">
      <post-card />
      <post-card />
      <post-card />
      <post-card />
      <post-card />
      <post-card />
    </div>
    <div class="posts-cards__pagination">
      pagination here
    </div>
  </div>
</template>

<script>
// posts-cards-slider, use for showing posts-cards based on search category and filter restuls
// and also to provide a pagination
import PostCard from './post-card';


// @vuese
export default {
  name: 'blog-posts-cards',

  components: {
    PostCard
  },
}
</script>