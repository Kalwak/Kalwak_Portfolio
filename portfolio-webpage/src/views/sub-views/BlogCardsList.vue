<!--
  // STRUCTURE OF THIS VIEW
  DIV // CLASSES: BLOG-POSTS-CARDS-SLIDER // CONTAINER FOR SPINNER LOADEING ICON, POSTS CARDS AND PAGINATION
    DIV // CLASSES: SPINNER // SPINNER FOR LOADING ANIMATION
    DIV // CLASSES: POSTS-CARDS-CONTAINER ANIMATED FADEIN // CONTAINER FOR POST-CARD COMPONENT
      POST-CARD COMPONENT
    DIV // CLASSES: POSTS-CARDS__PAGINATION // CONTAINER FOR PAGINATION BUTTONS
      SPAN // CLASSES: PAGINATION__BUTTON ICON-LEFT-ARROW ARROW // PAGINATION ARROW
      SPAN // CLASSES: PAGINATION__BUTTON // PAGINATION BUTTON
      SPAN // CLASSES: PAGINATION__BUTTON ICON-RIGHT-ARROW ARROW // PAGINATION ARROW
-->
<template>
  <div class="blog-posts-cards-slider">
    <div class="spinner" v-if="onSearching">
      <div class="rect1"></div>
      <div class="rect2"></div>
      <div class="rect3"></div>
      <div class="rect4"></div>
      <div class="rect5"></div>
    </div>
    <div class="posts-cards__container animated fadeIn" v-if="!onSearching">
      <post-card
        v-for="(card, index) in blogList"
        :key="index"
        :post="card"
        />
    </div>
    <div 
      class="alert alert-danger text-center d-none" 
      style="width: 80%; max-width: 600px; margin: 50px auto; font-size: 1.5em;" 
      :class="{ 'd-block': noResults }">
        No hay resultados
    </div>
    <div class="posts-cards__pagination" v-if="!onSearching && blogList.length > 0">
      <span class="pagination__button icon-left-arrow arrow" @click="navPages('prev')"></span>
      <template v-for="pageNumber in pageNumbers">
        <span 
          class="pagination__button"
          :class="{ 'currentPage': currentPageNumber === pageNumber }"
          :key="pageNumber">
            <router-link :to="`/blog/${category}/page/${pageNumber}`">{{ pageNumber }}</router-link>
          </span>
      </template>
      <span class="pagination__button icon-right-arrow arrow" @click="navPages('next')"></span>
    </div>
  </div>
</template>

<script>
// posts-cards-slider, use for showing posts-cards based on search category and filter restuls
// and also to provide a pagination
import PostCard from '../../components/sub-layout/post-card';
import { formatMonth } from '../../utils/utils';
import axios from 'axios';
import swal from 'sweetalert';
import { mapState } from 'vuex';


// @vuese
export default {
  name: 'blog-carsds-list',

  data() {
    return {
      blogList: [],
      numberOfPages: 0,
      noResults: false,
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

    currentPageNumber() {
      return Number(this.$route.params.number);
    },

    category() {
      return this.$route.params.category;
    },

    ...mapState({
      onSearching: state => state.onSearching,
      searchText: state => state.searchText,
      filter: state => state.filter
    }),

    blogUrl() {
      let tag = this.category === 'all' ? '' : `&tag=${this.category}`;
      let page = `page=${this.currentPageNumber}`;
      let { year, month } = this.filter;
      year = year === 'all' ? '' : `&year=${year}`;
      month = month === 'all' ? '' : `&month=${formatMonth(month)}`;
      let keyword = this.searchText;
      let baseUrl = process.env.VUE_APP_API_ENDPOINT;
      return `${baseUrl}/api/blog-list/?${page}${tag}${year}${month}`;
    }
  },

  components: {
    PostCard,
  },
  
  methods: {

    // @vuese
    // used to add or remove a page level, this is used in the pagination arrows
    // @arg toWhere must be a string which value is next or prev, if something different
    // is given, returns false
    navPages(toWhere) {
      let pageNumber = this.currentPageNumber;
      let limitNumber = this.numberOfPages;
      let category = this.category;
      this.$log.debug(toWhere);
      this.$log.debug('pageNumber:', pageNumber, 'limitNumber:', limitNumber)

      if (toWhere === 'next' && pageNumber < limitNumber) {
        pageNumber += 1
        this.$router.push(`/blog/${category}/page/${pageNumber}`);
      };
      if (toWhere === 'prev' && pageNumber > 1) {
        pageNumber -= 1
        this.$router.push(`/blog/${category}/page/${pageNumber}`);
      } else return false;
    },

    // @vuese
    // used to get and set the number of pages based on the number of 
    // posts given by the backend response
    // @arg number, number of item in the blog list
    setNumberOfPages(number) {
      let numberOfPages =  Math.ceil(number / 6);
      this.numberOfPages = numberOfPages;
    },

    // @vuese
    // fetch blog list based on category, year, month and page
    getBlogList() {
      let url = this.blogUrl;
      this.blogList = [];
      this.noResults = false;
      this.$store.commit('setOnSearching', true);
      axios.get(url)
        .then( response => {
          this.$log.debug(response);
          let results = response.data.results;
          this.blogList = results;
          this.setNumberOfPages(response.data.count);
          this.checkForNoResults();
        })
        .catch( errors => {
          let response = errors.response;
          this.$log.error(errors);
          this.$log.debug(response);
          if (!response && !navigator.onLine) {
            swal({
              title: 'Notificación',
              icon: 'error',
              text: 'Sin conexión a internet'
            })
          } else if (!response) {
            swal({
              title: 'Notificación',
              icon: 'warning',
              text: 'Hubo un error, intente de nuevo'
            })

          } else if (response.status === 404) {
            this.checkForNoResults();
          }
        })
        .finally(() => {
          this.$store.commit('setOnSearching', false);
        });
    },

    // @vuese
    // toggle no results error if no results from request
    checkForNoResults() {
      if (this.blogList.length < 1) this.noResults = true;
      else this.noResults = false;
    },

    // @vuese
    // sets default page number if currentPageNumber is undefined
    setDefaultPageNumber() {
      let pageNumber = this.currentPageNumber;
      if (!pageNumber) {
        this.$router.push({ path: `/blog/${this.category}/page/1` });
      };
    }
  },

  created() {
    this.setDefaultPageNumber();
    this.getBlogList();
  },

  watch: {
    category(newCategory, oldCategory) {
      this.setDefaultPageNumber();
    },

    blogUrl() {
      console.log('blog-url changed');
      this.getBlogList();
    }
  }
}
</script>