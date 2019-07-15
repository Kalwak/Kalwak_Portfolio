<template>
  <header class="header row">
    <div class="col-2">
      <div class="brand">
        <div class="brand__logo">
          <a href="/" title="Wink">
            <img src="@/assets/images/logo.svg" alt="Wink logo" title="Wink logo" class="logo-image" />
          </a>
        </div>
      </div>
    </div>
    <nav class="nav col-6">
      <router-link to="/"><a class="nav__item">Sobre nosotros</a></router-link>
      <router-link to="/"><a class="nav__item">Servicios</a></router-link>
      <router-link to="/"><a class="nav__item">Cotizar</a></router-link>
      <router-link to="/"><a class="nav__item">Contacto</a></router-link>
    </nav>
    <div class="col-2">
      <div class="language-switcher">
        <span class="icon-language">Language</span>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'page-header'
}
</script>

