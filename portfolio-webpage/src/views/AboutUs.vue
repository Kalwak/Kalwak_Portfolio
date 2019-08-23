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
        <h2>Misión</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam mauris elit, maximus vel odio nec, sagittis pulvinar enim. Duis faucibus libero vitae ultricies pellentesque. Nulla facilisi. Cras vestibulum sagittis magna, vitae vestibulum dui commodo non. Nullam maximus luctus enim, quis tempus nunc aliquam non. Praesent pulvinar, odio sit amet bibendum pretium, velit ex iaculis leo, sed auctor nisi nulla sed ex. Nunc ut mi ut mi cursus feugiat. Vivamus elementum ultricies purus, id cursus lorem fermentum nec. Etiam gravida pellentesque bibendum. Donec laoreet ornare tortor, a faucibus erat rutrum eu. Proin vestibulum mi mollis, viverra mi non, auctor risus. Praesent vulputate sit amet libero ac elementum.
        </p>
        <h2>Visión</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam mauris elit, maximus vel odio nec, sagittis pulvinar enim. Duis faucibus libero vitae ultricies pellentesque. Nulla facilisi. Cras vestibulum sagittis magna, vitae vestibulum dui commodo non. Nullam maximus luctus enim, quis tempus nunc aliquam non. Praesent pulvinar, odio sit amet bibendum pretium, velit ex iaculis leo, sed auctor nisi nulla sed ex. Nunc ut mi ut mi cursus feugiat. Vivamus elementum ultricies purus, id cursus lorem fermentum nec. Etiam gravida pellentesque bibendum. Donec laoreet ornare tortor, a faucibus erat rutrum eu. Proin vestibulum mi mollis, viverra mi non, auctor risus. Praesent vulputate sit amet libero ac elementum.
        </p>
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
// about-us view component
import TeamMember from '@/components/sub-layout/team-member.vue';
import teamMembersData from '@/team-members.json';


// @vuese
export default {
  name: 'about-us',
  data() {
    return {
      // array of objects, each object with member information
      teamMembersData
    };
  },

  components: {
    // team-member component, where information about the member will shown
    TeamMember
  },
}
</script>

