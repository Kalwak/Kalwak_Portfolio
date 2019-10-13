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
                <form id="service-form" class="hire-form" action="http://localhost:8000/api/service_request/" method="post" enctype="multipart/form-data">
                    <div class="hire-form__inputs">
                        <label for="fName">Nombre</label>
                        <input type="text" class="hire-form__input" id="fName" v-model="service_request.first_name"
                               placeholder="Nombre" name="name"/>
                        <label for="lName">Apellido</label>
                        <input type="text" class="hire-form__input" id="lName" v-model="service_request.last_name"
                               placeholder="Apellido" name="lastname"/>
                        <label for="phone">Teléfono</label>
                        <input type="tel" class="hire-form__input" id="phone" v-model="service_request.telephone"
                               placeholder="Teléfono" name="telephone"/>
                        <label for="email">E-mail</label>
                        <input type="email" class="hire-form__input" id="email" name="email" v-model="service_request.email"
                               placeholder="E-mail"/>
                    </div>
                    <div class="service-picker">
                        <h4 class="service-picker__title">Servicio a consultar</h4>
                        <div class="service-picker__options">
                            <div v-for="(option, idx) in options" class="service-picker__option" :key="idx">
                                <!-- change to :value="option.name" when every option.name is different, otherwise it'll get a bug when checking checkboxes-->
                                <input type="checkbox" :value="option.name + ' ' + option.id"
                                       :id="option.id" class="option__checkbox" v-model="service_request.services" name="services"/>
                                <label :for="option.id" class="option__label">{{ option.name + ' ' + option.price
                                    }}</label>
                            </div>
                        </div>
                        <small class="note-message">*El precio mostrado es un aproximado, puede variar dependiendo del
                            proyecto</small>
                    </div>
                    <div class="hire-form__message">
                        <label for="message">Consulta</label>
                        <textarea v-model="service_request.description" id="message" placeholder="Cuentenos de su proyecto" name="description"></textarea>
                    </div>
                    <div class="hire-form__files">
                        <input type="file" id="inputFile" class="files__input" lang="es" multiple @change="getUserFiles($event)" name="files"/>
                        <label for="inputFile" class="files__label">Adjuntar archivos</label>
                        <span class="files__output-label">Numero de archivos {{ numberOfSelectedFiles }}</span>
                        <small class="text-muted w-100 text-center my-2 text-uppercase">Tamaño maximo de archivos hasta 10MB</small>
                    </div>
                    <div class="hire-form__button">
                        <button class="u-button" :disabled="buttonDisabled" type="submit">Cotizar</button>
                    </div>
                    <input id="csrftoken" type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrftoken">
                </form>
            </div>
        </div>
    </div>



</template>

<script>
// hire-us view component, provides an interface where the client is able to make a consultation for a centain service
import swal from 'sweetalert';


// @vuese
export default {
  name: 'hire-us',
  data() {
            return {
                csrftoken : $cookies.get('csrftoken'),
                /* Saves a list of errors gathered from the url queries
                 Sample list:
                 [
                    {
                        telephone: [
                            "Telephone format is incorrect"
                        ]
                    }
                 ]
                */
                errors: [

                ],

                //Form info
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
    numberOfSelectedFiles() {
      let numberOfFiles = this.service_request.files.length;
      return numberOfFiles;
    },
    totalFilesSize() {
      let totalSize = 0;
      let files = this.service_request.files;
      if (files.length) {
        for (let i = 0; i < files.length; i++) {
        let file = files[i];
        totalSize += file.size;
        };
        return totalSize;
      };

      return 0;
    },
  },
  mounted: function () {
    this.process_query_params();
    this.handleErrorsFromData();
  },
  methods: {
    // @vuese 
    // used to get files from file input and then store in the service_request object
    // @arg event, representing event object provided by change event
    getUserFiles(event) {
      let files = event.target.files;
      let clearFiles = [];
      let limitSizeError = false;
      let totalSize = this.totalFilesSize;
      let errorMessage = 'Los siguientes archivos no se enviaran porque\n con ellos se supera el limite de 10MB\n';
      for (let i = 0; i < files.length; i++) {
        let file = files.item(i);
        totalSize += file.size;
        if (totalSize < 10000000) {
          clearFiles.push(file);
        } else {
          limitSizeError = true;
          errorMessage += file.name + '\n';
        };
      };

      if (limitSizeError) swal({
        title: 'Notificación',
        text: errorMessage,
        icon: 'warning',
        button: {
            text: 'Salir',
        },
      });

      this.service_request.files = this.service_request.files.concat(clearFiles);
      event.target.type = 'text';
      event.target.type = 'file';
    },

    // @vuese
    // Saves the errors gathered from the url queries to the this.errors array if no query in url, then nothing is done
    process_query_params(){
      let urlParams = new URLSearchParams(window.location.search);
      let query = urlParams.get("errors");
      if(query){
          query = query.replace(/'/g, '"'); //Replace is needed since JSON standards don't parse the ' correctly
          let json_query = JSON.parse(query);
          this.errors.push(json_query);
      }
      return this.errors; // Done for unittesting
    },

    // @vuese
    // handle the errors array from the data property
    // shows alerts if any error when submitting form
    handleErrorsFromData() {
      let errors = this.errors;
      let errorMessage = '';
      if (this.errors.length > 0) {
          errors.forEach( error => {
            let errorLabels = Object.keys(error);
            errorLabels.forEach( label => {
              if (label === 'email') errorMessage += 'Ingrese un email valido\n';
              if (label === 'telephone') errorMessage += 'Ingrese un numero de teléfono valido\n';
            });
          });

          swal({
            title: 'Notificación',
            text: errorMessage,
            icon: 'error',
          });
      };
    },
  },
};
</script>