import HireUs from '../../src/views/HireUs.vue';
import {createLocalVue, shallowMount} from '@vue/test-utils';
import {render} from '@vue/server-test-utils';


describe('hire-us', () => {
    const localVue = createLocalVue();
    localVue.use(require('vue-cookies'));
    let wrapper = shallowMount(HireUs, localVue);


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


    it('Check if csrf hidden input is inserted if method submit is called', async () => {
        global.$cookies = {
            get: (val) => "aaa"
        };
        wrapper = await render(HireUs);


        expect(wrapper.html()).toContain('<input id="csrftoken" type="hidden" name="csrfmiddlewaretoken" value="aaa">')
    });

    it('Checking if the errors are working fine', () => {
        let wrapper = shallowMount(HireUs, localVue);

        expect(wrapper.vm.errors.length).toBe(0);


        delete global.window.location;

        global.window = Object.create(window);
        // Doing this since the errors are gathered from the url query
        const search_query = "?errors=%7B%27telephone%27:%20[%27Telephone%20format%20is%20incorrect%27]%7D";
        const url = "http://localhost/hire-us/" + search_query;
        Object.defineProperty(window, "location", {
            value: {
                href: url,
                search: search_query
            },
            writable: true
        });

        wrapper = shallowMount(HireUs, localVue);

        expect(wrapper.vm.errors.length).toBe(1);

    })
});