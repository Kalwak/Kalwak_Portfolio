<!--
  BLOG VIEW
  STRUCTURE OF THIS SECTION
    DIV // CLASSES: COL-12 // MAIN CONTAINER FOR VIEW
      DIV // CLASSES: BLOG-SECTION // CONTAINER FOR BLOG SECTION
        H2 // CLASSES: BLOG-SECTION__TITLE // BLOG SECTION TITLE
        DIV // CLASSES: BLOG-BRAND // CONTAINER FOR BRAND LOGO
          IMG // CLASSES: BLOG-BRAND__IMAGE // IMAGE FOR BRAND-LOGO
        DIV // CLASSES: BLOG-CATEGORIES // CONTAINER FOR BLOG CATEGORIES
          SPAN // CLASSES: BLOG-CATEGORY__ITEM // CONTAINER FOR A PARTICULAR CATEGORY
        DIV // CLASSES: BLOG-SEARCH-BOX // CONTAINER FOR A SEARCH BOX
          DIV // CLASSES:SEARCH-BOX__BODY // BODY ELEMENT OF BLOG-SEARCH-BOX
            LABEL // CLASSES: D-NONE // LABEL FOR SEARCH-BOX__INPUT 
            INPUT // CLASSES: SEARCH-BOX__INPUT // INPUT FOR SEARCH-BOX
            SPAN // CLASSES: SEARCH-BOX__ICON ICON-SEARCH // BUTTON FOR SEARCHING
        DIV // CLASSES: BLOG-RESULTS-SECTION // CONTAINER FOR FILTER OPTIONS AND BLOGCARDSLIST VIEW
          DIV // CLASSES: BLOG-FILTER-OPTIONS // CONTAINER FOR THE FILTER OPTIONS
            SELECT-FILTER // COMPONENT TO PROVIDE OPTIONS
          DIV // CLASSES: INNER-WRAPPER // WIDTH LIMITER 
            ROUTER-VIEW // FOR BLOGCARDSLIST RESULTS
-->
<template>
  <div class="col-12">
    <div class="blog-section">
      <h2 class="blog-section__title">Bienvenido a nuestro blog</h2>
      <div class="blog-brand">
        <img src="@/assets/images/logo-second-style.png" alt="Kalwak logo" title="Kalwak logo" class="blog-brand__image" />
      </div>
      <div class="blog-categories" :class="{ 'd-none': onSearching }">
        <span
          class="blog-category__item"
          v-for="(category, index) in categories"
          :key="index"
          :class="{ 'selected-text': category.en === $route.params.category }"
          @click="changeCategory(category.en)">
            {{ category.es }}
          </span>
      </div>
      <div class="blog-search-box" :class="{ 'd-none': onSearching }">
        <div class="search-box__body">
          <label for="searchInput" class="d-none">Busque aqui</label>
          <input type="search" class="search-box__input" id="searchInput" :value="search.searchText" @input="setSearchText" placeholder="Busque aqui" />
          <span class="search-box__icon icon-search" title="Buscar"></span>
        </div>
      </div>
      <div class="blog-results-section">
        <div class="blog-filter-options" :class="{ 'd-none': onSearching }">
          <select-filter :options="years" :default-option="new Date().getFullYear()" @getOption="$store.commit('setSearchYear',$event)" />
          <select-filter :options="months" :default-option="months[new Date().getMonth()]" @getOption="$store.commit('setSearchMonth',$event)" />
        </div>
        <div class="inner-wrapper">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Blog view, gives a header where search box and category list is given and
// body where posts-cards and filter options are displayed
import SelectFilter from '../components/sub-layout/select-filter.vue';
import { mapState } from 'vuex';


// @vuese
export default {
  name: 'blog',
  data() {
    return {
      years: [],
      months: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
      categories: [
        { es: 'todas', en: 'all' },
        { es: 'desarrollo', en: 'development' },
        { es: 'redes sociales', en: 'social' },
        { es: 'startup', en: 'startup' },
        { es: 'seguridad', en: 'security' },
        { es: 'diseño grafico', en: 'design' },
      ],
    };
  },

  computed: {
    ...mapState({
      search: state => state.search,
      onSearching: state => state.onSearching,
    }),
  },

  components: {
    SelectFilter,
  },

  methods: {
    // @vuese
    // used to return an array of number of the given ranges
    // @args min, a int representing the min number of the array
    // @args limit, a int representing the limit number of the array
    // @return numbers, an array of numbers from min..to..limit
    getRangeOfNumbers(min, limit) {
      let numbers = [];
      let number = min;
      for (; number <= limit; number++) {
        numbers.push(number);
      };

      return numbers;
    },
    // @vuese
    // handles @input event for search input 
    // and sets event.target.value to store search.searchText through 
    // setSearchText mutation method
    setSearchText(event) {
      let text = event.target.value;
      this.$store.commit('setSearchText', text);
    },

    // @vuese
    //
    changeCategory(category) {
      this.$router.push({ name: 'blog list', params: { category: category, number: 1 }});
    },
  },

  created() {
    this.years = this.getRangeOfNumbers(2019, 2020);
    // if only /blog route is matched, give a default page and number
    if (this.$route.path === '/blog' || this.$route.path === '/blog/') this.$router.push('/blog/all/page/1');
  },
}
</script>