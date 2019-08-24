import PageFooter from '../../src/components/layout/page-footer.vue';
import { shallowMount } from '@vue/test-utils';


const $route = {
  path: '/some/path'
}

describe('page-footer', () => {
  const wrapper = shallowMount(PageFooter, {
    mocks: {
      $route,
    },
  });

  // buttonDisabledByInputs expects to be true if inputs like email, name or message are empty
  it('should have buttonDisabledByInputs set to true if required inputs are empty', () => {
    wrapper.setData({
      email: {
        name: '',
        address: '',
        message: '',
      },
    });
    expect(wrapper.vm.buttonDisabledByInputs).toBe(true);
  });

  // buttonDisabledByInputs expects to be false if inputs like email, name or message are not empty
  it('should have buttonDisabledByInputs set to false if required inputs are not empty', () => {
    wrapper.setData({
      email: {
        name: 'John Doe',
        address: 'johndoe@email.com',
        message: 'Hello, i\'m John Doe',
      },
    });
    expect(wrapper.vm.buttonDisabledByInputs).toBe(false);
  });

  // buttonDisabledByProcess expects to be false if onSending property of email object is set to false
  it('should have buttonDisabledByProcess set to false if onSending is set to false', () => {
    wrapper.setData({
      email: {
        onSending: false,
      },
    });
    expect(wrapper.vm.buttonDisabledByProcess).toBe(false);
  });

  // buttonDisabledByProcess expects to be true if onSending property of email object is set to true
  it('should have buttonDisabledByProcess set to true if onSending is set to true', () => {
    wrapper.setData({
      email: {
        onSending: true,
      },
    });
    expect(wrapper.vm.buttonDisabledByProcess).toBe(true);
  });

  // buttonDisabled expects to be true if buttonDisabledByProcess is true or buttonDisabledByInputs is true
  it('should have buttonDisabled set to true if buttonDisabledByProcess is true or buttonDisabledByInputs is true', () => {
    // as buttonDisabledByProcess depends in onSending property, this time onSending is set to true
    wrapper.setData({
      email: {
        onSending: true,
        name: '',
        address: '',
        message: '',
      },
    });

    // as onSending is set to true, buttonDisabledByProcess is true, so either buttonDisabledByProcess or buttonDisabledByInputs is true... 
    // buttonDisabled should be true
    expect(wrapper.vm.buttonDisabled).toBe(true);

      // not this time, will be oposite
    wrapper.setData({
      email: {
        onSending: false,
        name: '',
        address: '',
        message: '',
      },
    });

    // should be true, because required inputs are empty ... 
    expect(wrapper.vm.buttonDisabled).toBe(true);
  });

  it('should have emailInfo computed property, and should be an object', () => {
    wrapper.vm.data = ({
      email: '',
      name: '',
      message: '',
      phoneNumber: '',
    });

    expect(typeof wrapper.vm.emailInfo).toBe('object');
  });

  // methods
  it('should have a method called checkFields and should be a function', () => {
    expect(typeof wrapper.vm.checkFields).toBe('function');

    // also should return an object with prperty valid set to false if fields passed as arguments are empty
    expect(wrapper.vm.checkFields({ name: '', address: '', message: '' }).valid).toBe(false);

    // if at least one field is empty, should also return false
    expect(wrapper.vm.checkFields({ name: 'John Doe', address: '', message: 'Hello' }).valid).toBe(false);

    // should return true if all fields are not empty
    expect(wrapper.vm.checkFields({ name: 'John Doe', address: 'johndoe@email.com', message: 'Hello' }).valid).toBe(true);
  });

  it('should have a method called clearInputs and should clear/set to empty string email fields', () => {
    const data = Object.values(wrapper.vm.data);

    wrapper.vm.clearInputs();
    data.forEach( value => {
      expect(value).toBe('');
    });
  });
});