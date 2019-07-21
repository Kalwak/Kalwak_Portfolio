<!--
  page header
    - brand logo
    - navigation menu
    - language switcher
-->
<template>
  <header class="header row">
    <div class="col-12 inner-wrapper">
      <div class="row justify-content-between align-items-center">
        <div class="col-auto">
          <div class="brand">
            <div class="brand__logo">
              <a href="/" title="Wink">
                <img src="@/assets/images/logo.svg" alt="Wink logo" title="Wink logo" class="logo__image" />
              </a>
            </div>
          </div>
        </div>
        <nav-menu />
        <div class="col-auto">
          <div class="lang-switcher">
            <img src="@/assets/images/spanish-lang.svg" alt="Spain flag" class="lang" title="spanish" />
            <img src="@/assets/images/english-lang.svg" alt="USA flag" class="lang" title="english" />
          </div>
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

