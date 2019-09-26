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
    <div class="posts-cards__pagination" v-if="numberOfPages > 0 && !onSearching">
      <span class="pagination__button icon-left-arrow arrow" @click="navPages('prev')"></span>
      <template v-for="pageNumber in pageNumbers">
        <span 
          class="pagination__button"
          :class="{ 'currentPage': currentPageNumber === pageNumber }"
          :key="pageNumber">
            <router-link :to="{ name: 'blog list', params: { number: pageNumber }}">{{ pageNumber }}</router-link>
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
import axios from 'axios';
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

    // base backend url endpoint for getting post, with axios
    // I'll add the page query string
    postUrl() {
      let { filter, searchText } = this.search;
      let page = `page=${ this.currentPageNumber}&`;
      let category = this.currentCategory === 'all' ? '' : `tag=${this.currentCategory}&`;
      let year = filter.year ? `year=${filter.year}&` : '';
      let month = filter.month ? `month=${this.formatMonth(filter.month)}` : '';
      return `${process.env.VUE_APP_API_ENDPOINT}/api/blog-list?${page}${category}${year}${month}`;
    },

    currentPageNumber() {
      return Number(this.$route.params.number);
    },

    currentCategory() {
      return this.$route.params.category;
    },

    ...mapState({
      search: state => state.search,
      onSearching: state => state.onSearching,
    }),
  },

  components: {
    PostCard
  },
  
  methods: {

    // @vuese
    // used to add or remove a page level, this is used in the pagination arrows
    // @arg toWhere must be a string which value is next or prev, if something different
    // is given, returns false
    navPages(toWhere) {
      let pageNumber = this.currentPageNumber;
      let limitNumber = this.numberOfPages;
      this.$log.debug(toWhere);

      if (toWhere === 'next' && pageNumber < limitNumber) {
        this.$router.push({ name: 'blog list', params: { number: Number(pageNumber) + 1, category: this.currentCategory }});
      };
      if (toWhere === 'prev' && pageNumber > 1) {
        this.$router.push({ name: 'blog list', params: { number: Number(pageNumber) - 1, category: this.currentCategory }});
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
    // used in the created stage of the component
    // so if the :number router is anything else but not a number
    // user will be redirected to 404 page
    checkRouteNumber() {
      let pageNumber = this.$route.params.number;
      if (!Number(pageNumber)) {
        this.$router.push({ name: 'not found' });
      };
    },

    // @vuese
    // format month to have zero leading prefix if needed
    // @arg month, special string like Ene for Enero ~ Dic for Diciembre
    formatMonth(month) {
      let months = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"];
      if (typeof month !== 'string' || !month.length) return false;
      month = months.indexOf(month) + 1;
      month = month.toString().length === 1 ? '0' + month : month;
      return month;
    },

    // @vuese
    // fetch blog list based on category, year, month and page
    getBlogList() {
      let url = this.postUrl;
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
          this.$log.error(errors);
          this.$router.push({ name: 'not found' });
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
  },

  created() {
    this.checkRouteNumber();
  },

  mounted() {
    this.getBlogList();
  },

  watch: {
    postUrl() {
      this.getBlogList();
    },
  },
}
</script>