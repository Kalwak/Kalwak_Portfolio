<template>
  <div class="project-container">
    <div class="project__header">
      <div class="inner-wrapper">
        <h3>{{ project.name }}</h3>
        <div class="project__carousel">
          <carousel 
          :per-page="1" 
          :loop="true"
          :autoplay="true"
          :autoplay-timeout="4000"
          :navigation-click-target-size="0"
          :navigation-enabled="true" 
          :pagination-enabled="false" 
          navigation-prev-label="<span  style='font-size: 1.8em;' class='icon-left-arrow'></span>"
          navigation-next-label="<span  style='font-size: 1.8em;' class='icon-right-arrow'></span>">
          <slide class="project__slide"
            v-for="(imageSrc, index) in project.images" :key="index">
            <img :src="imageSrc" :alt="project.title" />
          </slide>
        </carousel>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// project component
import { Carousel, Slide } from 'vue-carousel';


export default {
  name: 'project-card',

  components: {
    // from vue-carousel, this is the carousel main container
    Carousel,
    // from vue-carousel, this is the slide that goes into caoursel component
    Slide
  },

  props: {
    // object with project information like name, images, description, url
    project: {
      type: Object,
      required: true,
    },
  },
}
</script>
