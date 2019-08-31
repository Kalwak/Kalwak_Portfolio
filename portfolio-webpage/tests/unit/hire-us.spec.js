import HireUs from '../../src/views/HireUs.vue';
import { shallowMount } from '@vue/test-utils';


describe('hire-us', () => {
  const wrapper = shallowMount(HireUs);

  // data function
  it('you have a data function and that data function should return an object', () => {
    expect(typeof HireUs.data).toBe('function');
    expect(typeof HireUs.data()).toBe('object');
  });

  // computed properties
  it('buttonDisabledByInputs computed property should return true if required fields are empty/undefined', () => {
    wrapper.setData({
      service_request: {
        first_name: '',
        last_name: '',
        email: '',
        description: '',
        telephone: '',
        files: [],
        services: [],
      },
    });

    expect(wrapper.vm.buttonDisabledByInputs).toBe(true);

    // now with undefine values instead of empty strings
    wrapper.setData({
      service_request: {
        first_name: undefined,
        last_name: undefined,
        email: undefined,
        description: undefined,
        telephone: undefined,
        files: [],
        services: [],
      },
    });

    expect(wrapper.vm.buttonDisabledByInputs).toBe(true);
  });

  it('buttonDisabledByInputs computed property should return true if required fields are not empty/undefined', () => {
    wrapper.setData({
      service_request: {
        first_name: 'John',
        last_name: 'Doe',
        email: 'johndoe@email.com',
        description: 'Hello Kalwak',
        telephone: '+123456789',
        files: [],
        services: [],
      },
    });

    expect(wrapper.vm.buttonDisabledByInputs).toBe(false);
  });

  it('buttonDisabled should return true if buttonDisabledByInputs is true, else if buttonDisabledByInputs is false returns false', () => {
    wrapper.setData({
      service_request: {
        first_name: '',
        last_name: '',
        email: '',
        description: '',
        telephone: '',
        files: [],
        services: [],
      },
    });

    expect(wrapper.vm.buttonDisabled).toBe(true);

    wrapper.setData({
      service_request: {
        first_name: 'John',
        last_name: 'Doe',
        email: 'johndoe@email.com',
        description: 'Hello Kalwak',
        telephone: '+123456789',
        files: [],
        services: [],
      },
    });

    expect(wrapper.vm.buttonDisabled).toBe(false);
  });

  // methods
  it('should have a method called format_name which has two arguments and those arguments are concatenated and set together to the service_request name property', () => {
    wrapper.setData({
      service_request: {},
    });

    let firstName = 'John';
    let lastName = 'Doe';

    let fullName = `${firstName} ${lastName}`;

    wrapper.vm.format_name(firstName, lastName);
    expect(wrapper.vm.$data.service_request.name).toEqual(fullName);
  });
});