import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vueSmoothScroll from 'vue2-smooth-scroll';
import axios from 'axios';
import '../node_modules/swiper/dist/js/swiper.min.js';
import './assets/css/main.scss';
import {VueCookies} from 'vue-cookies';

Vue.use(require('vue-cookies'));

Vue.config.productionTip = false;
Vue.use(vueSmoothScroll);
Vue.prototype.$axios = axios;

new Vue({
  router,
  store,
  // render: h => h(App),
  render: createElement => createElement(App),
}).$mount('#app');

window.$ = window.jQuery = require('jquery');
let csrf_cookie = window.$cookies.get('csrftoken');
axios.defaults.headers.common['X-CSRFToken'] = csrf_cookie; // for all requests
