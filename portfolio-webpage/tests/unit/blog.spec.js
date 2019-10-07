import Blog from '@/views/Blog.vue';
import BlogCardsList from '@/views/sub-views/BlogCardsList.vue';
import BlogDefault from '@/views/sub-views/BlogDefault.vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import vueLogger from 'vuejs-logger';
import { createLocalVue, shallowMount, mount } from '@vue/test-utils';


describe('blog', () => {

  const localVue = createLocalVue();
  localVue.use(VueRouter);
  localVue.use(Vuex);
  localVue.use(vueLogger);
  // avoid logger messages
  localVue.$log.debug = () => {};
  localVue.$log.error = () => {};


  const data = {
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

  const store = new Vuex.Store({
    state: {
      onSearching: false,
      searchText: '',
      filter: {
        year: '',
        month: '',
      },
    },

    mutations: {
      setSearchText: (state, text) => state.searchText = text,
      setYear: (state, year) => state.filter.year = year,
      setMonth: (state, month) => state.filter.month = month
    }
  });

  const router = new VueRouter({
  });

  // data
  it('should have the current data', () => {
    const wrapper = mount(Blog, {
      localVue,
      router,
      store
    });

    let componentData = wrapper.vm.$data;
    expect(componentData).toEqual(data);
  });


  // computed
  it('store onSearching is set to false by default', () => {
    const wrapper = mount(Blog, {
      localVue,
      router,
      store
    });

    let onSearching = wrapper.vm.onSearching;
    expect(onSearching).toBe(false);
  });

  // methods
  it('setSearchText should take searchText value and set it to store searchText through a mutation', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    let searchText = 'My search text';
    wrapper.vm.$data.searchText = searchText;
    wrapper.vm.setSearchText();
    let searchTextOnStore = wrapper.vm.$store.state.searchText;
    expect(searchTextOnStore).toEqual(searchText);
  });

  it('getYear method should check if its year parameter is equal to the string (todos) and replace it with string (all) else let it as it is, then set the year to store filter.year through a mutation', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    // first check if the value of todos is set as all
    let value = 'todos';
    wrapper.vm.getYear(value);
    let valueOnStore = wrapper.vm.$store.state.filter.year;
    expect(valueOnStore).toBe('all');

    // check for any year
    wrapper.vm.getYear(2019);
    valueOnStore = wrapper.vm.$store.state.filter.year;
    expect(valueOnStore).toBe(2019);
  });

  it('getMonth method should check if its month parameter is equal to the string (todos) and replace it with string (all) else let it as it is, then set the month to store filter.year through a mutation', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    // first check if the value of todos is set as all
    let value = 'todos';
    wrapper.vm.getMonth(value);
    let valueOnStore = wrapper.vm.$store.state.filter.month;
    expect(valueOnStore).toBe('all');

    // check for any year
    wrapper.vm.getMonth('Dec'); // December
    valueOnStore = wrapper.vm.$store.state.filter.month;
    expect(valueOnStore).toBe('Dec');
  });

  it('getPath should return a string with the format /blog/{category}/page/1 where {category} is replaced with its category parameter', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    let formattedText = wrapper.vm.getPath('my-category');
    expect(formattedText).toEqual('/blog/my-category/page/1');
  });

  // events as handlers
  it('as select-filter component is created, it emits a getOption event and getYear method (for the years options) should be called as its handler and set the payload value to store filter.year', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    // the default-option passed to select-filter for years options is -> todos, this value should be the payload when the select-filter emits the getOption when is created
    let defaultValue = 'all';
    // getYear method checks if the parameter is equal to the string 'todos', if it's equal, then replace its value with 'all', so that's why defaultValue is 'all'
    let filterYear = wrapper.vm.$store.state.filter.year;
    expect(filterYear).toBe(defaultValue)
  });

  it('as select-filter component is created, it emits a getOption event and getMonth method (for the months options) should be called as its handler and set the payload value to store filter.month', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    // the default-option passed to select-filter for years options is -> todos, this value should be the payload when the select-filter emits the getOption when is created
    let defaultValue = 'all';
    // getMonth method checks if the parameter is equal to the string 'todos', if it's equal, then replace its value with 'all', so that's why defaultValue is 'all'
    let filterMonth = wrapper.vm.$store.state.filter.month;
    expect(filterMonth).toBe(defaultValue)
  });


  // buttons actions


  // views render
  it('when this component is rendered, should also display a default children view component', () => {
    const wrapper = mount(Blog, {
      localVue,
      router,
      store
    });

    expect(wrapper.exists(BlogDefault)).toBe(true);
  });

  it('should render BlogCardsList view component with this route string -> /blog/{category}/page/{pageNumber}', () => {
    const wrapper = mount(Blog, { localVue, router, store });
    wrapper.vm.$router.push('/blog/all/page/1');
    expect(wrapper.exists(BlogCardsList)).toBe(true);
  });
})