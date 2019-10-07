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
          >
            <router-link :to="getPath(category.en)">{{ category.es }}</router-link>
        </span>
      </div>
      <div class="blog-search-box" :class="{ 'd-none': onSearching }">
        <div class="search-box__body">
          <label for="searchInput" class="d-none">Busque aqui</label>
          <input type="search" class="search-box__input" id="searchInput" v-model="searchText" placeholder="Busque aqui" />
          <span class="search-box__icon icon-search" title="Buscar" @click="setSearchText"></span>
        </div>
      </div>
      <div class="blog-results-section">
        <div class="blog-filter-options" :class="{ 'd-none': onSearching }">
          <select-filter label="Año" default-option="todos" :options="years" @getOption="getYear" />
          <select-filter label="Mes" default-option="todos" :options="months" @getOption="getMonth" />
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
import { mapState } from 'vuex';
import SelectFilter from '../components/sub-layout/select-filter.vue';

// @vuese
export default {
  name: 'blog',
  data() {
    return {
      categories: [
        { es: 'todas', en: 'all' },
        { es: 'desarrollo', en: 'development' },
        { es: 'redes sociales', en: 'social' },
        { es: 'startup', en: 'startup' },
        { es: 'seguridad', en: 'security' },
        { es: 'diseño grafico', en: 'design' },
      ],
      searchText: '',
      years: ['todos', 2019, 2020],
      months: ['todos', 'Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'],
    };
  },

  computed: {
    ...mapState({
      onSearching: state => state.onSearching,
    }),
  },

  components: {
    SelectFilter,
  },

  methods: {
    // @vuese
    // handles @input event for search input 
    setSearchText() {
      let text = this.searchText;
      this.$log.debug(text);
      this.$store.commit('setSearchText', text);
    },

    // @vuese
    // get and set filter year
    // handler for @getOption custom event in the select-filter component
    // @arg year represents the year emitted by the select-filer
    getYear(year) {
      year = year === 'todos' ? 'all' : year;
      this.$log.debug(year);
      this.$store.commit('setYear', year);
    },
  
    // @vuese
    // get and set filter month
    // handler for @getOption custom event in the select-filter component
    // @arg month represents the month emitted by the select-filer
    getMonth(month) {
      month = month === 'todos' ? 'all' : month;
      this.$log.debug(month);
      this.$store.commit('setMonth', month);
    },

    // @vuese
    // format a new string with the category string
    // @arg category, representing blog category
    getPath(category) {
      this.$log.debug(category);
      let path = `/blog/${category}/page/1`;
      this.$log.debug(path);
      return path;
    },
  },
}
</script>