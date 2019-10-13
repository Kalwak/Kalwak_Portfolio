export default {
  name: 'post-heading',
  props: {
    level: {
      type: Number,
      required: true
    },
    text: {
      type: String,
      required: true
    }
  },

  render(createElement) {
    let heading = 'h' + this.level;
    return createElement(
      heading,
      this.text
    )
  }
}