import SelectFilter from '@/components/sub-layout/select-filter.vue';
import { mount } from '@vue/test-utils';

describe('select-filter', () => {
  const propsData = {
    options: [1, 2, 3],
    defaultOption: 1,
    label: 'Numbers',
  };

  // props
  it('should get the right props', () => {
    const wrapper = mount(SelectFilter, {
      propsData: { ...propsData }
    });

    const props = wrapper.props();
    expect(props).toEqual(propsData);
  });


  // methods
  it('setOption should set its option parameter to data selectedOption', () => {
    const wrapper = mount(SelectFilter, {
      propsData: { ...propsData }
    });

    wrapper.vm.setOption(1);
    expect(wrapper.vm.$data.selectedOption).toBe(1);
  });

  it('setLabelHoveredStatus should set its parameter to data labelHovered', () => {
    const wrapper = mount(SelectFilter, {
      propsData: { ...propsData }
    });
    wrapper.vm.setLabelHoveredStatus(true);
    expect(wrapper.vm.$data.labelHovered).toBe(true);
  });


  // events
  it('when created, should call setOption method and defaulOption prop as its argument', () => {
    const wrapper = mount(SelectFilter, {
      propsData: { ...propsData }
    });

    expect(wrapper.vm.$data.selectedOption).toBe(wrapper.props().defaultOption);
  });


  // render
  it('should render label props', () => {
    const wrapper = mount(SelectFilter, {
      propsData: { ...propsData }
    });

    const labelElement = wrapper.find('.label');
    expect(labelElement.text()).toEqual(wrapper.props().label);
  });
})