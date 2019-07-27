import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vueSmoothScroll from 'vue2-smooth-scroll';
import 'bootstrap/dist/css/bootstrap.min.css';
import './assets/css/animate.css';
import '../node_modules/hamburgers/dist/hamburgers.min.css';
import './assets/icons/icons.css';
import './assets/css/main.scss';
Vue.config.productionTip = false;
Vue.use(vueSmoothScroll)

new Vue({
  router,
  store,
  // render: h => h(App),
  render: h => h(App)
}).$mount('#app');