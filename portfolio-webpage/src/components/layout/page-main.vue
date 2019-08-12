<!--
  PAGE MAIN
  STRUCTURE OF THIS SECTION 
  - MAIN (CLASS ROW) // THIS IS THE CONTAINER FOR THE VIEW-ROUTER
    - THE DIRECT CHILD OF THIS CONTAIER WILL ACTUALLY BE A MATCHED VIEW, LIKE ABOUT-US, PROJECTS, PRODUCTS, SERVICES
-->
<template>
  <main class="main row">
    <router-view></router-view>
  </main>
</template>

<script>
// views will render here, so its content is dynamic
export default {
  name: 'page-main'
}
</script>