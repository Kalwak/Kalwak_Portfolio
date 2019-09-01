<template>
  <div class="chatbot-container">
    <div class="chatbot__header">
      <h5 class="chatbot__header-title">
        <img  src="~@/assets/images/logo.svg" width="100px" />
      </h5>
      <div class="chatbot__header-settings">
          <span class="chatbot__setting-icon">
            <img src="~@/assets/images/chatbot-icons/refresh-icon.png" alt="clear chatbot"  class="setting-icon__image" title="clear chatbot" @click="clearMessages" />
          </span>
          <span class="chatbot__setting-icon">
            <img src="~@/assets/images/chatbot-icons/close-icon.png" alt="close chatbot"  class="setting-icon__image"  title="close chatbot" @click="closeChatbot" />
          </span>
      </div>
    </div>
    <div class="chatbot__body">
      <div class="chatbot-messages__container" ref="messages">
        <div 
          class="message-container"
          :class="{ 'bubble--right': message.type === 'human' }"
          v-for="message in messages" :key="message.id">
          <p class="message__bubble animated fadeIn" :class="{ 'orange--bubble': message.type === 'bot' }">
            <span class="message__text">{{ message.text }}</span>
            <small class="message__information">{{ message.time }}</small>
          </p>
        </div>
      </div>
      <div class="chatbot-input__container">
        <input type="text" class="input-text" placeholder="Escriba aqui"  v-model="message" @keyup.enter="pushMessage(fullMessage)"  ref="messageInput" />
        <button class="send-button" @click="pushMessage(fullMessage)" :disabled="invalidInput">
          <img src="~@/assets/images/chatbot-icons/send-icon.png" alt="send" title="send message" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// chat-bot component, provides chat inbox where the messages will be sent to the backend chatbot service
import ip from 'ip';
import axios from 'axios';


// @vuese
export default {
  name: 'chat-bot',

  data() {
    return {
    // messages is an array with all the messages
      messages: [],

      // user message
      message: '',
    };
  },

  computed: {
    // return an object with full information about the user message
    // like message id, message type, by default is human, text which the user message and message time
    fullMessage() {
      let id = this.messages.length + 1;
      let time = new Date().toLocaleTimeString();
      time = this.getTimewithOutSeconds(time);
      return {
        type: 'human',
        id,
        text: this.message,
        time,
      };
    },

    // invalidInput // checks if message is empty, if it's empty return true else false
    invalidInput() {
      return !this.message.trim().length;
    },

    // composed chatbotApi url
    // got based api url from process.env.VUE_APP_API_ENDPOINT
    chatbotApi() {
      let baseUrl = process.env.VUE_APP_API_ENDPOINT;
      let chatbotUrl = `${baseUrl}/api/chatbot/`;
      return chatbotUrl;
    },

    // user, not sure if this is the needed for the chatbot
    userIp() {
      let ip = this.getIp();

      return ip;
    },
  },

  methods: {
    // @vuese
    // push all full message to messages array,
    // @args bubbleMessage is an object container message information like, id, time, message
    // @args disabledIp, default false
    pushMessage(bubbleMessage, disabledIp = false) {
      if(!disabledIp) {
        bubbleMessage.ip = this.userIp;
      };

      if (!this.invalidInput) {
        this.messages.push(bubbleMessage);
        this.message = '';

        // when the new message is already added in dom
        this.$nextTick(function() {
          this.scrollBottom();
        });
      };
    },

    // @vuese
    // close chatbot inbox by emitting a custom event,
    // in the parent component, the event will be triggered and 
    // chatbot will be removed from dom
    closeChatbot() {
      this.$emit('close-chatbot');
    },

    // @vuese
    // scroll to bottom of the message inbox
    // used when new messages are added to inbox messages container
    // so the client messages view will always be in the last message
    scrollBottom() {
      const messagesContainer = this.$refs.messages;
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    },

    // @vuese
    // focus message input by calling focus method, 
    // called in the mounted method 
    focusInput() {
      this.$refs.messageInput.focus();
    },

    // @vuese
    // mock getIp method, this one helps me out with an error when testing
    getIp() {
      return ip.address();
    },

    //@vuese
    // clear messages array to an empty array
    clearMessages() {
      this.messages = [];
    },

    // @vuese
    // returns a string with the time, but without seconds information
    // @args time string // should be the string returned from new Date().toLocaleTimeString
    // or string with format hh:mm:ss am/pm, i.e 12:00 pm 
    getTimewithOutSeconds(time) {
      if (typeof time !== 'string') {
        return 'time string required';
      };

      // get am or pm value reparated by the space
      const timeStatus = time.split(' ')[1];
      time = time.split(' ');
      time.splice(1, 1);
      time = time.join('');
      time = time.split(':');
      time.splice(2, 1);
      time = time.join(':');
      return `${time} ${timeStatus}`;
    },

    // @vuese
    // get the fist message from the bot 
    getFirstChatbotResponse() {
      let chatbotUrl = this.chatbotApi;
      axios.post('http://localhost:8000/api/chatbot/', {
          ip: this.userIp,
          msg: 'Hello',
        })
        .then(response => {
          console.log(response);
        })
        .catch(err => console.error(err));
    },
  },

  // one purpose, everytime is mounted, the focusInput method will be called
  // and the message input will be focus, ready for use input
  mounted() {
    this.focusInput();
    this.getFirstChatbotResponse();
  },
}
</script>