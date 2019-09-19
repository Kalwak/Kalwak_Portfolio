<!--
  PAGE MAIN
  STRUCTURE OF THIS SECTION 
  - MAIN (CLASS ROW) // THIS IS THE CONTAINER FOR THE VIEW-ROUTER
    - THE DIRECT CHILD OF THIS CONTAIER WILL ACTUALLY BE A MATCHED VIEW, LIKE ABOUT-US, PROJECTS, PRODUCTS, SERVICES
-->
<template>
  <main class="main row">
    <router-view></router-view>
    <div class="chatbot-main-container" :class="{ 'chatbot-background': chatbotVisible }" @click="chatbotVisible = false">
      <chat-bot class="animated slideInUp"  @close-chatbot="chatbotVisible = false" v-if="chatbotVisible" />
    </div>
    <img src="~@/assets/images/chatbot-icons/chatbot-icon.png" alt="open chatbot" title="open chatbot" @click="chatbotVisible = true" class="chatbot-open-icon" />
  </main>
</template>

<script>
// views will render here, so its content is dynamic
import ChatBot from '../sub-layout/chatbot.vue';


// @vuese
export default {
  name: 'page-main',
  data() {
    return {
      // chatbotVisble for controlling chatbot position/visibility
      chatbotVisible: false,
    };
  },

  components: {
    // this represents the chatbot
    ChatBot
  },

  created() {
    // getting user ip when main component is created
    this.$store.dispatch('getUserIp');
  },
}
</script>