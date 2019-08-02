<!--
  ABOUT US VIEW
  STRUCTURE OF THIS SECTION
  - DIV CONTAINER // WHICH ACTUALLY IS A COLUMN 
      - ABOUT-SECTION
        - INNER-WRAPPER CLASS // LIMIT PAGE WIDTH
          - WITHOUT CONTENT //
      - TEAM-SECTION
        - INNER-WRAPPER CLASS
          - TEAM-MEMBER COMPONENT // REPRESENTS A TEAM MEMBER
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
        <team-member :member="teamMember" v-for="teamMember in teamMembersData" :key="teamMember.id" />
      </div>
    </div>
  </div>
</template>

<script>
import TeamMember from '@/components/sub-layout/team-member.vue';
import teamMembersData from '@/team-members.json';


export default {
  name: 'about-us',
  data() {
    return {
      teamMembersData
    };
  },

  components: {
    TeamMember
  },
}
</script>

