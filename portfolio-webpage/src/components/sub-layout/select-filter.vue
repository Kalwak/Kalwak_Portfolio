<template>
  <div class="filter-option">
    <span class="label" 
      @mouseover="setLabelHoveredStatus(true);"
      @mouseout="setLabelHoveredStatus(false)">
      {{ selectedOption }} 
      <span :class="{ 'icon-down-open-mini': !labelHovered, 'icon-up-open-mini': labelHovered }"></span>
    </span>
    <div class="options__list"
      @mouseover="setLabelHoveredStatus(true);"
      @mouseout="setLabelHoveredStatus(false);">
      <span 
        class="option"
        v-for="(option, index) in options"
        :key="index"
        @click="setOption(option)">
          {{ option }}
        </span>
    </div>
  </div>
</template>

<script>
// select-filter component, provides a select box, when hovering there will be
// a list of options (provided by options prop)


// @vuese
export default {
  name: 'select-filter',

  data() {
    return {
      selectedOption: '',
      labelHovered: false,
    };
  },

  props: {
    // array of options that will be displayed in the options list
    options: {
      type: Array,
      required: true,
    },
    // default option that will be taken and set as the selected option
    defaultOption: {
      type: String | Number,
      required: true,
    },
  },

  methods: {
    // @vuese
    // sets the value of the given argument to the selectedOption property
    // and also emits custom event called getOption which is payload is the option given argument as well
    // @arg option value which will be set as the value of selectedOption property
    setOption(option) {
      if ((typeof option !== 'string') && (typeof option !== 'number')) {
        this.$log.error('option must be a string or a number', 'but is', typeof option)
        return false;
      }
      this.selectedOption = option;
      this.$emit('getOption', option);
    },

    // @vuese
    // used to set labelHovered property to the given argument
    // @arg status is a boolean value
    setLabelHoveredStatus(status) {
      this.labelHovered = status;
    },
  },

  created() {
    this.setOption(this.defaultOption);
  }
};
</script>