import Header from '@editorjs/header';
import List from '@editorjs/list';
import Delimiter from '@editorjs/delimiter';
import Code from '@editorjs/code';
import Inline from '@editorjs/inline-code';
import Image from '@editorjs/image';


export default {
  holder: 'editor-holder',
  autofocus: true,
  initialBlock: null,
  placeholder: 'Toque aqui para editar',

  tools: {
    header: {
      class: Header,
      inlineToolbar: ['italic', 'bold'],
      config: {
        placeholder: 'Titulo',
      }
    },

    list: {
      class: List,
      inlineToolbar: true,
    },

    delimiter: {
      class: Delimiter,
    },

    code: Code,

    inlineCode: Inline,

    image: {
      class: Image,
      inlineToolbar: true,
      config: {
        endpoints: {
          byFile: 'http://localhost:4000/upload-image/',
        }
      }
    }
  },
};