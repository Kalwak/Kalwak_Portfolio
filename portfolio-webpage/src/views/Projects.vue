<!--
  PROJECTS VIEW
  STRUCTURE OF THIS SECTION
    - MAIN CONTAINER FOR PROJECTS SECTION
      - CATEGORY LIST // A COMPONENT WHERE THE CATEGORIES WILL BE PLACED
      - ROUTER-VIEW // WHEN A CATEGORY PAGE IS MATCHED ... IT WILL BE RENDERED HERE
--->
<template>
  <div class="col-12">
    <category-list />
    <router-view></router-view>
  </div>
</template>

<script>
// projects view,
import  CategoryList from '../components/sub-layout/category-list.vue';


export default {
  name: 'projects',

  components: {
    // category list component // for navigation based on categories
    CategoryList,
  },
}
</script>