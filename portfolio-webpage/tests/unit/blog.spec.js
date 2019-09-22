import Blog from '@/views/Blog.vue';
import BlogCardsList from '@/views/sub-views/BlogCardsList.vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import { createLocalVue, shallowMount, mount } from '@vue/test-utils';


describe('Blog', () => {
  // local vue
  const localVue = createLocalVue();
  localVue.use(Vuex);
  localVue.use(VueRouter);
  // store 
  const store = new Vuex.Store({
    state: {
      search: {
        searchText: '',
        filter: {
          year: '',
          month: '',
        },
      },
      onSearching: false,
    },
    mutations: {
      // blog list related
      setSearchText: (state, text) => state.search.searchText = text,
      setSearchYear: (state, year) => state.search.filter.year = year,
      setSearchMonth: (state, month) => state.search.filter.month = month,
      setOnSearching: (state, status) => state.onSearching = status, 
    },
  });
  // router
  const router = new VueRouter({
    routes: [
      {
        path: ':category/page/:number',
        name: 'blog list',
        component: BlogCardsList,
      }
    ],
  });

  // data
  it('should have data function and it should return an object', () => {
    expect(typeof Blog.data).toBe('function');
    expect(typeof Blog.data()).toBe('object');
  });

  // lifecycles
  it('should have a created lifecycle hook', () => {
    expect(typeof Blog.created).toBe('function');
  });

  it('when instance is on created lifecycle, BlogCardsList view should exist', () => {
    const wrapper = shallowMount(Blog, { store, localVue, router });
    expect(wrapper.exists(BlogCardsList)).toBe(true);
  });

  // computed
  it('should have computed object', () => {
    expect(typeof Blog.computed).toBe('object');
  });

  // methods 
  it('should have have a method called getRangeOfNumber which accepts a min and limit parameter, should return an array with number from min to limit', () => {
    let min = 1, limit = 6;
    let output = [1, 2, 3, 4, 5, 6];
    expect(Blog.methods.getRangeOfNumbers(min, limit)).toEqual(output);
  });

  it('should have a method called setSearchText which is a handler for @input event and it gets the value from event.target.value and sets the value to store.state.search.searchText through setSearchText mutation', () => {
    const wrapper = mount(Blog, { store, localVue, router });
    let searchInput = wrapper.find('input[id=searchInput]');
    searchInput.setValue('my text');
    expect(wrapper.vm.$store.state.search.searchText).toBe('my text');
    expect(searchInput.element.value).toBe('my text');
  });

  it('should have a method called changeCategory which recieves a category and pushes it to $route.params.category of the BlogCardsList component view', () => {
    const wrapper = mount(Blog, { store, localVue, router });
    wrapper.vm.changeCategory('category');
    expect(wrapper.vm.$route.path).toBe('category/page/1');
    expect(wrapper.vm.$route.params.category).toBe('category');

    // go through every category item, and trigger its @click event and check if the category matches with the $route.params & $route.path
    let categoriesElements = wrapper.findAll('.blog-category__item');
    let numberOfElements = categoriesElements.length;
    for (let i = 0; i < numberOfElements; i++) {
      let categoryElement = categoriesElements.at(i);
      let esCategory = categoryElement.text();
      let foundCategory = wrapper.vm.$data.categories.find( categoryOpt => categoryOpt.es === esCategory);
      let enCategory = foundCategory.en;
      categoryElement.trigger('click');
      expect(wrapper.vm.$route.path).toBe(`${enCategory}/page/1`);
      expect(wrapper.vm.$route.params.category).toBe(enCategory);
    };
  });

  // store
  it('should call $store.setsetSearchYear when an option is clicked', () => { // filter-option:first-child for years list
    const wrapper = mount(Blog, { store, localVue, router });
    let optionFilter = wrapper.find('.filter-option:first-child');
    
    // when created, getOption custom event should emit the defaultOptin as its payload
    expect(optionFilter.emitted().getOption[0][0]).toBe(optionFilter.props().defaultOption + '');

    // when an option is click, getOption custom event is emitted with its value corresponding to options
    let options = optionFilter.find('.options__list').findAll('.option');
    for (let i = 0; i < options.length; i++) {
      let option = options.at(i);
      let optionValue = optionFilter.props().options[i] + '';
      option.trigger('click');
      expect(wrapper.vm.$store.state.search.filter.year).toBe(optionValue);
    };
  });

  it('should call $store.setsetSearchMonth when an option is clicked', () => { // filter-option:last-child for month list
    const wrapper = mount(Blog, { store, localVue, router });
    let optionFilter = wrapper.find('.filter-option:last-child');
    
    // when created, getOption custom event should emit the defaultOptin as its payload
    expect(optionFilter.emitted().getOption[0][0]).toBe(optionFilter.props().defaultOption + '');

    // when an option is click, getOption custom event is emitted with its value corresponding to options
    let options = optionFilter.find('.options__list').findAll('.option');
    for (let i = 0; i < options.length; i++) {
      let option = options.at(i);
      let optionValue = optionFilter.props().options[i] + '';
      option.trigger('click');
      expect(wrapper.vm.$store.state.search.filter.month).toBe(optionValue);
    };
  });
});