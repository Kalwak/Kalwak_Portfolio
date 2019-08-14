import CategoryList from '../../src/components/sub-layout/category-list.vue';


describe('category-list', () => {
  it('should have a created hook', () => {
    expect(typeof CategoryList.created).toBe('function');
  });

  it('should have a computed hook', () => {
    expect(typeof CategoryList.computed).toBe('object');

    // computed property category should be a function
    expect(typeof CategoryList.computed.category).toBe('function');
  });

  it('should have a watcher on category', () => {
    expect(typeof CategoryList.watch.category).toBe('function');
  });
});