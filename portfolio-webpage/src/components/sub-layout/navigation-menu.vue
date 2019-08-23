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
          <router-link to="/about-us" class="nav__link">¿Quiénes somos?</router-link>
        </div>
        <div class="dropdown-list__item">
          <router-link :to="'/projects/' + projectCategory" class="nav__link">Trabajos anteriores</router-link>
        </div>
      </div>
    </div>

    <div class="nav__item">
      <router-link :to="'/services/' + serviceCategory" class="nav__link">Servicios</router-link>
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

<script>
// navigation menu component



// @vuese
export default {
  name: 'navigation-menu',

  computed: {
    // returns category from the store (vuex)
    projectCategory() {
      let category = this.$store.state.projects.projectsCategory;
      if (!category.length) {
        return 'web-development';
      } else {
        return category.split(' ').join('-');
      }
    },

    // returns service category 
    serviceCategory() {
      return 'web-development';
    },

    currentPath() {
      return this.$route.path;
    },
  },

  watch: {
    currentPath() {
      console.log('ok currentPath changed');
      this.$emit('close-nav-menu', false);
    },
  },
}
</script>


