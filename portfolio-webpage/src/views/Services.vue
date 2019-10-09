<!--
  SERVICES VIEW
  STRUCTURE OF THIS SECTIION
  -CATEGORY-LiST // LIST OF CATEGORIES FOR SERVICES
    - INNER-WRAPPER // LIMIT WIDTH
  - ROUTER-VIEW // ROUTE WILL MATCH A SERVICE ...

-->
<template>

  <div class="col-12">
    <div class="category-list">
      <div class="inner-wrapper">
        <div class="list__category">
          <router-link to="/services/web-development">
            <img src="~@/assets/images/categories-images/category-1.png" alt="web development" class="category__icon" />
          </router-link>
        </div>
        <div class="list__category">
          <router-link to="/services/web-payments">
            <img src="~@/assets/images/categories-images/category-2.png" alt="web payments" class="category__icon" />
          </router-link>
        </div>
        <div class="list__category">
          <router-link to="/services/inventory-systems">
            <img src="~@/assets/images/categories-images/category-3.png" alt="inventory systems" class="category__icon" />
          </router-link>
        </div>
        <div class="list__category">
          <router-link to="/services/graphic-design">
            <img src="~@/assets/images/categories-images/category-4.png" alt="graphic design" class="category__icon" />
          </router-link>
        </div>
        <!-- <div class="list__category">
          <router-link to="/services/products">
            <img src="~@/assets/images/categories-images/category-5.png" alt="services" class="category__icon" />
          </router-link>
        </div> -->
      </div>
    </div>
    <router-view />
  </div>
</template>
