<!--
  HIRE-US VIEW
  STRUCTURE OF THIS SECTION
  - DIV // CLASSES: COL-12 // THIS IS THE MAIN CONTAINER FOR ALL THE SECTION
    - DIV // CLASSES: HIRE-US // CONTAINER FOR CONTACT FORM FOR HIRING US
      - H2 // CLASSES: HIRE-US__TITLE // MAIN TITLE OF THIS SECTION
      - DIV // CLASSES: INNER-WRAPPER // LIMITER FOR PAGE WIDTH
        - H3 // CLASSES: HIRE-US__SUB-TITLE // SUBTITLE OF THIS SECTION
        - FORM // CLASSES: HIRE-FORM // FORM WHERE INPUTS FOR PROJECT INFORMATION WILL BE GIVEN BY USER
          - DIV // CLASSES: HIRE-FORM__INPUTS // CONTAINER FOR INPUTS LIKE FNAME, LNAME, PHONENUMBER AND EMAIL
            - INPUT:VARY // CLASSES: HIRE-FORM__INPUT // INPUT FOR BASIC USER INFORMATION
          - DIV // CLASSES: SERVICE-PICKER // SECTION WHERE THE SERVICES WILL BE PICKED THROUGH CHECKBOXES
            - h4 // CLASSES: SERVICE-PICKER__TITLE // TITLE FOR THIS SECTION
            - DIV // CLASSES: SERVICE-PICKER__OPTIONS // CONTAINER FOR OPTIONS WHICH ARE CHECKBOXES AND LABELS
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
                        <input type="text" class="hire-form__input" id="fName" v-model="service_request.first_name"
                               placeholder="Nombre"/>
                        <label class="d-none" for="lName">Apellido</label>
                        <input type="text" class="hire-form__input" id="lName" v-model="service_request.last_name"
                               placeholder="Apellido"/>
                        <label class="d-none" for="phone">Teléfono</label>
                        <input type="tel" class="hire-form__input" id="phone" v-model="service_request.telephone"
                               placeholder="Teléfono"/>
                        <label class="d-none" for="email">E-mail</label>
                        <input type="email" class="hire-form__input" id="email" v-model="service_request.email"
                               placeholder="E-mail"/>
                    </div>
                    <div class="service-picker">
                        <h4 class="service-picker__title">Servicio a consultar</h4>
                        <div class="service-picker__options">
                            <div v-for="(option, idx) in options" class="service-picker__option" :key="idx">
                                <!-- change to :value="option.name" when every option.name is different, otherwise it'll get a bug when checking checkboxes-->
                                <input type="checkbox" :value="option.name + ' ' + option.id"
                                       :id="option.id" class="option__checkbox" v-model="service_request.services"/>
                                <label :for="option.id" class="option__label">{{ option.name + ' ' + option.price
                                    }}</label>
                            </div>
                        </div>
                        <small class="note-message">*El precio mostrado es un aproximado, puede variar dependiendo del
                            proyecto</small>
                    </div>
                    <div class="hire-form__message">
                        <label class="d-none" for="message">Consulta</label>
                        <textarea v-model="service_request.description" id="message"
                                  placeholder="Cuentenos de su proyecto"></textarea>
                    </div>
                    <div class="hire-form__button">
                        <button class="u-button" :disabled="buttonDisabled" @click.prevent="submit">Cotizar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    // hire-us view component, provides an interface where the client is able to make a consultation for a centain service
    // 
    import {ServiceRequestService} from '../services/service_request';


    // @vuese
    export default {
        name: 'hire-us',

        data() {
            return {
                //Information that will be sent to the backend
                service_request: {
                    "first_name": undefined,
                    "last_name": undefined,
                    "email": undefined,
                    "description": undefined,
                    "telephone": undefined,
                    "files": [],
                    "services": []
                },
                // available options
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
            };
        },

        computed: {
            // returns true if any of the required inputs is empty, else returns false
            buttonDisabledByInputs() {
                return !this.service_request.first_name
                    || !this.service_request.last_name
                    || !this.service_request.telephone
                    || !this.service_request.email
                    || !this.service_request.description;
            },

            // button disabled based on buttonDisabledByInputs, this will be used to disabled cotizar button
            buttonDisabled() {
                return this.buttonDisabledByInputs;
            },
        },

        methods: {
            format_name(first_name, last_name) {
                this.service_request.name = `${first_name} ${last_name}`;
            },

            format_services(){
                let services = [];
                for(let service of this.service_request.services){
                    const formatted_service = {
                        "services": service
                    };
                    services.push();
                }
                this.service_request.services = services;
            },

            submit() {
                const api = new ServiceRequestService();

                this.format_name(this.service_request.first_name, this.service_request.last_name);

                this.format_services();

                api.postService(this.service_request).then((data) => {
                    console.log(data);
                }).catch(err => console.error(err));
            }
        }
    }
</script>