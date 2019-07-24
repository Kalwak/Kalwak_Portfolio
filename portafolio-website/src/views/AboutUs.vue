<!--
  ABOUT US PAGE
  structure of section
-->
<template>
  <div class="col-12">
    <div class="about-section">
      <div class="inner-wrapper">
        <h2>Mision</h2>
        <h2>Vision</h2>
        <h2>Objetivos</h2>
      </div>
    </div>
    <div class="team-section">
      <div class="inner-wrapper">
        <team-member :memberData="teamMember" v-for="teamMember in teamMembers" :key="teamMember.id" />
      </div>
    </div>
  </div>
</template>

<script>
import TeamMember from '@/components/sub-layout/team-member.vue';


export default {
  name: 'about-us',
  computed: {
    teamMembers() {
      return this.$store.state.team.members;
    }
  },

  components: {
    TeamMember
  },

  created() {
    const self = this;
    self.$store.dispatch('getTeamMembersData');
  }
}
</script>

