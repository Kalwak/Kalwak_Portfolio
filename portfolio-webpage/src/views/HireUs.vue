<!--
  HIRE-US VIEW
  STRUCTURE OF THIS SECTION
  - DIV // CLASSES: COL-12 // THIS IS THE MAIN CONTAINER FOR ALL THE SECTION
    - DIV // CLASSES: HIRE-US // CONTAINER FOR CONTACT FORM FOR HIRING US
      - H2 // CLASSES: HIRE-US__TITLE // MAIN TITLE OF THIS SECTION
      - DIV // CLASSES: INNER-WRAPPER // LIMITER FOR PAGE WIDTH
        - H3 // CLASSES: HIRE-US__SUB-TITLE // SUBTITLE OF THIS SECTION
        - FORM // CLASSES: HIRE-FORM // FORM WHERE INPUTS FOR PROJECT WILL BE
          - DIV // CLASSES: HIRE-FORM__INPUTS // CONTAINER FOR INPUTS LIKE FNAME, LNAME, PHONENUMBER AND EMAIL
            - INPUT:VARY // CLASSES: HIRE-FORM__INPUT // INPUT FOR BASIC USER INFORMATION
          - DIV // CLASSES: SERVICE-PICKER // SECTION WHERE THE SERVICES WILL BE PICKED THROUGH CHECKBOXES
            - h4 // CLASSES: SERVICE-PICKER__TITLE // TITLE FOR THIS SECTION
            - DIV // CLASSES: SERVICE-PICKER__OPTIONS // CONTAINER FOR OPTION WHICH ARE CHECKBOXES AND LABELS
              - DIV // CLASSES: SERVICE-PICKER__OPTION // CONTAINER FOR CHECKBOX AND LABEL FOR SERVICE OPTION
                - INPUT:CHECKBOX // CLASSES: OPTION__CHECKBOX // INPUT TYPE CHECKBOX
                - LABEL // CLASSES: OPTION_LABEL // LABLE FOR CHECKBOX
          - DIV // CLASSES: HIRE-FORM__MESSAGE // CONTAINER FOR TEXTAREA
            - TEXTAREA // CLASSES: NONE // TEXTAREA TO GET INFORMATION ABOUT THE CLIENT'S THOUGHTS ABOUT HER/HIS PROJECT
          - DIV // CLASSES: HIRE-FORM__BUTTON // CONTAINER FOR BUTTON 
            - BUTTON // CLASSES: U-BUTTON // BUTTON WHERE API POST WILL BE TRIGGERED
-->
<template>
  <div class="col-12">
    <div class="hire-us">
        <h2 class="hire-us__title">¿Le gustaría trabajar con nosotros?</h2>
        <div class="inner-wrapper">
          <h3 class="hire-us__sub-title">Complete el siguiente formulario para ser ascesorado</h3>
          <form class="hire-form">
            <div class="hire-form__inputs">
              <label class="d-none" for="fName">Nombre</label>
              <input type="text" class="hire-form__input"  id="fName" v-model="user.firstName" placeholder="Nombre" />
              <label class="d-none" for="lName">Apellido</label>
              <input type="text" class="hire-form__input"  id="lName" v-model="user.lastName" placeholder="Apellido" />
              <label class="d-none" for="phone">Teléfono</label>
              <input type="tel" class="hire-form__input"  id="phone" v-model="user.phoneNumber" placeholder="Teléfono" />
              <label class="d-none" for="email">E-mail</label>
              <input type="email" class="hire-form__input"  id="email" v-model="user.email" placeholder="E-mail" />
            </div>
            <div class="service-picker">
              <h4 class="service-picker__title">Servicio a consultar</h4>
              <div class="service-picker__options">
                <div v-for="(option, idx) in options" class="service-picker__option" :key="idx">
                  <!-- change to :value="option.name" when every option.name is different, otherwise it'll get a bug when checking -->
                  <input  type="checkbox" :value="option.name + ' ' + option.id" v-model="pickedOptions" :id="option.id" class="option__checkbox" />
                  <label :for="option.id" class="option__label">{{ option.name + ' ' +  option.price }}</label>
                </div>
              </div>
              <small class="note-message">*El precio mostrado es un aproximado, puede variar dependiendo del proyecto</small>
            </div>
            <div class="hire-form__message">
              <label class="d-none" for="message">Consulta</label>
              <textarea v-model="user.message" id="message" placeholder="Cuentenos de su proyecto"></textarea>
            </div>
            <div class="hire-form__button">
              <button class="u-button" :disabled="buttonDisabled">Cotizar</button>
            </div>
          </form>
        </div>
    </div>
  </div>
</template>

<script>
// hire-us view component


// @vuese
export default {
  name: 'hire-us',

  data() {
    return {
      // avaliable options
      options: [
        {
          id: 1,
          name: 'Diseño web corporativo',
          price: '$1300'
        },
        {
          id: 2,
          name: 'Diseño web corporativo',
          price: '$1200'
        },
        {
          id: 3,
          name: 'Hosting basico',
          price: '$90/Año'
        },
        {
          id: 4,
          name: 'Diseño web corporativo',
          price: '$1200'
        },
        {
          id: 5,
          name: 'Diseño web corporativo',
          price: '$1200'
        },
        {
          id: 6,
          name: 'Diseño web corporativo',
          price: '$1200'
        },
        {
          id: 7,
          name: 'Diseño web corporativo',
          price: '$1200'
        },
        {
          id: 8,
          name: 'Diseño web corporativo',
          price: '$1200'
        },
      ],
      // picked options
      pickedOptions: [],

      // user information
      user: {
        firstName: '',
        lastName: '',
        email: '',
        phoneNumber: '',
        message: '',
      },
    };
  },

  computed: {
    // returns true if any of the required inputs is empty, else returns false
    buttonDisabledByInputs() {
      return !this.user.firstName 
      || !this.user.lastName
      || !this.user.phoneNumber
      || !this.user.email 
      || !this.user.message;
    },

    // button disabled based on buttonDisabledByInputs
    buttonDisabled() {
      return this.buttonDisabledByInputs;
    },
  },
}
</script>