<!--
  CATEGORY LIST
  STRUCTURE OF THIS SECTION
    - CONTAINER FOR CATEGORY LIST
        - INNER WRAPPER // THIS IS A UTILITY CLASS TO LIMIT CONTENT WIDTH
        - LIST CATEGORY CONTAINER // THIS IS WHERE A CATEGORY WILL BE PLACED
          - ROUTER-LINK // TO MATCHED TO THE CATEGORIES ROUTES [WEB-DEVELOPMENT, WEB-PAYMENT, INVENTORY-SYSTEMS, GRAPHIC-DESIGN]
            - IMAGE TO SHOW AS AN ICON FOR THE CATEGORY
--->
<template>
    <div class="category-list">
        <div class="inner-wrapper">
            <div class="list__category">
                <router-link to="/projects/web-development">
                    <img src="~@/assets/images/categories-images/category-1.png" alt="web development"
                         class="category__icon"/>
                </router-link>
            </div>
            <div class="list__category">
                <router-link to="/projects/web-payments">
                    <img src="~@/assets/images/categories-images/category-2.png" alt="web payments"
                         class="category__icon"/>
                </router-link>
            </div>
            <div class="list__category">
                <router-link to="/projects/inventory-systems">
                    <img src="~@/assets/images/categories-images/category-3.png" alt="inventory systems"
                         class="category__icon"/>
                </router-link>
            </div>
            <div class="list__category">
                <router-link to="/projects/graphic-design">
                    <img src="~@/assets/images/categories-images/category-4.png" alt="graphic design"
                         class="category__icon"/>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    // category list


    import {ProjectService} from "../../services/project_service";

    function format_to_slug(string) {
        string = string.replace(' ', '-');
        return string;
    }

    export default {
        name: 'category-list',

        computed: {
            // category that comes from the router params
            category() {
                return this.$route.params.category.split('-').join(' ');
            },

        },

        created() {
            const self = this;
            console.log('category set');

            let service = new ProjectService();
            service.getProjects().then((data) => {
                self.$store.commit('setAllProjects', data);
                self.$store.commit('setCategory', format_to_slug(self.category));
                self.$store.dispatch('setProjectsByCategory');
            }).catch(err => console.error(err));
        },

        watch: {
            category(newCategory) {
                const self = this;
                self.$store.commit('setCategory', format_to_slug(newCategory));
                self.$store.dispatch('setProjectsByCategory');
            },
        },
    }
</script>
