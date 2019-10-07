<!--
  PAGE FOOTER
  structure of this section:
    - footer 
      - contact-section
        - contact-form // form to make consults 
        - contact-information // general information about kalwak 
          like: email, phone number, facebook page and whatsapp number
        - information-section
        - copyright-section // some commom copyright message
-->

<template>
  <footer class="footer row" id="contact-section">
    <div class="col-12">
      <div class="inner-wrapper">
        <div class="contact-section" v-if="currentPath !== '/blog.editor'">
          <div class="contact-form" v-if="!formDisabled">
            <h4 class="contact__title">Contáctanos</h4>
            <form class="form-row form animated fadeIn"  v-if="!email.onSending">
              <div class="form-group col-12 form__input-container">
                <label for="name" class="d-none">Nombre</label>
                <input type="text" placeholder="Nombre" class="form-control form__input" id="name" v-model="email.name" />
                <small class="text-danger mt-1 mb-2 d-block" :class="{ visible: inputError, invisible: !inputError }">*requerido</small>
              </div>
              <div class="form-group col form__input-container">
                <label for="phone" class="d-none">Teléfono</label>
                <input type="tel" placeholder="Teléfono" class="form-control form__input" id="phone" v-model.number="email.phoneNumber" />
                <small class="text-danger mt-1 mb d-block invisible">*opcional</small>
              </div>
              <div class="form-group col form__input-container">
                <label for="email" class="d-none">Email</label>
                <input type="email" placeholder="E-mail" class="form-control form__input" id="email" v-model="email.address" />
                <small class="text-danger mt-1 mb-2 d-block" :class="{ visible: inputError, invisible: !inputError }">*requerido</small>
              </div>
              <div class="form-group col-12 form__input-container">
                <label for="message" class="d-none">Consulta</label>
                <textarea placeholder="Consulta" class="form-control form__input form__textarea" id="message" v-model="email.message"></textarea>
                <small class="text-danger mt-1 mb-2 d-block" :class="{ visible: inputError, invisible: !inputError }">*requerido</small>
              </div>
              <div class="form-group col-12 form__button-container">
                <button class="form__button" @click.prevent="sendEmail" :disabled="buttonDisabled">Enviar</button>
              </div>
            </form>
            <div class="spinner" v-if="email.onSending">
              <div class="rect1"></div>
              <div class="rect2"></div>
              <div class="rect3"></div>
              <div class="rect4"></div>
              <div class="rect5"></div>
            </div>
          </div>
          <div class="contact-information" :class="{ 'information-50': formDisabled }">
            <div class="contact-info-container">
              <h4 class="contact__title">Más información</h4>
              <p class="contact-info">
                <span class="info__title">Teléfono:</span>
                <span class="info__description">
                  <a href="tel:+50684599023" title="telefono">+50684599023</a>
                </span>
              </p>
              <p class="contact-info">
                <span class="info__title">Correo:</span>
                <span class="info__description">
                  <a href="mailto:kalwakcr@gmail.com" target="_blank" title="correo kalwak">kalwakcr@gmail.com</a>
                </span>
              </p>
            </div>
            <div class="social-media">
              <h4 class="contact__title">Nuestras redes</h4>
              <a href="https://www.facebook.com/Kalwak-358576961719203" target="_blank" class="social-media__icon icon-facebook social-media__icon" title="facebook"></a>
              <a href="tel:+50684599023" class="social-media__icon icon-whatsapp social-media__icon" title="whatsapp"></a>
            </div>
          </div>
        </div>
        <div class="information-section">
          <div class="copyright-section">
            <p>Copyright&copy; - 2019 Kalwak Derechos Reservados</p>
            <p>Desarrollo web y de software www.kalwak.xyz</p>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
// page footer component, this is the app footer section, in this section we have the contact form and contact information
// also some copyright messages
import axios from 'axios';
import swal from 'sweetalert';


