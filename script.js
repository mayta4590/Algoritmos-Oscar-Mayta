/*4. Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma.*/

function mostrarPrecio() {
  let sel = document.getElementById('pizza');
  let precio = sel.options[sel.selectedIndex].value;
  document.getElementById('precioPizza').value = '$' + precio;
}