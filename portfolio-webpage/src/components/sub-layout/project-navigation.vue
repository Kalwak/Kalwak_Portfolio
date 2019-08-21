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
    ...mapGetters(['numberOfProjects']),
    ...mapState({
      category: state => state.projects.projectsCategory,
    }),
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
    // set true or false
    // @arg boolean
    setLeftArrowState(status) {
      this.leftArrowDisabled = status;
    },

    // @vuese
    // set true or false
    // @arg boolean
    setRightArrowState(status) {
      this.rightArrowDisabled = status;
    },

    // @vuese
    // disable arrows if limit
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
    //  create carousel and navigation for every project
    // of the current categroy 
    createProjectsCarousel() {
      const self = this;
      const carousel = new Swiper('.swiper-container', {
        // no touch swiping
        allowTouchMove: false,
      });
      let index = carousel.activeIndex;
      self.disableArrowsByBoundaries(index);
      carousel.activeIndex = 0;
    },

    prevSlide() {
      const self = this;
      self.carousel.slidePrev();
      let newSlideIndex = self.carousel.activeIndex;
      self.disableArrowsByBoundaries(newSlideIndex);
    },

    nextSlide() {
      const self = this;
      self.carousel.slideNext();
      let newSlideIndex = self.carousel.activeIndex;
      self.disableArrowsByBoundaries(newSlideIndex);
    },
  },

  watch: {
    category() {
      this.createProjectsCarousel();
      this.disableArrowsByZeroProjects();
    },
  },

  created() {
    this.disableArrowsByZeroProjects();
  },

  mounted() {
    this.createProjectsCarousel();
  },
}
</script>

