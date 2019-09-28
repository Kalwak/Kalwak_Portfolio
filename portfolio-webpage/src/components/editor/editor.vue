<template>
  <div class="editor-container">
    <header class="editor__header">
      <h2 class="editor-title">Editor Kalwak</h2>
    </header>
    <div class="editor__body">
      <div class="editor-page">
        <input class="post-main__title" placeholder="Titulo" />
        <div id="editor-holder"></div>
      </div>
      <div class="editor-settings">
        <div class="editor-toolbar">
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/anterior.png" alt="Anterior" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/siguiente.png" alt="Siguiente" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/more.png" alt="Mas" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/less.png" alt="Menos" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/bold.png" alt="Negrita" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/italic.png" alt="Italica" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/underline.png" alt="Delineado" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/ol.png" alt="Ordernada" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/ul.png" alt="Desordenada" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item">
            <img src="@/assets/images/editor-icons/paste.png" alt="Pegar" class="toolbar__item-icon" />
          </span>
          <div class="w-100"></div>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/image.png" alt="Imagen" class="toolbar__item-icon" />
          </span>
          <span class="toolbar__item toolbar__item--separator">
            <img src="@/assets/images/editor-icons/image.png" alt="Video" class="toolbar__item-icon" />
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
          <select-filter :options="categories" default-option="development" class="post-category"></select-filter>
          <select-filter :options="authors" default-option="development" class="post-category"></select-filter>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// editor component for the creation of post for the blog section
import EditorJS from '@editorjs/editorjs';
import editorConfig from './editor.config';
import SelectFilter from '../sub-layout/select-filter';


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
        'Jose Quesada Villalobos',
        'Joseph Zamora',
        'Edwin Garcia',
        'Jennifer De La Cruz',
      ],
    };
  },

  components: {
    SelectFilter,
  },

  methods: {
    initEditor() {
      window.editorJS = new EditorJS(editorConfig);
    }
  },

  mounted() {
    this.initEditor();
  }
}
</script>