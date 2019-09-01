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
            <h2>¡Kalwak es una compañía que tiene la solución de software que necesita! Utilizando ingeniería rápida y
                eficiente le proporcionamos un software de primer nivel, personalizado hasta el último detalle.</h2>
            <h2>Misión: Integrarse al ambiente de PYMES y microempresas, ofreciendo software para su crecimiento, al igual
                que lograr el crecimiento de Kalwak.</h2>
            <h2>Visión: Un país donde cada empresa tenga su representación digital, ya sea en una página web o en un
                aplicación, con el fin de promover el avance a la era digital, aprovechando cada uno de sus beneficios.</h2>

        </div>
      </div>
      <div class="team-section">
        <div class="inner-wrapper">
          <team-member :member="teamMember" v-for="teamMember in teamMembersData" :key="teamMember.id"/>
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

