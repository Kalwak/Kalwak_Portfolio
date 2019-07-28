<template>
  <div class="col-12">
    <div class="banner">
      <div class="inner-wrapper">
        <div class="banner__text">
          <h2 class="banner__text-title">Desarrollo web</h2>
          <p class="banner__text-description">Soluciones Innovadoras</p>
        </div>
      </div>
    </div>
    <div class="projects-container">
      <div class="inner-wrapper">
        <h3 class="projects__title">Trabajos anteriores</h3>
        <carousel 
          :per-page="1" 
          :loop="true"
          :autoplay="true"
          :autoplay-timeout="4000"
          :navigation-click-target-size="0"
          :navigation-enabled="true" 
          :pagination-enabled="false" 
          navigation-prev-label="<span class='icon-left-arrow'></span>"
          navigation-next-label="<span class='icon-right-arrow'></span>"
          class="projects-slider">
          <slide class="project-slide"
            v-for="project in projects" :key="project.id">
            <div class="img__container">
              <img :src="project.images.thumbnail" alt="" class="project__image">
            </div>
            <div class="information__container">
              <p class="project__category">{{ project.category }}</p>
            </div>
          </slide>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script>
import projectsInformation from '../projects-information.json';
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: 'home',
  data() {
    return {
      projectsInformation
    };
  },

  components: {
    Carousel,
    Slide
  },

  computed: {
    projects() {
      return this.projectsInformation;
    }
  },

  mounted() {
    const self = this;
  }
}
</script>
