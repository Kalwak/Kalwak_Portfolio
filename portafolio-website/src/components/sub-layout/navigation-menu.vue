<!--
  MAIN NAVIGATION MENU // this component is in the PAGE HEADER
  structure of this section
  - nav // navigation, this element works as a container for every navigation item or link
    - nav__item // this is a nav item that actually works as a container for the actual link
      - nav__link //  there are two options, if this is not intended for a link to drive to another section
        or website, so this will work just as a label/trigger to open a dropdown list to show more links,
        the second option is intended just to work as a hyperlink to drive to a view like about-us, projects, servies, etc.
      - dropdown-list // a dropdown list of hyperlinks if only the nav__link works as a trigger
        - dropdown-list__item // this one works as the nav__link (if needed there could be a dropdown list ...)
      - language-switcher // this one is a especial item for the navigation menu, it will work to switch between inglish and spanish 

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
          <router-link to="/projects" class="nav__link">Proyectos anteriores</router-link>
        </div>
      </div>
    </div>

    <div class="nav__item">
      <router-link to="/services" class="nav__link">Servicios</router-link>
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

