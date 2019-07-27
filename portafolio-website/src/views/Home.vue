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
    <div class="projects-carousel">
    </div>
  </div>
</template>

<script>
import projectsInformation from '../projects-information.json';
import Swiper from 'swiper';


export default {
  name: 'home',
  data() {
    return {
      projectsInformation
    };
  },

  computed: {
    projects() {
      return this.projectsInformation;
    }
  },

  mounted() {}
}
</script>


<style lang="scss">
  @import url('https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.0/css/swiper.css');
</style>
