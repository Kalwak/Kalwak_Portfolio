import PageHeader from '@/components/layout/page-header.vue';
// import Vue from 'vue';


// describe, here goes the title for this testing suite
describe('page-header.vue', () => {
  it('sets the correct default data', () => {
    
    // data property should be a function
    expect(typeof PageHeader.data).toBe('function');

    // activeMenu default set to false
    const defaultData = PageHeader.data();
    expect(defaultData.activatedMenu).toBe(false);
  });
});