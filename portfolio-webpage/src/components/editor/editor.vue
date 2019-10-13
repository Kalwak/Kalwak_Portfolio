<template>
  <div class="editor-container">
    <header class="editor__header">
      <h2 class="editor-title">Editor Kalwak</h2>
    </header>
    <div class="editor__body">
      <div class="editor-page">
        <input class="post-main__title" placeholder="Titulo" v-model="post.title" />
        <div id="editor-holder"></div>
      </div>
      <div class="editor-settings">
        <div class="editor-toolbar">
          <span class="toolbar__item" @click="execCommand('undo')">
            <img src="@/assets/images/editor-icons/anterior.png" alt="Anterior" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator" @click="execCommand('redo')">
            <img src="@/assets/images/editor-icons/siguiente.png" alt="Siguiente" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/more.png" alt="Mas" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/less.png" alt="Menos" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item" @click="execCommand('bold')">
            <img src="@/assets/images/editor-icons/bold.png" alt="Negrita" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item" @click="execCommand('italic')">
            <img src="@/assets/images/editor-icons/italic.png" alt="Italica" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator" @click="execCommand('underline')">
            <img src="@/assets/images/editor-icons/underline.png" alt="Delineado" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item" @click="addList('ordered')">
            <img src="@/assets/images/editor-icons/ol.png" alt="Ordernada" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator" @click="addList('unordered')">
            <img src="@/assets/images/editor-icons/ul.png" alt="Desordenada" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item" @click="execCommand('paste')">
            <img src="@/assets/images/editor-icons/paste.png" alt="Pegar" class="toolbar__item-icon" />
          </span>
          <div class="w-100"></div>
          <span class="toolbar__item toolbar__item--separator" @click="addImage">
            <img src="@/assets/images/editor-icons/image.png" alt="Imagen" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/video.png" alt="Video" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/left.png" alt="Izquierda" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/center.png" alt="Centrar" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/preview.png" alt="Vista previa" class="toolbar__item-icon" />
          </span>
        </div>
        <div class="editor-information-picker">
          <select-filter :options="categories" default-option="development" label="Categoria" class="post-category" @getOption="getTag" />
          <select-filter :options="authors" default-option="Joseph" label="Autor" class="post-category" @getOption="getAuthor" />
        </div>
      </div>

      <div class="saving-tools">
        <label for="thumbnail" class="mr-2 p-3 rounded text-white" :class="{ 'bg-success': post.thumbnail, 'bg-danger': !post.thumbnail }">
          {{ !post.thumbnail ? 'Seleciona imagen thumbnail' : post.thumbnail.name }}
          <input type="file" class="form-control-file" @change="getThumbnail" id="thumbnail" />
        </label>
        <button class="u-button" @click="submitPost" :disabled="onLoading">Crear</button>
      </div>
    </div>
    <div 
    v-if="onLoading"
      class="d-flex justify-content-center align-self-center bg-danger w-100" style="z-index: 10; position: absolute; margin-top: -300px">
      <div class="spinner">
        <div class="rect1"></div>
        <div class="rect2"></div>
        <div class="rect3"></div>
        <div class="rect4"></div>
        <div class="rect5"></div>
      </div>
    </div>
  </div>
</template>

<script>
// editor component for the creation of post for the blog section
import EditorJS from '@editorjs/editorjs';
import editorConfig from './editor.config';
import SelectFilter from '../sub-layout/select-filter';
import swal from 'sweetalert';
import axios from 'axios';


