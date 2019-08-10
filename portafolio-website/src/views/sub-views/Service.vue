<!--
  SERVICE COMPONENT
  STRUCTURE OF THIS SECTION
    - SERVICE-CONTAINER
      - SERVICE__NAME
        - INNER-WRAPPER // LIMIT PAGE ELEMENT WIDTH
      - SERVICE DESCRIPTION
      - INNER-WRAPPER 
        - CAROUSEL
          - SLIDE
      - BUTTON FOR CONTACT // u-button
-->
<template>
  <div class="service-container">
    <h3 class="service__name">
        <div class="inner-wrapper">
          {{ service.name }}
        </div>
    </h3>
    <div class="inner-wrapper">
        <p class="service__description">
          {{ service.description }}
        </p>
    </div>
    <div class="service__carousel">
      <div class="inner-wrapper">
        <carousel 
          class="project__carousel"
          :key="serviceCategory"
          :per-page="1" 
          :loop="true"
          :autoplay="true"
          :autoplay-timeout="4000"
          :pagination-enabled="false"
          :navigation-enabled="true"
          navigation-prev-label="<span class='icon-left-arrow carousel__arrow'></span>"
          navigation-next-label="<span class='icon-right-arrow carousel__arrow'></span>">
          <slide class="project__carousel__slide" v-for="(imageSrc, index) in images" :key="index">
            <div class="project__images">
              <img :src="imageSrc" alt="category" />
            </div>
        </slide>
      </carousel>
      </div>
    </div>
    <div class="inner-wrapper text-center mt-3">
      <button class="u-button">Cotizar</button>
    </div>
  </div>
</template>

<script>
// service component
import services from '../../services.json';
import projects from '../../projects-information.json';
import { Carousel, Slide } from 'vue-carousel';


export default {
  name: 'service',

  data() {
    return {
      // projects information
      projects,
    };
  },

  components: {
    // from vue-carousel
    Carousel,
    // from vue-carousel
    Slide,
  },

  computed: {
    // returns the service that match the current category
    service() {
      return services.find(service => service.category === this.serviceCategory)
    },

    // return current page category
    serviceCategory() {
      return this.$route.params.service.split('-').join(' ');
    },


    // returns images from each project 
    // NOTE: this is temporal because I think defferent images has to be here
    images() {
      return this.projects.reduce((arr, project) =>  arr.concat(project.images) ,[]); 
    },
  },
}
</script>

