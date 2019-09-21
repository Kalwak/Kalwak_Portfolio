/*
  que es javascript ?
  jascript es un lenguaje de programacion principamente usado
  en los navegadores web para hacer paginas web dinamicas
  pero como es una pagina dinamica ?, pues supongamos que quieres
  preguntarle al usuario cual es su nombre,
*/


// definimos la variables cuyo valor sera el nombre del usuario 
var username;

// ahora usaremos algo llamado una funcion
// ( una funcion no es mas que bloque de codigo que se hace cierta tarea )
username = prompt('Esto es el label de la vetana que muestra la funcion prompt', 'esto es el valor por defecto');
// prompt toma dos argumentos 
// una label/letrero/titulo para dar a conocer al usuario sobre la informacion requerida
// un valor por defecto
// la funcion prompt devuelve lo que el usuario haya escribido, si no escribio nada y el usuario toca ok, 
// devuelve un string vacio
// si toca cancel la funcion devuelve null