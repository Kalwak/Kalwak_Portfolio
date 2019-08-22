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
  <footer class="footer row">
    <div class="col-12">
      <div class="inner-wrapper">
        <div class="contact-section" id="contact-section">
          <div class="contact-form">
            <h4 class="contact__title">Contáctanos</h4>
            <div class="form-row form">
              <div class="form-group col-12 form__input-container">
                <label for="name" class="d-none">Nombre</label>
                <input type="text" placeholder="Nombre" class="form-control form__input" id="name" v-model="email.name" />
                <small class="text-danger mt-1 mb-3 d-block">*requerido</small>
              </div>
              <div class="form-group col form__input-container">
                <label for="phone" class="d-none">Teléfono</label>
                <input type="tel" placeholder="Telefono" class="form-control form__input" id="phone" v-model="email.phoneNumber" />
                <small class="text-danger mt-1 mb-3 d-block" style="visibility: hidden;">*requerido</small>
              </div>
              <div class="form-group col form__input-container">
                <label for="email" class="d-none">Email</label>
                <input type="email" placeholder="E-mail" class="form-control form__input" id="email" v-model="email.address" />
                <small class="text-danger mt-1 mb-3 d-block">*requerido</small>
              </div>
              <div class="form-group col-12 form__input-container">
                <label for="message" class="d-none">Consulta</label>
                <textarea placeholder="Consulta" class="form-control form__input form__textarea" id="message" v-model="email.message"></textarea>
                <small class="text-danger mt-1 mb-3 d-block">*requerido</small>
              </div>
              <div class="form-group col-12 form__button-container">
                <button class="form__button" @click="sendEmail" :disabled="buttonDisabled">Enviar</button>
              </div>
            </div>
          </div>
          <div class="contact-information">
            <h4 class="contact__title">Más información</h4>
            <p class="contact-info">
              <span class="info__title">teléfono:</span>
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
            <div class="social-media">
              <h4 class="contact__title">Nuestras redes</h4>
              <a href="https://www.facebook.com/Kalwak-358576961719203" target="_blank" class="social-media__icon icon-facebook social-media__icon" title="facebook"></a>
              <a href="tel:+50684599023" target="_blank" class="social-media__icon icon-whatsapp social-media__icon" title="whatsapp"></a>
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
// page footer component
import axios from 'axios';


// @vuese
export default {
  name: 'page-footer',

  data() {
    return {
      email: {
        subject: 'contactanos-sitio-web',
        name: '',
        phoneNumber: '',
        address: '',
        message: '',
        onSending: false,
        inputError: false,
      },
    };
  },

  computed: {
    // base api endpoint
    apiEndpoint() {
      return process.env.VUE_APP_API_ENDPOINT;
    },

    // endpoint where email will be posted
    apiEmail() {
      return `${this.apiEndpoint}/api/send_email`;
    },

    fullMessage() {
      const email = this.email;
      return `
      nombre: ${ email.name }\n
      telefono: ${ email.phoneNumber || 'no fue dado!' }\n
      ======================================================
      consulta:\n
      ${ email.message }
      `;
    },

    // disable send button whereas email is onSending or inputError
    buttonDisabledByProcess() {
      return this.email.onSending;
    },

    buttonDisabledByInputs() {
      return !this.email.name 
      || !this.email.address 
      || !this.email.message;
    },

    buttonDisabled() {
      return this.buttonDisabledByProcess || this.buttonDisabledByInputs;
    },

    emailInfo() {
      const { name, address, message } = this.email;
      return  {
        name,
        address,
        message
      }
    },
  },

  methods: {
    sendEmail() {
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
        // fetch('http://localhost:8000/api/send_email', {
        //   method: 'POST',
        //   headers: {
        //   'Content-Type': 'application/json',
        //   // 'Content-Type': 'application/x-www-form-urlencoded'
        //   },
        //   body: JSON.stringify({
        //   subject: 'warning',
        //   email: 'someemail@email.com',
        //   message: 'some message'
        // }),
        // })
        axios.post('http://localhost:8000/api/send_email', {
          subject: 'some subject',
          email: 'someemail@email.com',
          message: 'Hi there!!',
        })
          .then(res => {
            console.log(res);
          })
          .catch(err => {
            console.log(err);
          });
      }
    },

    // check if fields are not empty
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
  },
}
</script>
