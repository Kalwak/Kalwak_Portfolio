<!--
  PAGE HEADER
    structure of this section
    - header
      - brand-logo // here is presented the page brand logo
      - navigation-menu // here is represented the navigation menu for 
        [about-us, projects, services, prices, contact, language-switcher]
-->
<template>
  <header class="header row animated slideInDown">
    <div class="col-12">
      <div class="inner-wrapper">
        <div class="row justify-content-between align-items-center">
          <div class="col-auto brand-column">
            <div class="brand">
              <div class="brand__logo">
                <a href="/" title="kalwak">
                  <img src="@/assets/images/logo.svg" alt="Wink logo" title="Kalwak logo" class="logo__image" />
                </a>
                <!-- <span class="menu-button" >menu</span> -->
              </div>
              <button class="hamburger hamburger--squeeze menu-button" :class="{ 'is-active': activatedMenu }" type="button" @click="activatedMenu = !activatedMenu">
                <span class="hamburger-box">
                  <span class="hamburger-inner"></span>
                </span>
              </button>
            </div>
          </div>
          <nav-menu  :class="{ activatedMenu }" />
      </div>
      </div>
    </div>
  </header>
</template>

<script>
import NavMenu from '@/components/sub-layout/navigation-menu.vue';

export default {
  name: 'page-header',
  data() {
    return {
      activatedMenu: false
    };
  },
  
  components: {
    NavMenu
  }
}
</script>

