/*
  Ejercicio 1: Guardar Preferencias de Usuario
  Consigna: Crear una función que guarde y recupere las preferencias de un
  usuario, como su nombre y el color de fondo preferido, utilizando
  LocalStorage. La función debe permitir al usuario ingresar su nombre y
  seleccionar su color de fondo preferido desde una lista de opciones.
  Los datos ingresados deben almacenarse en LocalStorage. Cada vez que la
  página se recargue, las preferencias deben recuperarse de LocalStorage y
  aplicarse automáticamente (mostrar el nombre del usuario y cambiar el
  color de fondo).
*/

document.addEventListener("DOMContentLoaded", function () {
  cargarPreferencias();
});

document.getElementById("guardar-preferencias").addEventListener("click", function () {
  var nombre = document.getElementById("nombre").value;
  var color = document.getElementById("color").value;

  var preferencias = { nombre: nombre, color: color };
  localStorage.setItem("preferencias", JSON.stringify(preferencias));

  cargarPreferencias();
});

function cargarPreferencias() {
  var preferencias = JSON.parse(localStorage.getItem("preferencias")) || null;

  if (preferencias) {
    document.body.style.backgroundColor = preferencias.color;
    document.getElementById("saludo").textContent = "Hola, " + preferencias.nombre + "!";
    document.getElementById("nombre").value = preferencias.nombre;
    document.getElementById("color").value = preferencias.color;
  }
}
