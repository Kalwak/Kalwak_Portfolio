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
        title: 'Kalwak | Proyectos anteriores'
      },
      children: [
        {
          path: 'category/:category',
          component: () => import('./views/sub-views/ProjectCategory.vue'),
        }
      ]
    },
    {
      path: '/about-us',
      name: 'about-us',
      component: () => import('./views/AboutUs.vue'),
      meta: {
        title: 'Kalwak | Acerca de nosotros' 
      }
    },
  ]
});
// component: () => import(/* webpackChunkName: "about" */ './views/Component.vue')