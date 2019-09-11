<template>
  <div class="chatbot-container" @click.stop="">
    <div class="chatbot__header">
      <h5 class="chatbot__header-title">
        <img  src="~@/assets/images/logo.svg" width="100px" />
      </h5>
      <div class="chatbot__header-settings">
          <span class="chatbot__setting-icon" @click="clearMessages">
            <img src="~@/assets/images/chatbot-icons/refresh-icon.png" alt="borrar mensajes"  class="setting-icon__image" title="borrar mensajes" />
          </span>
          <span class="chatbot__setting-icon" @click="closeChatbot">
            <img src="~@/assets/images/chatbot-icons/close-icon.png" alt="cerrar"  class="setting-icon__image"  title="cerrar" />
          </span>
      </div>
    </div>
    <div class="chatbot__body">
      <div class="chatbot-messages__container" ref="messages">
        <div 
          class="message-container"
          :class="{ 'bubble--right': message.type === 'human' }"
          v-for="message in messages" :key="message.id">
          <p class="message__bubble animated fadeIn" 
            :class="{ 'orange--bubble': message.type === 'bot' }">
            <span class="message__text" v-html="message.text"></span>
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
import swal from 'sweetalert';


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
      let time = new Date().toLocaleTimeString();
      time = this.getTimewithOutSeconds(time);
      return {
        type: 'human',
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

    // get current $path form $route
    currentPath() {
      return this.$route.path;
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
        this.message = '';
        this.PostMessageToChatbot({
          ip: bubbleMessage.ip,
          msg: bubbleMessage.text,
        });
        this.saveMessageToLocalStorage(bubbleMessage);
        this.loadMessagesFromLocalStorage();

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
    // clear messages of the localStorage _messages.messages
    clearMessages() {
      let _messages = JSON.parse(localStorage.getItem('_messages'));
      if (typeof _messages === 'object') {
        if (!_messages.messages) return false;
        _messages.messages = [];
        localStorage.setItem('_messages', JSON.stringify(_messages));
        this.loadMessagesFromLocalStorage();
      } else return false;
    },

    // @vuese
    // returns a string with the time, but without seconds information
    // @args time string // should be the string returned from new Date().toLocaleTimeString
    // or string with format hh:mm:ss am/pm, i.e 12:00:10 pm 
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
    // push bot response to localStoge _messages.messages object
    setChatbotResponseMessage(response) {
      let message = {
        type: 'bot',
        text: response,
        time: this.getTimewithOutSeconds(new Date().toLocaleTimeString()),
      };
      
      // save bot response to localStorage
      this.saveMessageToLocalStorage(message);
      this.loadMessagesFromLocalStorage();
      this.$nextTick(() => {
        this.scrollBottom();
      });
    },
    // @vuese
    // used to post message to bot api
    // @arga message, this has to contain user ip and msg string
    PostMessageToChatbot(message) {
      let chatbotUrl = this.chatbotApi;
      window.setTimeout(() => {
        axios.post(chatbotUrl, message)
          .then(response => {
            this.setChatbotResponseMessage(response.data);
          })
          .catch(error => {
            swal({
              title: 'Notificación',
              text: 'Hubo un error, intente otra vez'
            }); 
          });
      }, 500);
    },

    // @vuese
    // set localStorage item _messages, which
    // is an object where messages from both user and bot 
    // are store, also last user message is storage
    setMessagesLocalStorageItem() {
      // create localStorage item for messages information
      // which in an object
      if (!localStorage.getItem('_messages')) {
        localStorage.setItem('_messages', JSON.stringify({
          messages: [],
          lastMessage: '',
        }));
      };
    },

    // @vuese
    // push message object to localStorage _messages.messages, which is an array of object
    // @args message, object with text, time and type properties
    saveMessageToLocalStorage(message) {
      // first check if localStorage item _messages is created && it's type of an object
      let _messages = JSON.parse(localStorage.getItem('_messages'));
      if (typeof _messages === 'object') {
        // only need text type and date from message if they're not, return false
        if ((typeof message !== 'object') && ((!message.text) || (!message.type) || (!message.time))) {
          return false;
        };
        _messages.messages.push({
          type: message.type,
          text: message.text,
          time: message.time,
          id: _messages.messages.length + 1,
        });

        localStorage.setItem('_messages', JSON.stringify(_messages));
      } else return false;
    },
    
    // @vuese
    // load last message from ocalStorage _messages.lastMessage, which is a string
    loadLastMessageFromLocalStorage() {
      let _messages = JSON.parse(localStorage.getItem('_messages'));
      if (typeof _messages === 'object') {
        this.message = _messages.lastMessage;
      } else return false;
    },

    // @vuese 
    // save last user message to the localStorage _messages.lastMessage
    // @args message, string
    saveLastMessageToLocalStorage(message) {
      let _messages = JSON.parse(localStorage.getItem('_messages'));
      if (typeof _messages === 'object') {
        if (typeof message !== 'string') {
          return false;
        }
        _messages.lastMessage = message;
        localStorage.setItem('_messages', JSON.stringify(_messages));
      } else return false;
    },

    // @vuese
    // 
    loadMessagesFromLocalStorage() {
      let _messages = JSON.parse(localStorage.getItem('_messages'));
      if (typeof _messages === 'object') {
        if (!_messages.messages) {
          return false;
        }
        this.messages = _messages.messages;
      } else return false;
    },
  },

  // one purpose, everytime is mounted, the focusInput method will be called
  // and the message input will be focus, ready for use input
  mounted() {
    this.focusInput();
    this.scrollBottom();
  },

  created() {
    this.setMessagesLocalStorageItem();
    this.loadMessagesFromLocalStorage();
    this.loadLastMessageFromLocalStorage();
  },

  beforeDestroy() {
    // before component instance ins destroy, saveLastMessageToLocalStorage will save user message 
    this.saveLastMessageToLocalStorage(this.message);
  },
}
</script>