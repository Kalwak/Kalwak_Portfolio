<!--
  BLOG VIEW
  STRUCTURE OF THIS SECTION
-->
<template>
  <div class="col-12">
    <div class="blog-section">
      <h2 class="blog-section__title">Bienvenido a nuestro blog</h2>
      <div class="blog-brand">
        <img src="@/assets/images/logo-second-style.png" alt="Kalwak logo" title="Kalwak logo" class="blog-brand__image" />
      </div>
      <div class="blog-categories">
        <span
          class="blog-category__item"
          v-for="(category, index) in categories"
          :key="index">
            {{ category }}
          </span>
      </div>
      <div class="blog-search-box">
        <div class="search-box__body">
          <label for="searchInput" class="d-none">Busque aqui</label>
          <input type="search" class="search-box__input" id="searchInput" v-model="search.searchText" placeholder="Busque aqui" />
          <span class="search-box__icon icon-search" title="Buscar"></span>
        </div>
      </div>
      <div class="blog-results-section">
        <div class="blog-filter-options">
          <select-filter :options="years" label="Año"  :default-option="2019" @getOption="search.filter.year = $event" />
          <select-filter :options="months" label="Mes" default-option="Enero" @getOption="search.filter.month = $event" />
        </div>
        <div class="inner-wrapper">
          <posts-cards-slider />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Blog view, gives a header where search box and category list is given and
// body where posts-cards and filter options are displayed
import SelectFilter from '../components/sub-layout/select-filter.vue';
import PostsCardsSlider from '../components/sub-layout/posts-cards-slider.vue';


// @vuese
export default {
  name: 'blog',
  data() {
    return {
      search: {
        searchText: '',
        filter: {
          year: '',
          month: '',
        },
      },
      years: [],
      months: [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre'
      ],
      categories: [
        'Desarrollo',
        'Redes Sociales',
        'Startup',
        'Seguridad',
        'Diseño grafico'
      ],
    };
  },

  components: {
    SelectFilter,
    PostsCardsSlider
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
  },

  created() {
    this.years = this.getRangeOfNumbers(2019, 2030);
  },
}
</script>