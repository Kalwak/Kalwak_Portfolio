<template>
  <div class="team__member">
    <div class="inner-wrapper">
      <div class="member__content">
        <div class="member__image">
          <img src="~@/assets/images/banner.jpg" alt="placeholder image" class="image" />
        </div>
      </div>
      <div class="member__content">
        <div class="member__information">
          <h3 class="member__name text-uppercase">{{ member.name }}</h3>
          <p class="member__biography">{{ member.biography }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'team-member',
  props: {
    member: {
      type: Object,
      required: true,
    } 
  }
}
</script>

