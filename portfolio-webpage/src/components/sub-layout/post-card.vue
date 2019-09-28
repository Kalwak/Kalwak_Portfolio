<!--
  STRUCTURE OF THIS COMPONENT
  DIV // CLASSES: POST-CARD // CONTAINER FOR POST-CARD
    HEADER // CLASSES: POST-CARD__HEADER // HEADER SECTION OF THE POST-CARD
      DIV // CLASSES: POST-CARD__COVER // CONTAINER FOR THUMBNAIL IMAGE
        IMG // CLASSES: COVER__IMAGE // IMAGE USED TO SHOW THUMBNAIL
      SPAN // CLASSES: POST-CARD__CATEGORY // CATEGORY FOR THE POST-CARD
    DIV // CLASSES: POST-CARD__BODY // BODY SECTION FOR THE POST-CARD
      H4 // CLASSES: POST-CARD__TITLE // POST-CARD TITLE
      P // CLASSES: POST-CARD__DESCRIPTION // POST-CARD DESCRIPTION TEXT
    FOOTER // CLASSES: POST-CARD__FOOTER // FOOTER SECTION FOR THE POST-CARD
      DIV // CLASSES: POST-CARD__DETAILS // CONTAINER FOR POST-CARD DETAILS
        SPAN // CLASSES: POST-CARD__AUTHOR // AUTHOR OF THE POST
        SPAN // CLASSES: POST-CARD__DATE // DATE FOR POST-CARD

-->
<template>
  <div class="post-card">
    <header class="post-card__header">
      <div class="post-card__cover">
        <img src="https://images.pexels.com/photos/879109/pexels-photo-879109.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="imagen miniatura" class="cover__image" />
      </div>
      <span class="post-card__category">{{ post.tag }}</span>
    </header>
    <div class="post-card__body">
      <h4 class="post-card__title">{{ post.title }}</h4>
      <p class="post-card__description">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi inventore quas non accu...
      </p>
    </div>
    <footer class="post-card__footer">
      <div class="post-card__details">
        <span class="post-card__author">{{ post.author }}</span>
        <span class="post-card__date">{{ post.date }}</span>
      </div>
    </footer>
  </div>
</template>

<script>
// showcase a single post informnation through a good-looking card


export default {
  name: 'post-card',
  props: {
    // object which contains post title, tag, author and date
    post: {
      type: Object,
      required: true,
    },
  },
};
</script>