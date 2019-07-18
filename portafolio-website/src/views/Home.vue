
<template>
  <div class="col-12 column">
    <div class="banner">
      <div class="banner__text text-uppercase">
        <h2 class="banner__text-title">
          Desarrollo web
        </h2>
        <p class="banner__text-description">
          Soluciones Innovadoras
        </p>
      </div>
    </div>
  <div class="col-12 column">
  </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    axios.get(`http://localhost:8000/`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.posts = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })

    // async / await version (created() becomes async created())
    //
    // try {
    //   const response = await axios.get(`http://jsonplaceholder.typicode.com/posts`)
    //   this.posts = response.data
    // } catch (e) {
    //   this.errors.push(e)
    // }
  }
}
</script>
