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
                <input type="text" placeholder="Nombre" class="form-control form__input" id="name" />
              </div>
              <div class="form-group col form__input-container">
                <label for="phone" class="d-none">Telefono</label>
                <input type="tel" placeholder="Telefono" class="form-control form__input" id="phone" />
              </div>
              <div class="form-group col form__input-container">
                <label for="email" class="d-none">Email</label>
                <input type="email" placeholder="E-mail" class="form-control form__input" id="email" />
              </div>
              <div class="form-group col-12 form__input-container">
                <label for="message" class="d-none">Consulta</label>
                <textarea placeholder="Consulta" class="form-control form__input form__textarea" id="message"></textarea>
              </div>
              <div class="form-group col-12 form__button-container">
                <button class="form__button">Enviar</button>
              </div>
            </div>
          </div>
          <div class="contact-information">
            <h4 class="contact__title">Mas información</h4>
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