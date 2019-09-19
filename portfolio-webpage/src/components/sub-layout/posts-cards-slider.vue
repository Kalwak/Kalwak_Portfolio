<template>
  <div class="blog-posts-cards-slider">
    <div class="posts-cards__container">
    </div>
    <div class="posts-cards__pagination">
      <span class="pagination__button icon-left-arrow arrow" @click="navPages('prev')"></span>
      <template v-for="pageNumber in pageNumbers">
        <span 
          class="pagination__button"
          :class="{ 'currentPage': currentPageNumber === pageNumber }"
          @click="setPageNumber(pageNumber)"
          :key="pageNumber">{{ pageNumber }}</span>
      </template>
      <span class="pagination__button icon-right-arrow arrow" @click="navPages('next')"></span>
    </div>
  </div>
</template>

<script>
// posts-cards-slider, use for showing posts-cards based on search category and filter restuls
// and also to provide a pagination
import PostCard from './post-card';


// @vuese
export default {
  name: 'blog-posts-cards',

  data() {
    return {
      postsCardsInfo: [],
      numberOfPages: 10,
      currentPageNumber: 1,
    };
  },

  computed: {
    // returns an array with the page numbers
    pageNumbers() {
      let limit = this.numberOfPages;
      let pageNumber = 1;
      let pageNumbers = [];
      for (pageNumber; pageNumber <= limit; pageNumber++) {
        pageNumbers.push(pageNumber);
      };

      return pageNumbers;

    },
  },

  props: {
    // used to query the posts information, related to category, keyword used in search box
    // and filter with year and month
    search: {
      type: Object,
      required: true,
    }
  },

  components: {
    PostCard
  },
  
  methods: {
    // @vuese 
    // set the currentPageNumber to the given argument value
    // @arg number is the value given to currentPageNumber
    setPageNumber(number) {
      this.$log.debug(number);
      this.currentPageNumber = number;
    },

    // @vuese
    navPages(toWhere) {
      let pageNumber = this.currentPageNumber;
      let limitNumber = this.numberOfPages;

      if (toWhere === 'next' && pageNumber < limitNumber) {
        this.currentPageNumber = pageNumber + 1;
      };
      if (toWhere === 'prev' && pageNumber > 1) {
        this.currentPageNumber = pageNumber - 1;
      };
    },
  },
}
</script>