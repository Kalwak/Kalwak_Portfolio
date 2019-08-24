import ProjectNavigation from '@/components/sub-layout/project-navigation.vue';
// import Vue from 'vue';
import Vuex from 'vuex';
import { shallowMount, createLocalVue } from '@vue/test-utils';


const localVue = createLocalVue();
localVue.use(Vuex);

const store = new Vuex.Store({
  state: {
    projects: {
      projectsCategory: '',
    },
  },
  getters: {
    numberOfProjects() {
      return 10;
    },
  },
});

// function getRenderedText(Component, propsData) {
//   const Constructor = Vue.extend(Component);
//   const vm = new Constructor({ propsData: propsData }).$mount();
//   return vm;
// };

describe('project-nagivation', () => {
  const data = ProjectNavigation.data();
  const wrapper = shallowMount(ProjectNavigation, { store, localVue });

  it('should have leftArrowDisabled set to false', () => {
    expect(data.leftArrowDisabled).toEqual(false);
  });

  it('should set leftArrowDisabled true when setLeftArrowState is called with true argument', () => {
    wrapper.vm.setLeftArrowState(true);
    expect(wrapper.vm.leftArrowDisabled).toEqual(true);
  });

  it('should set leftArrowDisabled when current slide index equals 0', () => {
    wrapper.vm.disableArrowsByBoundaries(0);
    expect(wrapper.vm.leftArrowDisabled).toEqual(true);
  });


  it('should have rightArrowDisabled set to false', () => {
    expect(data.rightArrowDisabled).toEqual(false);
  });

  it('should set rightArrowDisabled true when setRightArrowState is called with true argument', () => {
    wrapper.vm.setRightArrowState(true);
    expect(wrapper.vm.rightArrowDisabled).toEqual(true);
  });

  it('should set rightArrowDisabled when current slide index equals the total number of slides - 1', () => {
    wrapper.vm.disableArrowsByBoundaries(9);
    expect(wrapper.vm.rightArrowDisabled).toEqual(true);
  });
  
  it('should have a created hook', () => {
    expect(typeof ProjectNavigation.created).toBe('function');
  });

  it('should have a mounted hook', () => {
    expect(typeof ProjectNavigation.mounted).toBe('function');
  });

});