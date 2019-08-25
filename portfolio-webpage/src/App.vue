<template>
  <div id="app" class="container-fluid">
    <page-header></page-header>
    <page-main></page-main>
    <page-footer></page-footer>
  </div>
</template>

<script>
// app components, this is the root component
import PageHeader from './components/layout/page-header.vue';
import PageMain from './components/layout/page-main.vue';
import PageFooter from './components/layout/page-footer.vue';


// @vuese
export default {
  name: 'app',
  components: {
    // this represents the header element
    PageHeader,
    // this represents the main content
    PageMain,
    // this represent the footer element
    PageFooter,
  }
}
</script>
