<!--
  TEAM-MEMBER COMPONENT
  STRUCTURE OF THIS SECTION
  - TEAM__MEMBER // CONTAINER FOR USER INFORMATION
    - INNER-WRAPPER // USED TO LIMIT PAGE WIDTH
      - MEMBER__CONTENT // THERE ARE TWO OF THEM ... ONE TO REPRESENT USER PICTURE,
      THE OTHER TO SHOW INFORMATION OF THE USER LIKE NAME AND BIOGRAPHY
        - MEMBER__IMAGE // CONTAINER FOR USER PICTURE
          - IMAGE // IMG ELEMENT WITH CLASS IMAGE
        - MEMBER__INFORMATION // HERE IS SHOWN USER 
          - MEMBER__NAME // H3 ELEMENT, HERE WILL BE USER NAME
          - MEMBER__BIOGRAPHY // P ELEMENT, HERE WILL BE USER BIOGRAPHY
-->
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
// team-member component, used to show information about a member,
// like name, biography and profile photo

// @vuese
export default {
  name: 'team-member',
  props: {
    // member prop, this will be the object with member information
    member: {
      type: Object,
      required: true,
    } 
  }
}
</script>

