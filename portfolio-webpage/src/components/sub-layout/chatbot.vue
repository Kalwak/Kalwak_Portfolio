<template>
  <div class="chatbot-container">
    <div class="chatbot__header">
      <h5 class="chatbot__header-title">Chatbot</h5>

      <div class="chatbot__header-settings">
        <span class="chatbot__setting-icon">Refresh</span>
        <span class="chatbot__setting-icon">Close</span>
      </div>
    </div>
    <div class="chatbot__body">
      <div class="chatbot-messages__container"></div>
      <div class="chatbot-input__container">
        <input type="text" class="input-text">
        <span class="send-button">Send</span>
      </div>
    </div>
  </div>
</template>