/*
Ejercicio 02: Creación Dinámica de Elementos y Eventos
Enunciado: Desarrollar un programa que permita a la persona agregar nuevos
elementos a una lista mediante un botón. Los pasos son:
1. Al hacer clic en un botón, se debe crear un nuevo elemento &lt;li&gt; en una lista ya
existente.
2. El contenido del nuevo elemento debe ser el texto: &quot;Nuevo Elemento&quot;.
3. Usar createElement() para crear el nuevo elemento y appendChild() para
añadirlo a la lista.
4. Cada vez que se agrega un nuevo elemento, se debe mostrar una alerta
indicando: &quot;Se ha añadido un nuevo elemento&quot;.
*/

const lista2 = document.getElementById("lista2");
const btn2 = document.getElementById("btn2");

btn2.addEventListener("click", () => {
  const nuevoLi = document.createElement("li");
  nuevoLi.textContent = "Nuevo Elemento";
  lista2.appendChild(nuevoLi);
  alert("Se ha añadido un nuevo elemento");
});