import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import vueLogger from 'vuejs-logger';
import '../node_modules/swiper/dist/js/swiper.min.js';
import './assets/css/main.scss';

Vue.use(require('vue-cookies'));

// vuejs logget and an object for configuration
const isProduction = process.env.NODE_ENV === 'production';
Vue.use(vueLogger, {
  isEnabled: true,
  logLevel: isProduction? 'error' : 'debug',
  stringifyArguments: false,
  showMethodName: true,
  separator: '|',
  showConsoleColors: true,
  showLogLevel: true,
});

Vue.config.productionTip = false;
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