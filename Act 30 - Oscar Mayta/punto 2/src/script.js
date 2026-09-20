/*
Ejercicio práctico #2:
Crear un carrito de compras dinámico con productos de una API
Enunciado: Vas a crear un carrito de compras dinámico que permite agregar
productos al carrito utilizando datos obtenidos de una API externa. Los pasos
específicos son:
1. Utilizá fetch() para obtener una lista de productos desde una API (puede ser la
misma API de productos del Ejercicio 1).
2. Mostrá los productos en la página en forma de tarjetas o lista.
3. Agregá un botón &quot;Añadir al carrito&quot; para cada producto. Al hacer clic en el
botón, el producto debe añadirse al carrito.
4. Usá LocalStorage para almacenar los productos que se agreguen al carrito,
de manera que si recarga la página, los productos sigan allí.
5. Mostrá la cantidad de productos que hay en el carrito en todo momento,
actualizándose cada vez que se añada un nuevo producto.
*/

function actualizarCarrito() {
  const carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  const carritoCounter = document.getElementById("cart-counter");
  if (carritoCounter) carritoCounter.textContent = carrito.length;
}

document.addEventListener("DOMContentLoaded", () => {
  const contenedor = document.getElementById("productos-container");
  const categorias = ["smartphones", "laptops", "tablets"];

  categorias.forEach((categoria) => {
    fetch(`https://dummyjson.com/products/category/${categoria}`)
      .then((response) => response.json())
      .then((data) => {
        data.products.forEach((producto) => {
          contenedor.innerHTML += `
            <div class="card">
              <img src="${producto.thumbnail}" alt="${producto.title}">
              <h3>${producto.title}</h3>
              <p>Precio: $${producto.price}</p>
              <button onclick="agregarAlCarrito(${producto.id})">Añadir al carrito</button>
            </div>
          `;
        });

        actualizarCarrito();
      })
      .catch((error) => {
        console.error("Error al obtener productos:", error);
        contenedor.innerHTML = "<p>Hubo un problema al cargar los productos.</p>";
      });
  });
});

document.getElementById("vaciar-carrito").addEventListener("click", () => {
  localStorage.removeItem("carrito");
  actualizarCarrito();
});

function agregarAlCarrito(idProducto) {
  let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  carrito.push(idProducto);
  localStorage.setItem("carrito", JSON.stringify(carrito));
  alert("Producto añadido al carrito");
  actualizarCarrito();
}
