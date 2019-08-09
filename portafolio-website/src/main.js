import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vueSmoothScroll from 'vue2-smooth-scroll';
import axios from 'axios';
import '../node_modules/swiper/dist/js/swiper.min.js';
import './assets/css/main.scss';


Vue.config.productionTip = false;
Vue.use(vueSmoothScroll);
Vue.prototype.$axios = axios;

new Vue({
  router,
  store,
  // render: h => h(App),
  render: createElement => createElement(App),
}).$mount('#app');