// @vuese
export default {
  name: 'post-editor',
  data() {
    return {
      categories: [
        'development',
        'social',
        'startup',
        'security',
        'design',
      ],
      authors: [
        'Jose',
        'Joseph',
        'Ricardo',
        'Edwin',
        'Jennifer',
      ],
      editorIsReady: false,
      onLoading: false,
      editorData: {},
      post: {
        title: '',
        author: '',
        tag: '',
        thumbnail: null,
      },
    };
  },

  components: {
    SelectFilter,
  },

  computed: {
    postUrl() {
      return `${process.env.VUE_APP_API_ENDPOINT}/api/blog/`
    },
  },

  methods: {
    // @vuese
    // wrapper method for calling document.execCommand(command)
    // @arg command a valid command to execute, like copy, undo, redo, etc...
    execCommand(command) {
      this.$log.debug(command);
      document.execCommand(command);
    },

    // @vuese
    // init editorJS instance and set the returned editorJS instance in window.editor
    // also checks if editor is ready by calling isReady and set editorIsReady to true if is ready
    initEditor() {
      this.$log.debug(this.editorData);
      window.editor = new EditorJS({ ...editorConfig, data: this.editorData });
      window.editor.isReady
        .then(() => {
          this.editorIsReady = true;
        });
    },

    // @vuese
    // insert editor new list block
    // @arg type is a list type, ordered or unordered
    addList(type) {
      this.$log.debug(type);
      let editor = window.editor;
      editor.blocks.insert('list', {
        style: type === 'ordered' ? type : 'unordered'
      });
    },

    // @vuese
    // insert new editor image block
    addImage() {
      let editor = window.editor;
      editor.blocks.insert('image');
    },

    // @vuese
    // get Editor data and set it to component editorData, then call saveDataToLocalStorage
    // to save editorData to localStorage
    getData() {
      return new Promise((resolve, reject) => {
        window.editor.save()
          .then( data => {
            resolve(data);
          })
          .catch( error => {
            reject(error)
          })
      });
    },

    // @vuese
    // save editor data to localStorage, but check if data.blocks has something in it, if it's empty
    // returns false and no data is saved
    saveDataToLocalStorage(editorData) {
      this.$log.debug(editorData);
      if (editorData.blocks && editorData.blocks.length === 0) return false;
      localStorage.setItem('_editor-data', JSON.stringify(editorData));

    },

    // @vuese
    // load the editorData from the localStorage and check if it's valid, then set value to
    // component editorData, else if it's not valid return false
    loadDataFromLocalStorage() {
      let editorData = JSON.parse(localStorage.getItem('_editor-data'));
      this.$log.debug(editorData);
      if (!editorData) return false;
      this.editorData = editorData;
    },

    // @vuese
    clearEditorData() {
      localStorage.setItem('_editor-data', JSON.stringify({}));
      this.editorData = {};
      this.post.title = '';
      this.post.thumbnail = '';
      window.editor.destroy();
      this.initEditor();
    },

    // @vuese
    // handler method to get the tag from select-filter @getOption event
    // @arg tag value from the @getOption payload
    getTag(tag) {
      this.$log.debug(tag);
      this.post.tag = tag;
    },

    // @vuese
    // handler method to get the author from select-filter @getOption event
    // @arg author value from the @getOption payload
    getAuthor(author) {
      this.$log.debug(author);
      this.post.author = author;
    },

    // @vuese
    // handler for @change event for input to get the thumbnail image
    // @arg event object
    getThumbnail(event) {
      this.$log.debug(event);
      let file = event.target.files[0];
      this.$log.debug(file);

      if (file.type.includes('image/')) {
        this.post.thumbnail = file;
      } else {
        this.$log.debug('file type should be an image');
        swal({
          title: 'Notificación',
          text: 'El archivo debe ser una imagen',
        });
      };
    },

    // @vuese
    // submit post information to backend
    submitPost() {
      this.onLoading = true;
      let postUrl = this.postUrl;
      let post = this.post;
      this.getData()
        .then( data => {
          let text = JSON.stringify(data);
          this.$log.debug('editor data', post);
          let postFormData = new FormData();
          postFormData.append('title', post.title);
          postFormData.append('author', post.author);
          postFormData.append('tag', post.tag);
          postFormData.append('text', text);
          postFormData.append('thumbnail', post.thumbnail);
          axios.post(postUrl, postFormData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            }
          })
            .then( response => {
              this.$log.debug(response);
              let data = response.data;
              this.$log.debug(data);
              swal({
                title: 'Notificación',
                text: `Creado con exito`,
              });
              this.clearEditorData();
            })
            .catch( errors => {
              let request = errors.request;
              this.$log.error(request);
              if (request.status === 400) {
                swal({
                  title: 'Notificación',
                  text: 'Verifique lo siguiente:\n- que el post tenga un titulo\n- que el titulo del post no tenga mas de 100 letras\n- que haya elegido una imagen thumbnail',
                });
              } else {
                swal({
                  title: 'Notificación',
                  text: 'Hubo un error, intente de nuevo',
                });
              };
            })
            .finally( () => {
              this.onLoading = false;
            });
        })
        .catch( error => {
          this.$log.error(error);
        });
    },
  },

  mounted() {
    this.loadDataFromLocalStorage();
    this.initEditor();
  },
  
  beforeDestroy() {
    this.getData()
      .then( data => {
        this.saveDataToLocalStorage(data);
      })
    window.editor.destroy();
  }
}
</script>