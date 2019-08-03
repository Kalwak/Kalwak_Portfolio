<!--
  NAVBAR COMPONENT 
  STRUCTURE OF THIS SECTION
  - NAV ELEMENT CONTAINER FOR NAV__ITEMS 
    - NAV__ITEM FOR ACTUALLY ROUTER-LINK WITH SPECIFIC ROUTES THAT WILL MATCH A VIEW 
    OR SECTION OF THE PAGE, E.I, CONTACT.
-->
<template>
  <nav class="nav col-auto">
    <div class="nav__item">
      <span class="nav__link nav__link--flex">Sobre nosotros<span class="icon-down-open-mini"></span></span>
      <div class="dropdown-list">
        <div class="dropdown-list__item">
          <router-link to="/about-us" class="nav__link">Quienes somos ?</router-link>
        </div>
        <div class="dropdown-list__item">
          <router-link to="/projects" class="nav__link">Trabajos anteriores</router-link>
        </div>
      </div>
    </div>

    <div class="nav__item">
      <router-link to="/services" class="nav__link">Servicios</router-link>
    </div>

    <div class="nav__item">
      <router-link to="/products" class="nav__link">Productos</router-link>
    </div>

    <div class="nav__item">
      <router-link to="/cotizar" class="nav__link">Cotizar</router-link>
    </div>

    <div class="nav__item">
      <a href="#contact-section" class="nav__link" v-smooth-scroll>Contacto</a>
    </div>

    <div class="nav__item">
      <div class="lang-switcher">
        <img src="@/assets/images/spanish-lang.svg" alt="Spain flag" class="lang" title="spanish" />
        <img src="@/assets/images/english-lang.svg" alt="USA flag" class="lang" title="english" />
      </div>
    </div>
  </nav>
</template>

