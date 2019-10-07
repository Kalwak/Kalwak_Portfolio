<!--
  STRUCTURE OF THIS COMPONENT
  DIV // CLASSES: FILTER-OPTION // MAIN CONTAINER FOR FILTER COMPONENT
    SPAN // CLASSES: LABEL // LABEL FOR CURRENT SELECTED OPTION
    DIV // CLASSES: OPTIONS__LIST // CONTAINER FOR LIST OF AVAILABLE OPTIONS
      SPAN // CLASSES: OPTION // CONTAINER FOR A PARTICULAR OPTION
-->
<template>
  <div class="filter-option">
    <span class="label" 
      @mouseover="setLabelHoveredStatus(true);"
      @mouseout="setLabelHoveredStatus(false)">
      {{ label }} 
      <span :class="{ 'icon-down-open-mini': !labelHovered, 'icon-up-open-mini': labelHovered }"></span>
    </span>
    <div class="options__list"
      @mouseover="setLabelHoveredStatus(true);"
      @mouseout="setLabelHoveredStatus(false);">
      <span 
        class="option"
        :class="{ 'selected-text': option === selectedOption }"
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

    defaultOption: {
      type: String | Number
    },

    label: {
      type: String,
      required: true,
    }
  },

  methods: {
    // @vuese
    // sets the value of the given argument to the selectedOption property
    // and also emits custom event called getOption which is payload is the option given argument as well
    // @arg option value which will be set as the value of selectedOption property
    // @arg emit, boolean value by default is true, used to check if the method should emit the custom event getOption
    setOption(option, emit = true) {
      if ((typeof option !== 'string') && (typeof option !== 'number')) {
        return false;
      }
      this.selectedOption = option;
      // storing value as string values
      emit ? this.$emit('getOption', option + '') : '';
    },

    // @vuese
    // used to set labelHovered property to the given argument
    // @arg status is a boolean value
    setLabelHoveredStatus(status) {
      this.labelHovered = status;
    },
  },

  created() {
    this.setOption(this.defaultOption)
  }
};
</script>