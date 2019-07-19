<!--
  main navigation menu 
  - About us  
    - Who are we ?
    - Projects
  - Services
  - Cotizar
  - Contact
-->
<template>
  <nav class="nav col-auto column">

    <div class="nav__item">
      <span class="nav__link nav__link--flex">Sobre nosotros<span class="icon-down-open-mini"></span></span>
      <div class="dropdown-list">
        <router-link to="/team"><a class="dropdown-list__item nav__link">Quienes somos ?</a></router-link>
        <router-link to="/projects"><a class="dropdown-list__item nav__link">Proyectos anteriores</a></router-link>
      </div>
    </div>

    <div class="nav__item">
      <router-link to="/services" class="nav__link">Servicios</router-link>
    </div>

    <div class="nav__item">
      <router-link to="/cotizar" class="nav__link">Cotizar</router-link>
    </div>

    <div class="nav__item">
      <router-link to="/contact" class="nav__link">Contacto</router-link>
    </div>
  </nav>
</template>

