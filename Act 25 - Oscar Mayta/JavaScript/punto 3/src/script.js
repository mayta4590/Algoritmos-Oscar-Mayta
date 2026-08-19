/*
3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ [&quot;Franco&quot;, (78.5, 77.2, 79.1)], [&quot;Lewis&quot;, (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
*/

function cargar_pilotos() {
    let pilotos = [];

    for (let i = 0; i < 4; i++) {
        let nombre = prompt("Ingrese el nombre del piloto:");

        let tiempo1 = Number(prompt("Ingrese el tiempo de la vuelta 1:"));
        let tiempo2 = Number(prompt("Ingrese el tiempo de la vuelta 2:"));
        let tiempo3 = Number(prompt("Ingrese el tiempo de la vuelta 3:"));

        let tiempos = [tiempo1, tiempo2, tiempo3];

        pilotos.push([nombre, tiempos]);
    }

    return pilotos;
}


function calcular_promedios(pilotos) {
    for (let [nombre, tiempos] of pilotos) {
        let promedio = (tiempos[0] + tiempos[1] + tiempos[2]) / 3;

        console.log("Piloto:", nombre, "Promedio:", promedio);
    }
}


function mejor_vuelta(pilotos) {
    let mejor = pilotos[0][1][0];
    let piloto_mejor = pilotos[0][0];

    for (let [nombre, tiempos] of pilotos) {
        for (let tiempo of tiempos) {
            if (tiempo < mejor) {
                mejor = tiempo;
                piloto_mejor = nombre;
            }
        }
    }

    console.log("La mejor vuelta fue:", mejor, "segundos");
    console.log("Pertenece al piloto:", piloto_mejor);
}


let pilotos = cargar_pilotos();

calcular_promedios(pilotos);

mejor_vuelta(pilotos);