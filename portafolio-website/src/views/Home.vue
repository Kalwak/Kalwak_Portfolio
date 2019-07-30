<template>
  <div class="col-12">
    <div class="banner">
      <div class="inner-wrapper">
        <div class="banner__text">
          <h2 class="banner__text-title">Desarrollo web</h2>
          <h3 class="banner__text-description">Soluciones Innovadoras</h3>
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
            <div class="image__container">
              <img :src="project.images.cover" :alt="project.name" class="project__image">
            </div>
            <div class="information__container">
              <h3 class="project__category">{{ project.category }}</h3>
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
  }
}
</script>
