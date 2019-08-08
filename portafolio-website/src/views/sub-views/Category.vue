<!--
  PROJECTS CATEGORY
  STRUCTURE OF THIS SECTION
    .project-category - main container for categories
      - project-navigation // component that provices arrow (left & right) to swtich between projects that belong to this category 
        - swiper-container // 
--->
<template>
  <div class="project-category">
    <project-navigation />

    <div class="swiper-container" v-if="projects">
      <div class="swiper-wrapper">
        <div class="swiper-slide" v-for="project in projects" :key="project.pageId">
          <project-card :key="projects.id" :project="project" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// category view
import { mapState } from 'vuex';
import ProjectNavigation from '@/components/sub-layout/project-navigation.vue';
import ProjectCard from '@/components/sub-layout/project.vue';


export default {
  name: 'category',

  components: {
    // navigation arrows to go through projects sections
    ProjectNavigation,
    ProjectCard,
  },

  computed: {
    ...mapState({
      projects: state => state.projects.projects,
    }),
  },
}
</script>

