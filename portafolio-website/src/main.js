import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vueSmoothScroll from 'vue2-smooth-scroll';
import VAnimateCss from 'v-animate-css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './assets/css/animate.css';
import './assets/icons/icons.css';
import './assets/css/main.scss';
Vue.config.productionTip = false;
Vue.use(VAnimateCss);
Vue.use(vueSmoothScroll)

new Vue({
  router,
  store,
  // render: h => h(App),
  render: h => h(App)
}).$mount('#app');