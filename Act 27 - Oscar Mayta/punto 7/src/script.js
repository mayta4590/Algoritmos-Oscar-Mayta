/*7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió.*/

function mostrarDeportes() {
  let mensaje = 'Deportes seleccionados:\n';
  let alguno = false;

  if (document.getElementById('futbol').checked) {
    mensaje += '- Fútbol\n';
    alguno = true;
  }
  if (document.getElementById('basquet').checked) {
    mensaje += '- Básquet\n';
    alguno = true;
  }
  if (document.getElementById('voleibol').checked) {
    mensaje += '- Voleibol\n';
    alguno = true;
  }
  if (!alguno) {
    mensaje = 'No seleccionó ningún deporte';
  }
  alert(mensaje);
}