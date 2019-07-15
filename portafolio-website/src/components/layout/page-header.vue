<template>
  <header class="header row">
    <div class="col-auto">
      <div class="brand">
        <div class="brand__logo">
          <a href="/" title="Wink">
            <img src="@/assets/images/logo.svg" alt="Wink logo" title="Wink logo" class="logo__image" />
          </a>
        </div>
      </div>
    </div>
    <nav class="nav col-auto">
      <router-link to="/"><a class="nav__item">Sobre nosotros</a></router-link>
      <router-link to="/"><a class="nav__item">Servicios</a></router-link>
      <router-link to="/"><a class="nav__item">Cotizar</a></router-link>
      <router-link to="/"><a class="nav__item">Contacto</a></router-link>
    </nav>
    <div class="col-auto">
      <div class="lang-switcher">
        <img src="@/assets/images/spanish-lang.svg" alt="Spain flag" class="lang" title="spanish" />
        <img src="@/assets/images/english-lang.svg" alt="USA flag" class="lang" title="english" />
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'page-header'
}
</script>

