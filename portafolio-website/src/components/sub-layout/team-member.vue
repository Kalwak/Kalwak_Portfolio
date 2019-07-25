<template>
  <div class="team__member">
    <div class="inner-wrapper">
      <div class="member__content">
        <p>image goes here</p>
      </div>
      <div class="member__content">
        <h4 class="font-weight-bold text-uppercase">{{ memberData.name }}</h4>
        <p>{{ memberData.biography }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'team-member',
  props: {
    memberData: {
      type: Object,
      required: true,
    } 
  }
}
</script>

