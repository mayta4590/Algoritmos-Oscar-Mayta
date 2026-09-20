/*
  Ejercicio 3: Borrador de Notas de Sesión
  Consigna: Crear una aplicación de notas rápidas que permita al usuario
  escribir un mensaje o nota en un campo de texto y guardarlo de forma
  temporal utilizando SessionStorage. Debe contar con un campo de texto
  (<textarea> o <input>) y un botón "Guardar Nota". Al hacer clic en el
  botón "Guardar Nota", el texto ingresado debe almacenarse en
  SessionStorage y mostrarse en un elemento dentro del DOM. Al recargar la
  página (F5), la nota guardada debe recuperarse de SessionStorage y seguir
  mostrándose en pantalla. Debe incluir un botón "Borrar Nota" que elimine
  el registro de SessionStorage mediante removeItem() y limpie el
  contenido del DOM.
*/

document.addEventListener("DOMContentLoaded", function () {
  cargarNota();
});

document.getElementById("guardar-nota").addEventListener("click", function () {
  var texto = document.getElementById("nota").value;
  sessionStorage.setItem("nota", texto);
  cargarNota();
});

document.getElementById("borrar-nota").addEventListener("click", function () {
  sessionStorage.removeItem("nota");
  document.getElementById("nota").value = "";
  cargarNota();
});

function cargarNota() {
  var nota = sessionStorage.getItem("nota");
  var notaGuardada = document.getElementById("nota-guardada");

  if (nota) {
    notaGuardada.textContent = nota;
    document.getElementById("nota").value = nota;
  } else {
    notaGuardada.textContent = "";
  }
}
