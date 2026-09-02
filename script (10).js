/*5. Generar un presupuesto de un equipo de computación a partir de tres
objetos de tipo SELECT que nos permiten seleccionar:
Procesador (Intel I3 - $400, Intel I5 $600, Intel I7 $800).
Monitor (Samsung 20&#39; - $250, Samsung 22&#39; - $350, Samsung 26&#39; - $550)
Disco Duro(500 Gb - $300, 1 Tb - $440, 3 Tb - $500)
Para cada característica indicamos string a mostrar (Ej. Intel I3) y el
valor asociado a dicho string (Ej. 400).
Al presionar un botón &quot;Calcular&quot; mostrar el presupuesto en un objeto de
tipo TEXT.*/

function calcularPresupuesto() {
  let proc = document.getElementById('procesador');
  let mon = document.getElementById('monitor');
  let dis = document.getElementById('disco');

  let valorProc = Number(proc.options[proc.selectedIndex].value);
  let valorMon = Number(mon.options[mon.selectedIndex].value);
  let valorDis = Number(dis.options[dis.selectedIndex].value);

  let total = valorProc + valorMon + valorDis;
  document.getElementById('totalPC').value = '$' + total;
}