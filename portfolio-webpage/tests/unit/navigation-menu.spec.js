import NavigationMenu from '../../src/components/sub-layout/navigation-menu.vue';
import Vue from 'vue';


describe('navigation-menu', () => {
  it('should have computed property serviceCategory', () => {
    const computedProps = Object.keys(NavigationMenu.computed);
    expect(computedProps.find(prop => prop === 'serviceCategory').length > 0).toBe(true);
  });

  it('should have computed property projectCategory', () => {
    const computedProps = Object.keys(NavigationMenu.computed);
    expect(computedProps.find(prop => prop === 'projectCategory').length > 0).toBe(true);
  });

  it('should have computed property currentPath', () => {
    const computedProps = Object.keys(NavigationMenu.computed);
    expect(computedProps.find(prop => prop === 'currentPath').length > 0).toBe(true);
  });
});