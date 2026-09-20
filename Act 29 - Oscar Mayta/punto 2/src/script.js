/*
  Ejercicio 2: Carrito de Compras con Conteo de Productos
  Consigna: Crear un carrito de compras utilizando LocalStorage, que permita
  a los usuarios agregar productos y muestre la cantidad total de productos
  en el carrito. Los productos deben tener un botón para agregar al
  carrito. Al agregar un producto, se debe mostrar el número total de
  productos en el carrito, almacenándolo en LocalStorage. Al recargar la
  página, el número total de productos debe recuperarse de LocalStorage y
  mostrarse correctamente.
*/

document.addEventListener("DOMContentLoaded", function () {
  cargarCarrito();
});

var botonesAgregar = document.querySelectorAll(".agregar-carrito");
for (var i = 0; i < botonesAgregar.length; i++) {
  botonesAgregar[i].addEventListener("click", agregarProducto);
}

document.getElementById("vaciar-carrito").addEventListener("click", function () {
  localStorage.removeItem("carrito");
  cargarCarrito();
});

function agregarProducto(event) {
  var id = event.target.getAttribute("data-id");
  var nombre = event.target.getAttribute("data-nombre");
  var precio = parseInt(event.target.getAttribute("data-precio"));
  var producto = { id: id, nombre: nombre, precio: precio };

  var carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  carrito.push(producto);
  localStorage.setItem("carrito", JSON.stringify(carrito));

  cargarCarrito();
}

function cargarCarrito() {
  var carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  document.getElementById("contador").textContent = carrito.length;
}
