<!--
  PROJECTS VIEW
  STRUCTURE OF THIS SECTION
    - MAIN CONTAINER FOR PROJECTS SECTION
      - CATEGORY LIST // A COMPONENT WHERE THE CATEGORIES WILL BE PLACED
      - ROUTER-VIEW // WHEN A CATEGORY PAGE IS WATCHED ... IT WILL BE RENDERED HERE
--->
<template>
  <div class="col-12">
    <category-list />
    <div class="inner-wrapper">
      <!-- /projects/category/category-name -->
      <router-view></router-view>
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

