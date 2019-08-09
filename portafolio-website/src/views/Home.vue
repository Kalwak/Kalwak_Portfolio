<!--
  HOME VIEW
  STRUCTURE OF THIS SECTION
  - MAIN COLUMN
    - BANNER // CONTAINER FOR BANNER
      - INNER-WRAPPER
        - BANNER__TEXT // CONTAINER FOR BANNER TEXT
          - BANNER__TITLE
          - BANNER__DESCRIPTION
    - PROJECTS-SECTION
      - INNER-WRAPPER
        - PROJECTS__TITLE // TITLE OF THIS SECTION
        - CAROUSEL // MAIN CONTAINER FOR PROJECTS CAROUSEL, ALSO HAS PROJECTS-SLIDER CLASS
          - SLIDE // CONTAINER FOR PROJECT INFORMATION, HAS PROJECT-SLIDE CLASS
            - IMAGE__CONTAINER // CONTAINER FOR PROJECT COVER IMAGE
              - COVER IMAGE WITH CLASS PROJECT__IMAGE
            - INFORMATION__CONTAINER // 
              - PROJECT__CATEGORY
--->
<template>
    <div>

    </div>
</template>

<script>
    import {ProjectService} from "../services/project_service";

    const apiService = new ProjectService();

    export default {

        name: 'home',

        components: {},

        data() {

            return {
                contacts: [],
                numberOfContacts: 0,

            };

        },

        methods: {

            getContacts() {
                apiService.getProjects().then((data) => {

                    this.contacts = data.data;
                    this.numberOfContacts = data.count;
                    console.log(data);
                }).catch(err => console.error(err));
            },
        },

        mounted() {
            this.getContacts();
        },
    }
</script>
