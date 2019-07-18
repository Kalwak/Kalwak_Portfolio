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
    <nav class="nav col-auto column">
      <div class="nav__item dropdown-list" @mouseover="dropdown = true" @mouseout="dropdown = false">
        <span class="dropdown__label">
          Sobre nosotros <span class="icon-down-open-mini"></span>
        </span>
        <transition name="dropdown">
          <div class="dropdown__options" v-if="dropdown">
            <span class="dropdown__option">Quienes somos ?</span>
            <span class="dropdown__option">Trabajos anteriores</span>
          </div>
        </transition>
      </div>
      <router-link to="/"><a class="nav__item">Servicios</a></router-link>
      <router-link to="/"><a class="nav__item">Cotizar</a></router-link>
      <router-link to="/"><a class="nav__item">Contacto</a></router-link>
    </nav>
    <div class="col-auto column">
      <div class="lang-switcher">
        <img src="@/assets/images/spanish-lang.svg" alt="Spain flag" class="lang" title="spanish" />
        <img src="@/assets/images/english-lang.svg" alt="USA flag" class="lang" title="english" />
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'page-header',
  data() {
    return {
      dropdown: false,
    };
  },
}
</script>

