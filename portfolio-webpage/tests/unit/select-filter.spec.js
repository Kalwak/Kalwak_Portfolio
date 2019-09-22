import SelectFilter from '@/components/sub-layout/select-filter.vue';
import { mount } from '@vue/test-utils';

describe('select-filter', () => {
  const options = [1, 2, 3, 4];
  const defaultOption = '1';

  it('when instance is created it should set defaultOption to selectedOption using setOption method', () => {
    const wrapper = mount(SelectFilter, {
      propsData: {
        options,
        defaultOption,
      },
    });
    expect(wrapper.vm.$data.selectedOption).toBe(wrapper.props().defaultOption);
  });

  it('when created setOption method is called a custom event getOption is emitted and its payload is setOption passed argument which is defaultOption', () => {
    const wrapper = mount(SelectFilter, {
      propsData: {
        options,
        defaultOption,
      },
    });

    let emittedValue = wrapper.emitted().getOption[0][0];
    expect(emittedValue).toBe(wrapper.props().defaultOption);
  });

  it('filter-option label should have the same text as selected option', () => {
    const wrapper = mount(SelectFilter, {
      propsData: {
        options,
        defaultOption,
      },
    });

    expect(wrapper.find('.filter-option .label').text()).toBe(wrapper.vm.$data.selectedOption);
  });

  it('setOption method should set its argument to data selectedOption and also emit a custom event with its argument as the payload', () => {
    const wrapper = mount(SelectFilter, {
      propsData: {
        options,
        defaultOption,
      },
    });

    wrapper.vm.setOption('option');
    let emittedValue = wrapper.emitted().getOption[1][0];
    expect(wrapper.vm.$data.selectedOption).toBe('option');
    expect(emittedValue).toBe('option');
  });

  it('when mouse is over or if mouse is out of filter-option label, labelHovered property should toggle between true and false', () => {
    const wrapper = mount(SelectFilter, {
      propsData: {
        options,
        defaultOption,
      },
    });

    const label = wrapper.find('.filter-option .label');
    // if not hovering labelHovered should be false
    expect(wrapper.vm.$data.labelHovered).toBe(false);

    // if hovering labelHovered should be true;
    label.trigger('mouseover');
    expect(wrapper.vm.$data.labelHovered).toBe(true);
  }); 
});