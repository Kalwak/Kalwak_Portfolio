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
    <div class="col-12">
        <div class="banner">
            <div class="inner-wrapper">
                <div class="banner__text">
                    <h2 class="banner__text-title">Desarrollo web</h2>
                    <h3 class="banner__text-description">Soluciones Innovadoras</h3>
                </div>
            </div>
        </div>
        <div class="projects-container">
            <div class="inner-wrapper">
                <h3 class="projects__title">Trabajos anteriores</h3>
                <carousel
                        :key="1"
                        :per-page="1"
                        :loop="true"
                        :autoplay="true"
                        :autoplay-timeout="4000"
                        :navigation-click-target-size="0"
                        :navigation-enabled="true"
                        :pagination-enabled="false"
                        navigation-prev-label="<span class='icon-left-arrow'></span>"
                        navigation-next-label="<span class='icon-right-arrow'></span>"
                        class="projects-slider">
                    <slide class="project-slide"
                        v-for="(project, index) in projects" :key="project.id">
                        <div class="image__container">
                            <img :src="project.cover_page" :alt="project.name" class="project__image">
                        </div>
                        <div class="information__container">
                            <h3 class="project__category">
                                <router-link :to="'/projects/' + project.categories[0]">{{ categoryFormatted[index] }}
                                </router-link>
                            </h3>
                        </div>
                    </slide>
                </carousel>
            </div>
        </div>
    </div>
</template>

<script>
    import {ProjectService} from "../services/project_service";
    // home views
    import {Carousel, Slide} from 'vue-carousel';


    const apiService = new ProjectService();

    export default {

        name: 'home',

        components: {
            // from vue-carousel, this is the carousel main container
            Carousel,
            // from vue-carousel, this is the slide that goes into caoursel component
            Slide
        },

        data() {

            return {
                projects: []
            };

        },

        methods: {

            getProjects() {
                // Gives us a list of projects from the django backend
                apiService.getProjects().then((data) => {
                    this.projects = data;
                    console.log(data);
                }).catch(err => console.error(err));
            },
        },

        mounted() {
            //Once the component is mounted we will fetch the projects
            this.getProjects();
        },


        computed: {
            categoryFormatted() {
                return this.projects.map(project => {
                    return project.categories[0].split('-').join(' ');
                });
            },
        },
    }
</script>
