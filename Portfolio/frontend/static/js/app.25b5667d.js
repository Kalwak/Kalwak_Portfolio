(function(t){function e(e){for(var n,i,r=e[0],c=e[1],l=e[2],u=0,d=[];u<r.length;u++)i=r[u],Object.prototype.hasOwnProperty.call(s,i)&&s[i]&&d.push(s[i][0]),s[i]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);m&&m(e);while(d.length)d.shift()();return o.push.apply(o,l||[]),a()}function a(){for(var t,e=0;e<o.length;e++){for(var a=o[e],n=!0,i=1;i<a.length;i++){var c=a[i];0!==s[c]&&(n=!1)}n&&(o.splice(e--,1),t=r(r.s=a[0]))}return t}var n={},s={app:0},o=[];function i(t){return r.p+"static/js/"+({}[t]||t)+"."+{"chunk-07556c8a":"cec47260","chunk-08f9e24e":"221a02a3","chunk-113e4ac2":"f037ef8d","chunk-2d0ae5a4":"76be52d6","chunk-0a5d62ec":"a76b43f0","chunk-2cc30f6d":"a6f99ffa","chunk-45f40b0c":"52c6e225","chunk-2d0af2dd":"bd739cd4","chunk-2d0e5e97":"eb6c60a2","chunk-322bc55e":"4e16736d","chunk-51f77354":"b6028069","chunk-55a7b690":"2cd99fe7","chunk-6f08e1fa":"5530d0d2","chunk-808da5ba":"2e64038d"}[t]+".js"}function r(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.e=function(t){var e=[],a=s[t];if(0!==a)if(a)e.push(a[2]);else{var n=new Promise(function(e,n){a=s[t]=[e,n]});e.push(a[2]=n);var o,c=document.createElement("script");c.charset="utf-8",c.timeout=120,r.nc&&c.setAttribute("nonce",r.nc),c.src=i(t);var l=new Error;o=function(e){c.onerror=c.onload=null,clearTimeout(u);var a=s[t];if(0!==a){if(a){var n=e&&("load"===e.type?"missing":e.type),o=e&&e.target&&e.target.src;l.message="Loading chunk "+t+" failed.\n("+n+": "+o+")",l.name="ChunkLoadError",l.type=n,l.request=o,a[1](l)}s[t]=void 0}};var u=setTimeout(function(){o({type:"timeout",target:c})},12e4);c.onerror=c.onload=o,document.head.appendChild(c)}return Promise.all(e)},r.m=t,r.c=n,r.d=function(t,e,a){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},r.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)r.d(a,n,function(e){return t[e]}.bind(null,n));return a},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="/",r.oe=function(t){throw console.error(t),t};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],l=c.push.bind(c);c.push=e,c=c.slice();for(var u=0;u<c.length;u++)e(c[u]);var m=l;o.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"059b":function(t,e,a){t.exports=a.p+"static/img/close-icon.cb8fe3b1.png"},"0b80":function(t,e,a){t.exports=a.p+"static/img/refresh-icon.aaf96b9f.png"},"42d3":function(t,e,a){t.exports=a.p+"static/img/send-icon.85b481ac.png"},"55ee":function(t,e,a){t.exports=a.p+"static/img/chatbot-icon.6ef538e3.png"},"56d7":function(t,e,a){"use strict";a.r(e);a("cadf"),a("551c"),a("f751"),a("097d");var n=a("2b0e"),s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container-fluid",attrs:{id:"app"}},[a("page-header"),a("page-main"),a("page-footer")],1)},o=[],i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("header",{staticClass:"header row animated slideInDown fixed-top"},[n("div",{staticClass:"col-12"},[n("div",{staticClass:"inner-wrapper"},[n("div",{staticClass:"row justify-content-between align-items-center"},[n("div",{staticClass:"col-auto brand-column"},[n("div",{staticClass:"brand"},[n("h1",{staticClass:"brand__logo"},[n("router-link",{attrs:{to:"/",title:"kalwak"}},[n("img",{staticClass:"logo__image",attrs:{src:a("e347"),alt:"Wink logo",title:"Kalwak logo"}})])],1),n("button",{staticClass:"hamburger hamburger--squeeze menu-button",class:{"is-active":t.activatedMenu},attrs:{type:"button","aria-label":"menu-button"},on:{click:t.toggleMenu}},[t._m(0)])])]),n("nav-menu",{class:{activatedMenu:t.activatedMenu},on:{"close-nav-menu":function(e){t.activatedMenu=!1}}})],1)])])])},r=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"hamburger-box"},[a("span",{staticClass:"hamburger-inner"})])}],c=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("nav",{staticClass:"nav col-auto"},[a("div",{staticClass:"nav__item"},[t._m(0),a("div",{staticClass:"dropdown-list"},[a("div",{staticClass:"dropdown-list__item"},[a("router-link",{staticClass:"nav__link",attrs:{to:"/about-us"}},[t._v("¿Quiénes somos?")])],1),a("div",{staticClass:"dropdown-list__item"},[a("router-link",{staticClass:"nav__link",attrs:{to:"/projects/"+t.projectCategory}},[t._v("Trabajos anteriores")])],1)])]),a("div",{staticClass:"nav__item"},[a("router-link",{staticClass:"nav__link",attrs:{to:"/services/"+t.serviceCategory}},[t._v("Servicios")])],1),a("div",{staticClass:"nav__item"},[a("router-link",{staticClass:"nav__link",attrs:{to:"/hire-us"}},[t._v("Cotizar")])],1),a("div",{staticClass:"nav__item"},[a("a",{staticClass:"nav__link",attrs:{href:t.currentPath+"#contact-section"},on:{click:function(e){return t.$emit("close-nav-menu",!1)}}},[t._v("Contacto")])]),a("div",{staticClass:"nav__item"},[a("router-link",{staticClass:"nav__link",attrs:{to:"/blog"}},[t._v("Blog")])],1),t._m(1)])},l=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"nav__link nav__link--flex"},[t._v("Sobre nosotros"),a("span",{staticClass:"icon-down-open-mini"})])},function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"nav__item"},[n("div",{staticClass:"lang-switcher"},[n("img",{staticClass:"lang",attrs:{src:a("6b0d"),alt:"Spain flag",title:"spanish"}}),n("img",{staticClass:"lang",attrs:{src:a("e14f"),alt:"USA flag",title:"english"}})])])}],u=(a("28a5"),{name:"navigation-menu",computed:{projectCategory:function(){var t=this.$store.state.projects.projectsCategory;return t.length?t.split(" ").join("-"):"web-development"},serviceCategory:function(){return"web-development"},currentPath:function(){return this.$route.path}},watch:{currentPath:function(t,e){this.$emit("close-nav-menu",!1)}}}),m=u,d=a("2877"),p=Object(d["a"])(m,c,l,!1,null,null,null),f=p.exports,h={name:"page-header",data:function(){return{activatedMenu:!1}},components:{NavMenu:f},methods:{toggleMenu:function(){this.activatedMenu=!this.activatedMenu}}},g=h,b=Object(d["a"])(g,i,r,!1,null,null,null),v=b.exports,_=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("main",{staticClass:"main row"},[n("router-view"),n("div",{staticClass:"chatbot-main-container",class:{"chatbot-background":t.chatbotVisible},on:{click:function(e){t.chatbotVisible=!1}}},[t.chatbotVisible?n("chat-bot",{staticClass:"animated slideInUp",on:{"close-chatbot":function(e){t.chatbotVisible=!1}}}):t._e()],1),t.notEditorPath?n("img",{staticClass:"chatbot-open-icon",attrs:{src:a("55ee"),alt:"open chatbot",title:"open chatbot"},on:{click:function(e){t.chatbotVisible=!0}}}):t._e()],1)},C=[],k=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"chatbot-container",on:{click:function(t){t.stopPropagation()}}},[n("div",{staticClass:"chatbot__header"},[t._m(0),n("div",{staticClass:"chatbot__header-settings"},[n("span",{staticClass:"chatbot__setting-icon",attrs:{title:"borrar mensajes"},on:{click:t.clearMessages}},[n("img",{staticClass:"setting-icon__image",attrs:{src:a("0b80"),alt:"borrar mensajes"}})]),n("span",{staticClass:"chatbot__setting-icon",attrs:{title:"cerrar"},on:{click:t.closeChatbot}},[n("img",{staticClass:"setting-icon__image",attrs:{src:a("059b"),alt:"cerrar"}})])])]),n("div",{staticClass:"chatbot__body"},[n("div",{ref:"messages",staticClass:"chatbot-messages__container"},t._l(t.messages,function(e){return n("div",{key:e.id,staticClass:"message-container",class:{"bubble--right":"human"===e.type}},[n("p",{staticClass:"message__bubble animated fadeIn",class:{"orange--bubble":"bot"===e.type}},[n("span",{staticClass:"message__text",domProps:{innerHTML:t._s(e.text)}}),n("small",{staticClass:"message__information"},[t._v(t._s(e.time))])])])}),0),n("div",{staticClass:"chatbot-input__container"},[n("input",{directives:[{name:"model",rawName:"v-model",value:t.message,expression:"message"}],ref:"messageInput",staticClass:"input-text",attrs:{type:"text",placeholder:"Escriba aqui"},domProps:{value:t.message},on:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.pushMessage(t.fullMessage)},input:function(e){e.target.composing||(t.message=e.target.value)}}}),n("button",{staticClass:"send-button",attrs:{disabled:t.invalidInput},on:{click:function(e){return t.pushMessage(t.fullMessage)}}},[n("img",{attrs:{src:a("42d3"),alt:"send",title:"send message"}})])])])])},y=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("h5",{staticClass:"chatbot__header-title"},[n("img",{attrs:{src:a("e347"),width:"100px",title:"Kalwak",alt:"Kalwak logo"}})])}],w=a("7618"),j=a("bc3a"),S=a.n(j),x=a("1940"),M=a.n(x),P={name:"chat-bot",data:function(){return{messages:[],message:""}},computed:{fullMessage:function(){var t=(new Date).toLocaleTimeString();return t=this.getTimewithOutSeconds(t),{type:"human",text:this.message,time:t}},invalidInput:function(){return!this.message.trim().length},chatbotApi:function(){var t="",e="".concat(t,"/api/chatbot/");return e},userIp:function(){var t=this.$store.state.userIp;return t},currentPath:function(){return this.$route.path}},methods:{pushMessage:function(t){var e=arguments.length>1&&void 0!==arguments[1]&&arguments[1];e||(t.ip=this.userIp),this.invalidInput||(this.message="",this.PostMessageToChatbot({ip:t.ip,msg:t.text,current_vue_path:this.currentPath}),this.saveMessageToLocalStorage(t),this.loadMessagesFromLocalStorage(),this.$nextTick(function(){this.scrollBottom()}),this.focusInput())},closeChatbot:function(){this.$emit("close-chatbot")},scrollBottom:function(){var t=this.$refs.messages;t.scrollTop=t.scrollHeight},focusInput:function(){this.$refs.messageInput.focus()},clearMessages:function(){var t=JSON.parse(localStorage.getItem("_messages"));return"object"===Object(w["a"])(t)&&(!!t.messages&&(t.messages=[],localStorage.setItem("_messages",JSON.stringify(t)),void this.loadMessagesFromLocalStorage()))},getTimewithOutSeconds:function(t){if("string"!==typeof t)return"time string required";var e=t.split(" ")[1];return t=t.split(" "),t.splice(1,1),t=t.join(""),t=t.split(":"),t.splice(2,1),t=t.join(":"),"".concat(t," ").concat(e)},setChatbotResponseMessage:function(t){var e=this,a={type:"bot",text:t,time:this.getTimewithOutSeconds((new Date).toLocaleTimeString())};this.saveMessageToLocalStorage(a),this.loadMessagesFromLocalStorage(),this.$nextTick(function(){e.scrollBottom()})},PostMessageToChatbot:function(t){var e=this,a=this.chatbotApi;S.a.post(a,t).then(function(t){e.setChatbotResponseMessage(t.data)}).catch(function(t){console.error(t.response),M()({title:"Notificación",text:"Hubo un error, intente otra vez"})})},setMessagesLocalStorageItem:function(){localStorage.getItem("_messages")||localStorage.setItem("_messages",JSON.stringify({messages:[],lastMessage:""}))},saveMessageToLocalStorage:function(t){var e=JSON.parse(localStorage.getItem("_messages"));return"object"===Object(w["a"])(e)&&(!!("object"===Object(w["a"])(t)||t.text&&t.type&&t.time)&&(e.messages.push({type:t.type,text:t.text,time:t.time,id:e.messages.length+1}),void localStorage.setItem("_messages",JSON.stringify(e))))},loadLastMessageFromLocalStorage:function(){var t=JSON.parse(localStorage.getItem("_messages"));if("object"!==Object(w["a"])(t))return!1;this.message=t.lastMessage},saveLastMessageToLocalStorage:function(t){var e=JSON.parse(localStorage.getItem("_messages"));return"object"===Object(w["a"])(e)&&("string"===typeof t&&(e.lastMessage=t,void localStorage.setItem("_messages",JSON.stringify(e))))},loadMessagesFromLocalStorage:function(){var t=JSON.parse(localStorage.getItem("_messages"));return"object"===Object(w["a"])(t)&&(!!t.messages&&void(this.messages=t.messages))}},mounted:function(){var t=localStorage.getItem("_messages")&&0===JSON.parse(localStorage.getItem("_messages")).messages.length;t&&this.PostMessageToChatbot({ip:"127.0.0.1",msg:"Hello",current_vue_path:this.currentPath}),this.focusInput(),this.scrollBottom()},created:function(){this.setMessagesLocalStorageItem(),this.loadMessagesFromLocalStorage(),this.loadLastMessageFromLocalStorage()},beforeDestroy:function(){this.saveLastMessageToLocalStorage(this.message)}},I=P,O=Object(d["a"])(I,k,y,!1,null,null,null),E=O.exports,$={name:"page-main",data:function(){return{chatbotVisible:!1}},components:{ChatBot:E},computed:{notEditorPath:function(){return"/blog.editor"!==this.$route.path}},created:function(){this.$store.dispatch("getUserIp")},watch:{chatbotVisible:function(t){document.body.style.overflow=t?"hidden":""}}},T=$,N=Object(d["a"])(T,_,C,!1,null,null,null),L=N.exports,D=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("footer",{staticClass:"footer row",attrs:{id:"contact-section"}},[a("div",{staticClass:"col-12"},[a("div",{staticClass:"inner-wrapper"},["/blog.editor"!==t.currentPath?a("div",{staticClass:"contact-section"},[t.formDisabled?t._e():a("div",{staticClass:"contact-form"},[a("h4",{staticClass:"contact__title"},[t._v("Contáctanos")]),t.email.onSending?t._e():a("form",{staticClass:"form-row form animated fadeIn"},[a("div",{staticClass:"form-group col-12 form__input-container"},[a("label",{attrs:{for:"name"}},[t._v("Nombre")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.email.name,expression:"email.name"}],staticClass:"form-control form__input",attrs:{type:"text",placeholder:"Nombre",id:"name"},domProps:{value:t.email.name},on:{input:function(e){e.target.composing||t.$set(t.email,"name",e.target.value)}}}),a("small",{staticClass:"text-danger mt-1 mb-2 d-block",class:{visible:t.inputError,invisible:!t.inputError}},[t._v("*requerido")])]),a("div",{staticClass:"form-group col form__input-container"},[a("label",{attrs:{for:"phone"}},[t._v("Teléfono")]),a("input",{directives:[{name:"model",rawName:"v-model.number",value:t.email.phoneNumber,expression:"email.phoneNumber",modifiers:{number:!0}}],staticClass:"form-control form__input",attrs:{type:"tel",placeholder:"Teléfono",id:"phone"},domProps:{value:t.email.phoneNumber},on:{input:function(e){e.target.composing||t.$set(t.email,"phoneNumber",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),a("small",{staticClass:"text-danger mt-1 mb d-block invisible"},[t._v("*opcional")])]),a("div",{staticClass:"form-group col form__input-container"},[a("label",{attrs:{for:"email"}},[t._v("Email")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.email.address,expression:"email.address"}],staticClass:"form-control form__input",attrs:{type:"email",placeholder:"E-mail",id:"email"},domProps:{value:t.email.address},on:{input:function(e){e.target.composing||t.$set(t.email,"address",e.target.value)}}}),a("small",{staticClass:"text-danger mt-1 mb-2 d-block",class:{visible:t.inputError,invisible:!t.inputError}},[t._v("*requerido")])]),a("div",{staticClass:"form-group col-12 form__input-container"},[a("label",{attrs:{for:"message"}},[t._v("Consulta")]),a("textarea",{directives:[{name:"model",rawName:"v-model",value:t.email.message,expression:"email.message"}],staticClass:"form-control form__input form__textarea",attrs:{placeholder:"Consulta",id:"message"},domProps:{value:t.email.message},on:{input:function(e){e.target.composing||t.$set(t.email,"message",e.target.value)}}}),a("small",{staticClass:"text-danger mt-1 mb-2 d-block",class:{visible:t.inputError,invisible:!t.inputError}},[t._v("*requerido")])]),a("div",{staticClass:"form-group col-12 form__button-container"},[a("button",{staticClass:"form__button",attrs:{disabled:t.buttonDisabled},on:{click:function(e){return e.preventDefault(),t.sendEmail(e)}}},[t._v("Enviar")])])]),t.email.onSending?a("div",{staticClass:"spinner"},[a("div",{staticClass:"rect1"}),a("div",{staticClass:"rect2"}),a("div",{staticClass:"rect3"}),a("div",{staticClass:"rect4"}),a("div",{staticClass:"rect5"})]):t._e()]),a("div",{staticClass:"contact-information",class:{"information-50":t.formDisabled}},[t._m(0),t._m(1)])]):t._e(),t._m(2)])])])},J=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"contact-info-container"},[a("h4",{staticClass:"contact__title"},[t._v("Más información")]),a("p",{staticClass:"contact-info"},[a("span",{staticClass:"info__title"},[t._v("Teléfono:")]),a("span",{staticClass:"info__description"},[a("a",{attrs:{href:"tel:+50684599023",title:"telefono"}},[t._v("+50684599023")])])]),a("p",{staticClass:"contact-info"},[a("span",{staticClass:"info__title"},[t._v("Correo:")]),a("span",{staticClass:"info__description"},[a("a",{attrs:{href:"mailto:kalwakcr@gmail.com",target:"_blank",title:"correo kalwak"}},[t._v("kalwakcr@gmail.com")])])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"social-media"},[a("h4",{staticClass:"contact__title"},[t._v("Nuestras redes")]),a("a",{staticClass:"social-media__icon icon-facebook social-media__icon",attrs:{href:"https://www.facebook.com/Kalwak-358576961719203",target:"_blank",rel:"noopener",title:"facebook"}}),a("a",{staticClass:"social-media__icon icon-whatsapp social-media__icon",attrs:{href:"tel:+50684599023",title:"whatsapp"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"information-section"},[a("div",{staticClass:"copyright-section"},[a("p",[t._v("Copyright© - 2019 Kalwak Derechos Reservados")]),a("p",[t._v("Desarrollo web y de software www.kalwak.xyz")])])])}],B=(a("ac6a"),a("456d"),a("96cf"),a("3b8d")),F=(a("7f7f"),{name:"page-footer",data:function(){return{email:{subject:"CONTACTO KALWAK",name:"",phoneNumber:"",address:"",message:"",onSending:!1,inputError:!1},formDisabled:!1,inputError:!1}},computed:{apiEndpoint:function(){return""},apiEmail:function(){return"".concat(this.apiEndpoint,"/api/send_email/")},fullMessage:function(){var t=this.email;return"\n      nombre: ".concat(t.name,"\n\n      telefono: ").concat(t.phoneNumber||"no fue dado!","\n\n      ").concat(t.message,"\n      ")},buttonDisabledByProcess:function(){return this.email.onSending},buttonDisabledByInputs:function(){return!this.email.name||!this.email.address||!this.email.message},buttonDisabled:function(){return this.buttonDisabledByProcess},emailInfo:function(){var t=this.email,e=t.name,a=t.address,n=t.message;return{name:e,address:a,message:n}},currentPath:function(){return this.$route.path}},methods:{sendEmail:function(){var t=Object(B["a"])(regeneratorRuntime.mark(function t(){var e,a,n;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:e=this,a=e.checkFields(e.emailInfo),a.valid?(e.email.onSending=!0,n={subject:e.email.subject,email:e.email.address,message:e.fullMessage},S.a.post(e.apiEmail,n).then(function(t){"OK"===t.request.statusText&&1===t.data.response?(M()({title:"Notificación",text:"Su mensaje ha sido enviado",icon:"success"}),e.clearInputs()):M()({title:"Notificación",text:t.data.email[0],icon:"warning"})}).catch(function(t){M()({title:"Notificación",text:"Hubo un error, intente otra vez",icon:"error"})}).finally(function(){e.email.onSending=!1})):e.inputError=!0;case 3:case"end":return t.stop()}},t,this)}));function e(){return t.apply(this,arguments)}return e}(),checkFields:function(t){for(var e=!0,a=Object.keys(t),n=0;n<a.length;n++){var s=t[a[n]];s.length<1&&(e=!1)}return{valid:e}},clearInputs:function(){var t=this.email;t.name="",t.address="",t.message="",t.phoneNumber=""}},watch:{currentPath:function(){this.inputError=!1,"/hire-us"===this.currentPath?this.formDisabled=!0:this.formDisabled=!1}}}),A=F,q=Object(d["a"])(A,D,J,!1,null,null,null),K=q.exports,U={name:"app",components:{PageHeader:v,PageMain:L,PageFooter:K}},V=U,H=Object(d["a"])(V,s,o,!1,null,null,null),R=H.exports,z=a("8c4f");n["a"].use(z["a"]);var Q=new z["a"]({mode:"history",base:"/",scrollBehavior:function(){return{x:0,y:0}},routes:[{path:"/",name:"home",component:function(){return Promise.all([a.e("chunk-2d0ae5a4"),a.e("chunk-2cc30f6d")]).then(a.bind(null,"bb51"))}},{path:"/projects",name:"projects",component:function(){return a.e("chunk-322bc55e").then(a.bind(null,"acca"))},children:[{path:":category",name:"category",component:function(){return Promise.all([a.e("chunk-2d0ae5a4"),a.e("chunk-45f40b0c")]).then(a.bind(null,"aff8"))}}]},{path:"/about-us",name:"about-us",component:function(){return a.e("chunk-6f08e1fa").then(a.bind(null,"2664"))}},{path:"/services",name:"services",component:function(){return a.e("chunk-55a7b690").then(a.bind(null,"f23e"))},children:[{path:":service",component:function(){return Promise.all([a.e("chunk-2d0ae5a4"),a.e("chunk-0a5d62ec")]).then(a.bind(null,"8524"))}}]},{path:"/hire-us",name:"hire us",component:function(){return a.e("chunk-07556c8a").then(a.bind(null,"5977"))}},{path:"/blog",component:function(){return a.e("chunk-808da5ba").then(a.bind(null,"fd3f"))},children:[{path:"",name:"blog",component:function(){return a.e("chunk-2d0af2dd").then(a.bind(null,"0ce9"))}},{path:":category/(page/)?:number(\\d+)?",name:"blog list",component:function(){return a.e("chunk-51f77354").then(a.bind(null,"27c4"))}},{path:":category/post/:id(\\d+)",nane:"article",component:function(){return a.e("chunk-113e4ac2").then(a.bind(null,"0e1b"))}}]},{path:"*",redirect:"/not-found"},{path:"/not-found",name:"not found",component:function(){return a.e("chunk-2d0e5e97").then(a.bind(null,"9703"))}},{path:"/blog.editor",name:"blog editor",component:function(){return a.e("chunk-08f9e24e").then(a.bind(null,"09bd"))}}]}),W=a("2f62");n["a"].use(W["a"]);var X=new W["a"].Store({state:{projectsInformation:[],projects:{projectsCategory:"",projects:[],currentProject:{},currentProjectId:0},userIp:"",onSearching:!1,searchText:"",filter:{year:"",month:""}},mutations:{setCategory:function(t,e){return t.projects.projectsCategory=e},setProjects:function(t,e){return t.projects.projects=e},setCurrentProject:function(t,e){return t.projects.currentProject=e},setAllProjects:function(t,e){return t.projectsInformation=e},setUserIp:function(t,e){return t.userIp=e},setOnSearching:function(t,e){return t.onSearching=e},setSearchText:function(t,e){return t.searchText=e},setYear:function(t,e){return t.filter.year=e},setMonth:function(t,e){return t.filter.month=e}},actions:{setProjectsByCategory:function(t){var e=t.commit,a=t.state,n=a.projects.projectsCategory,s=[],o=a.projectsInformation;o.forEach(function(t){t.categories.indexOf(n)>-1&&(t.pageId=s.length+1,s.push(t))}),s&&e("setProjects",s)},getUserIp:function(t){var e=t.commit,a="".concat("","/api/get-ip/");S.a.get(a).then(function(t){var a=t.data.ip;e("setUserIp",a)}).catch(function(t){console.error(t)})}},getters:{numberOfProjects:function(t){return t.projects.projects.length}}}),Y=a("85ff"),G=a.n(Y);a("5720"),a("a0d8");n["a"].use(a("2b27"));var Z=!0;n["a"].use(G.a,{isEnabled:!0,logLevel:Z?"error":"debug",stringifyArguments:!1,showMethodName:!0,separator:"|",showConsoleColors:!0,showLogLevel:!0}),n["a"].config.productionTip=!1,n["a"].prototype.$axios=S.a,new n["a"]({router:Q,store:X,render:function(t){return t(R)}}).$mount("#app"),window.$=window.jQuery=a("1157");var tt=window.$cookies.get("csrftoken");S.a.defaults.headers.common["X-CSRFToken"]=tt},"6b0d":function(t,e,a){t.exports=a.p+"static/img/spanish-lang.6b7f4fbd.svg"},a0d8:function(t,e,a){},e14f:function(t,e,a){t.exports=a.p+"static/img/english-lang.cbfe8d83.svg"},e347:function(t,e,a){t.exports=a.p+"static/img/logo.b33b1b46.svg"}});
//# sourceMappingURL=app.25b5667d.js.map