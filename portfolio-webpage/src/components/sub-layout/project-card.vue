<template>
    <div class="project-container">
        <div class="project__header">
            <div class="inner-wrapper">
                <h3 class="project__title">{{ project.name }}</h3>
                <carousel
                        class="project__carousel"
                        :key="project.pageId"
                        :per-page="1"
                        :loop="true"
                        :autoplay="true"
                        :autoplay-timeout="4000"
                        :pagination-enabled="false"
                        :navigation-enabled="true"
                        navigation-prev-label="<span class='icon-left-arrow carousel__arrow'></span>"
                        navigation-next-label="<span class='icon-right-arrow carousel__arrow'></span>">
                    <slide class="project__carousel__slide" v-for="(image, index) in project.images" :key="index">
                        <div class="project__images">
                            <img :src="image.cover_page" :alt="project.title"/>
                            <h3 class="image__category">{{ project.categories[0] }}</h3>
                        </div>
                    </slide>
                </carousel>
            </div>
        </div>
        <div class="inner-wrapper">
            <div class="project__body">
                <h3 class="project__title">{{ project.subtitle }}</h3>
                <div class="project__description">
                    <p class="description__text" v-html="project.description"></p>
                    <p class="description__widget">Dirección de la página web <a :href="project.website" tabindex="_blank">{{ project.website }}</a></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // project component
    import {Carousel, Slide} from 'vue-carousel';


    // @vuese
    export default {
        name: 'project-card',

        components: {
            // from vue-carousel, this is the carousel main container
            Carousel,
            // from vue-carousel, this is the slide that goes into caoursel component
            Slide
        },

        props: {
            // object with project information like name, images, description, url
            project: {
                type: Object,
                required: true,
            },
        },
    }
</script>
