import PostCard from '@/components/sub-layout/post-card.vue';
import { mount } from '@vue/test-utils';

describe('post-card', () => {
  it('should render everything post object values fine', () => {
    const wrapper = mount(PostCard, {
      propsData: {
        post: {
          tag: 'category',
          title: 'title',
          author: 'John Doe',
          date: 'date',
        },
      },
    });

    let post = wrapper.props().post;
    expect(wrapper.find('.post-card__category').text()).toBe(post.tag);
    expect(wrapper.find('.post-card__title').text()).toBe(post.title);
    expect(wrapper.find('.post-card__author').text()).toBe(post.author);
    expect(wrapper.find('.post-card__date').text()).toBe(post.date);
  });
});