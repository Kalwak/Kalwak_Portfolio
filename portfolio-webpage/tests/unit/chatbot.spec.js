import ChatBot from '../../src/components/sub-layout/chatbot.vue';
import { mount, createLocalVue } from '@vue/test-utils';


describe('chat-bot', () => {
  const $route = {
    path: '/some/path'
  };
  const localVue = createLocalVue();
  const wrapper = mount(ChatBot, {
    localVue,
    mocks: {
      $route
    },
  });


  it('should have a data option and should be a function', () => {
    expect(typeof ChatBot.data).toBe('function');
  });

  it('should have a messages data\'s property which is a array', () => {
    expect(ChatBot.data().messages).toEqual([]);
  });

  it('should have a message data\'s property which is a string', () => {
    expect(typeof ChatBot.data().message).toBe('string');
  });

  // computed properties
  it('should have a computed property called fullMessage', () => {
    expect(typeof ChatBot.computed.fullMessage).toBe('function');

    // should return an object
    expect(typeof wrapper.vm.fullMessage).toBe('object');
  });

  it('should have invalidInput set to true if message data\'s property is empty', () => {
    expect(wrapper.vm.invalidInput).toBe(true);
  });

  it('should have invalidInput set to false if message data\'s property is not empty', () => {
    wrapper.setData({
      message: 'Hello John Doe'
    });
    expect(wrapper.vm.invalidInput).toBe(false);
  }); 
  
  it('should have chatbotApi', () => {
    expect(wrapper.vm.chatbotApi).toBeTruthy();
  });

  // liecycle hooks
  it('should have a mounted hook', () => {
    expect(typeof ChatBot.mounted).toBe('function');
  });

  // methods 
  it('should have pushMessage method', () => {
    wrapper.setData({
      messages: [],
      message: 'Hello',
    });

    let fullMessage = wrapper.vm.fullMessage;

    wrapper.vm.pushMessage(fullMessage, true);
    let data = wrapper.vm.$data;

    expect(data.messages.length > 0).toBe(true);
  });
});