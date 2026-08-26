/*
Ejercicio 01: Modificación del DOM con Métodos de Selección
Enunciado: Crear un programa que, al hacer clic en un botón, cambie el contenido de
un párrafo en la página utilizando los métodos para acceder al DOM. Los pasos
específicos son:
1. Al cargar la página, se debe mostrar un párrafo con el texto: &quot;Texto inicial&quot;.
2. Al hacer clic en un botón, se debe cambiar ese texto por: &quot;El texto ha sido
modificado con JavaScript&quot;.
3. Usar getElementById() para seleccionar el párrafo y modificar su contenido con
textContent.
*/

const parrafo1 = document.getElementById("parrafo1");
const btn1 = document.getElementById("btn1");

btn1.addEventListener("click", () => {
  parrafo1.textContent = "El texto ha sido modificado con JavaScript";
});