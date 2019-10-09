<template>
  <div class="project-navigation">
    <div class="inner-wrapper">
      <span class="navigation__arrow leftControlArrow noselect" @click="prevSlide" :class="{ 'navigation__arrow--disabled': leftArrowDisabled }"><span class="icon-double-left-arrow"></span>anterior</span>
      <span class="navigation__arrow rightControlArrow noselect" @click="nextSlide" :class="{ 'navigation__arrow--disabled': rightArrowDisabled }">siguiente<span class="icon-double-right-arrow"></span></span>
    </div>
  </div>
</template>

<script>
// project navigation
import { mapGetters } from 'vuex';
import { mapState } from 'vuex';
import Swiper from 'swiper';


// @vuese
export default {
  name: 'project-navigation',
  
  data() {
    return {
      // used to disable left arrow
      leftArrowDisabled: false,
      
      // used to disable right arrow
      rightArrowDisabled: false,
    };
  },

  computed: {
    // getting values from store getters and state
    ...mapGetters(['numberOfProjects']),
    ...mapState({
      category: state => state.projects.projectsCategory,
    }),

    // initializate and returns the carousel object
    // which will be used to trigger its methods slideNext and slidePrev with Anterior y Seguiente buttons, when they are clicked
    carousel() {
      const carousel = new Swiper('.swiper-container', {
        // no touch swiping
        allowTouchMove: false,
      });
      return carousel;
    },
  },

  methods: {
    // @vuese
    // disable navigation arrows when number of projects is less than one
    // else enable them again, so set them to false
    disableArrowsByZeroProjects() {
      if (this.numberOfProjects < 2) {
        this.leftArrowDisabled = true;
        this.rightArrowDisabled = true;
      } 
      // else {
      //   this.leftArrowDisabled = false;
      //   this.rightArrowDisabled = false;
      // };
    },

    // @vuese
    // set true or false to data property leftArrowDisabled
    // @arg boolean
    setLeftArrowState(status) {
      this.leftArrowDisabled = status;
    },

    // @vuese
    // set true or false to data property rightArrowDisabled
    // @arg boolean
    setRightArrowState(status) {
      this.rightArrowDisabled = status;
    },

    // @vuese
    // disable Anterior o Siguiente arrows based 
    // on the current caousel slide index,
    // so if current caousel slide index is 0, then Anterior arrow should be disabled
    // the same to Siguiente arrow, but opposite case
    // @arg index, index value which comes from carousel current slide index
    disableArrowsByBoundaries(index) {
      // to disable left arrow
      if (index === 0) {
        this.setLeftArrowState(true);
      } else {
        this.setLeftArrowState(false);
      }

      // @vuese
      // to disable right arrow 
      if (index === this.numberOfProjects - 1) {
        this.setRightArrowState(true);
      } else {
        this.setRightArrowState(false);
      }
    },

    // @vuese
    //  create carousel to navigation for every project
    createProjectsCarousel() {
      const self = this;
      const carousel = new Swiper('.swiper-container', {
        // no touch swiping for carousel slides
        allowTouchMove: false,
      });
      let index = carousel.activeIndex;
      self.disableArrowsByBoundaries(index);
      carousel.activeIndex = 0;
    },

    // @vuese
    // triggered by Anterior button,
    // used to go to the prevous carousel slide and call disableArrowsByBoundaries method
    // to check if Anterior should be disabled
    prevSlide() {
      const self = this;
      self.carousel.slidePrev();
      let newSlideIndex = self.carousel.activeIndex;
      self.disableArrowsByBoundaries(newSlideIndex);
    },

    // @vuese
    // triggered by Siguiente button,
    // used to go to the next carousel slide and call disableArrowsByBoundaries method
    // to check if Siguiente should be disabled
    nextSlide() {
      const self = this;
      self.carousel.slideNext();
      let newSlideIndex = self.carousel.activeIndex;
      self.disableArrowsByBoundaries(newSlideIndex);
    },
  },

  watch: {
    // watcher for category computed property,
    // everytime category changes, a new carousel will be created
    // by calling createProjectsCarousel method
    // and disableArrowsByZeroProjects method will be called to check if there's not projects
    // then if so, disable navigation arrows
    category() {
      this.createProjectsCarousel();
      this.disableArrowsByZeroProjects();
    },
  },

  // used to call disableArrowsByZeroProjects method
  created() {
    this.disableArrowsByZeroProjects();
  },

  // used to call createProjectsCarousel method
  mounted() {
    this.createProjectsCarousel();
  },
}
</script>