// @vuese
export default {
  name: 'page-footer',

  data() {
    return {
      // email is an object containing properties for email information like name, address etc...
      email: {
        subject: 'CONTACTO KALWAK',
        name: '',
        phoneNumber: '',
        address: '',
        message: '',
        onSending: false,
        inputError: false,
      },
      formDisabled: false,

      // if click send button and required fields are empty, this will set to true
      // and warnings about that the fields are required will be showned
      inputError: false,
    };
  },

  computed: {
    // base api endpoint 
    apiEndpoint() {
      return process.env.VUE_APP_API_ENDPOINT;
    },

    // endpoint where email will be posted
    apiEmail() {
      return `${this.apiEndpoint}/api/send_email/`;
    },

    // full message where name, phone and message will be included
    fullMessage() {
      const email = this.email;
      return `
      nombre: ${ email.name }\n
      telefono: ${ email.phoneNumber || 'no fue dado!' }\n
      ${ email.message }
      `;
    },

    // disable send button whereas email is onSending
    buttonDisabledByProcess() {
      return this.email.onSending;
    },

    // returns true if any of the required inputs is empty, else returns false
    buttonDisabledByInputs() {
      return !this.email.name 
      || !this.email.address 
      || !this.email.message;
    },

    // returns true if buttonDisabledByProcess is true, else returns false
    buttonDisabled() {
      return this.buttonDisabledByProcess;
    },

    // returns an object with the three required properties from email
    emailInfo() {
      const { name, address, message } = this.email;
      return  {
        name,
        address,
        message
      }
    },

    // returns current $route.path
    currentPath() {
      return this.$route.path;
    },
  },

  methods: {
    // @vuese
    // sendEmail method, this method is triggered by the Enviar button which is only
    // enabled if required inputs are not empty, in this method axios is used to make http post request
    // to api/send_email endpoint (django backend service)
    async sendEmail() {
      const self = this;
      let validation = self.checkFields(self.emailInfo);
      if (validation.valid) {
        self.email.onSending = true;

        // posting email to api service
        let data = {
          subject: self.email.subject,
          email: self.email.address,
          message: self.fullMessage,
        };
        axios.post(self.apiEmail, data)
          .then(res => {
            if (res.request.statusText === 'OK' && res.data.response === 1) {
              swal({
                title: 'Notificación',
                text: 'Su mensaje ha sido enviado',
                icon: 'success',
              });
              self.clearInputs();
            } else {
              swal({
                title: 'Notificación',
                text: res.data.email[0],
                icon: 'warning',
              });
            }
          })
          .catch(err => {
            swal({
              title: 'Notificación',
              text: 'Hubo un error, intente otra vez',
              icon: 'error',
            });
          })
          .finally(() => {
            self.email.onSending = false;
          });
      } else {
        self.inputError = true;
      }
    },

    // @vuese
    // check if fields are not empty, 
    // it's used to check if required inputs are not empty, this method is used in sendEmail method
    // @arg filds which is an object contain actually any fields
    checkFields(fields) {
      let validFields = true;
      let fieldsKeys = Object.keys(fields);
      // idx = index
      for (let idx = 0; idx < fieldsKeys.length; idx++) {
        let fieldValue = fields[fieldsKeys[idx]];
        if (fieldValue.length < 1) {
          validFields = false;
        }
      }

      return {
        valid: validFields,
      };
    },

    // @vuese
    // clear email property values like name, email, phoneNumber and message which are the ones showned in the contact form
    clearInputs() {
      let email = this.email;
      email.name = '';
      email.address = '';
      email.message = '';
      email.phoneNumber = '';
    },
  },

  watch: {
    // watcher for currenthPath computed property, used to hide contact form
    // callback function, check if current path is equal to /hire-us,
    // if true, set data property formDisabled to true, else set it to false
    currentPath() {
      this.inputError = false;
      if (this.currentPath === '/hire-us') {
        this.formDisabled = true;
      } else {
        this.formDisabled = false;
      }
    },
  },
}
</script>
