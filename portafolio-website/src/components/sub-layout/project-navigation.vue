<template>
  <div class="project-navigation">
    <div class="inner-wrapper">
      <span class="navigation__arrow leftControlArrow noselect" :class="{ 'navigation__arrow--disabled': leftArrowDisabled }"><span class="icon-double-left-arrow"></span>anterior</span>
      <span class="navigation__arrow rightControlArrow noselect" :class="{ 'navigation__arrow--disabled': rightArrowDisabled }">siguiente<span class="icon-double-right-arrow"></span></span>
    </div>
  </div>
</template>

<script>
// project navigation
import { mapGetters } from 'vuex';
import { mapState } from 'vuex';
import Swiper from 'swiper';


export default {
  name: 'project-navigation',
  
  data() {
    return {
      leftArrowDisabled: false,
      rightArrowDisabled: false,
    };
  },

  computed: {
    ...mapGetters(['numberOfProjects']),
    ...mapState({
      category: state => state.projects.projectsCategory,
    }),
  },

  methods: {
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

    // set true or false
    setLeftArrowState(status) {
      this.leftArrowDisabled = status;
    },

    setRightArrowState(status) {
      this.rightArrowDisabled = status;
    },

    // disable arrows if limit
    disableArrowsByBoundaries(index) {
      // to disable left arrow
      if (index === 0) {
        this.setLeftArrowState(true);
      } else {
        this.setLeftArrowState(false);
      };

      // to disable right arrow 
      if (index === this.numberOfProjects - 1) {
        this.setRightArrowState(true);
      } else {
        this.setRightArrowState(false);
      };
    },

    //  create carousel and navigation for every project
    // of the current categroy 
    createProjectsCarousel() {
      const self = this;
      const carousel = new Swiper('.swiper-container', {
        // no touch swiping
        allowTouchMove: false,
      });
      let index = carousel.activeIndex;
      console.log(index);
      self.disableArrowsByBoundaries(index);
      // carousel.activeIndex = 0;
      const prevArrow = document.querySelector('.leftControlArrow');
      const nextArrow = document.querySelector('.rightControlArrow');
      prevArrow.addEventListener('click', () => {
        carousel.slidePrev();
        let newSlideIndex = carousel.activeIndex;
        self.disableArrowsByBoundaries(newSlideIndex);
        console.log(index);
      });
      nextArrow.addEventListener('click', function() {
        carousel.slideNext();
        let newSlideIndex = carousel.activeIndex;
        self.disableArrowsByBoundaries(newSlideIndex);
      });
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

