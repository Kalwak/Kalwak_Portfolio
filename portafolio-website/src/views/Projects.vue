<template>
  <div class="col-12">
    <category-list />
    <div class="inner-wrapper">
    </div>
  </div>
</template>

<script>
import  CategoryList from '../components/sub-layout/category-list.vue';


export default {
  name: 'projects',
  components: {
    CategoryList
  }
}
</script>

