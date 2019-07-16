<template>
  <header class="header row">
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
      <div class="nav__item dropdown-list">
        Sobre nosotros
        <div class="dropdown__options">
          <span class="dropdown__option">Quienes somos ?</span>
          <span class="dropdown__option">Trabajos anteriores</span>
        </div>
      </div>
      <div class="nav__item dropdown-list">
        Servicios
        <div class="dropdown__options">
          <span class="dropdown__option">Desarrollo web</span>
          <span class="dropdown__option">Desarrollo de software</span>
          <span class="dropdown__option">Pagos web</span>
          <span class="dropdown__option">Diseño grafico</span>
        </div>
      </div>
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
}
</script>

