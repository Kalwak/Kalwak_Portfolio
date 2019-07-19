<!--
  page header
    - brand logo
    - navigation menu
    - language switcher
-->
<template>
  <header class="header row animated slideInLeft">
    <div class="col-auto column">
      <div class="brand">
        <div class="brand__logo">
          <a href="/" title="Wink">
            <img src="@/assets/images/logo.svg" alt="Wink logo" title="Wink logo" class="logo__image" />
          </a>
        </div>
      </div>
    </div>
    <nav-menu></nav-menu>
    <div class="col-auto column">
      <div class="lang-switcher">
        <img src="@/assets/images/spanish-lang.svg" alt="Spain flag" class="lang" title="spanish" />
        <img src="@/assets/images/english-lang.svg" alt="USA flag" class="lang" title="english" />
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

