import Vue from 'vue';
import Router from 'vue-router';
Vue.use(Router);


export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
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
      meta: {
        title: 'Wink | trabajos anteriores'
      }
    }
  ]
});

// component: () => import(/* webpackChunkName: "about" */ './views/Component.vue')