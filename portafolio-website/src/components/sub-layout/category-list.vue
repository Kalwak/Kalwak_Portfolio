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
        <router-link to="/projects/category/web-development">
          <img src="~@/assets/images/categories-images/category-1.png" alt="categoria" class="category__icon" />
        </router-link>
      </div>
      <div class="list__category">
        <router-link to="/projects/category/web-payment">
          <img src="~@/assets/images/categories-images/category-2.png" alt="categoria" class="category__icon" />
        </router-link>
      </div>
      <div class="list__category">
        <router-link to="/projects/category/inventory-systems">
          <img src="~@/assets/images/categories-images/category-3.png" alt="categoria" class="category__icon" />
        </router-link>
      </div>
      <div class="list__category">
        <router-link to="/projects/category/graphic-design">
          <img src="~@/assets/images/categories-images/category-4.png" alt="categoria" class="category__icon" />
        </router-link>
      </div>
    </div>
  </div>
</template>