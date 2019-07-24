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
          <div class="col-auto">
            <div class="brand">
              <div class="brand__logo">
                <a href="/" title="kalwak">
                  <img src="@/assets/images/logo.svg" alt="Wink logo" title="Kalwak logo" class="logo__image" />
                </a>
              </div>
            </div>
          </div>
          <nav-menu />
      </div>
      </div>
    </div>
  </header>
</template>

<script>
import NavMenu from '@/components/sub-layout/navigation-menu.vue';

export default {
  name: 'page-header',
  components: {
    NavMenu
  }
}
</script>

