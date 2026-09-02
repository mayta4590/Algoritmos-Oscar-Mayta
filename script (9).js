/*6. Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT)*/

function corregirExamen() {
  let correctas = 0;
  let incorrectas = 0;

  for (let i = 1; i <= 4; i++) {
    let select = document.getElementById('p' + i);
    let valor = select.options[select.selectedIndex].value;
    if (valor == 1) {
      correctas++;
    } else {
      incorrectas++;
    }
  }
  alert('Respuestas correctas: ' + correctas + '\nRespuestas incorrectas: ' + incorrectas);
}