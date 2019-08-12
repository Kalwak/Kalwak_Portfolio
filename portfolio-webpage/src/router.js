import Vue from 'vue';
import Router from 'vue-router';
Vue.use(Router);


export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior () {
    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Home.vue'),
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('./views/Projects.vue'),
      children: [
        {
          path: ':category',
          name: 'category',
          component: () => import('./views/sub-views/Category.vue'),
        }
      ]
    },
    {
      path: '/about-us',
      name: 'about-us',
      component: () => import('./views/AboutUs.vue'),
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('./views/Services.vue'),

      children: [
        {
          path: ':service',
          component() {
            return import('./views/sub-views/Service.vue');
          },
        }
      ],
    },
  ]
});
// component: () => import(/* webpackChunkName: "about" */ './views/Component.vue')