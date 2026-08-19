/*
1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
*/

function carga() {
    let temperaturas = [];

    for (let i = 0; i < 6; i++) {
        let temperatura = parseFloat(prompt("Ingrese la temperatura:"));
        temperaturas.push(temperatura);
    }

    return temperaturas;
}

function procesar_extremos(temperaturas) {
    let maxima = temperaturas[0];
    let minima = temperaturas[0];

    for (let i = 0; i < 6; i++) {
        if (temperaturas[i] > maxima) {
            maxima = temperaturas[i];
        }

        if (temperaturas[i] < minima) {
            minima = temperaturas[i];
        }
    }

    return [maxima, minima];
}

let temperaturas = carga();

let [maxima, minima] = procesar_extremos(temperaturas);

console.log("La temperatura máxima es:", maxima);
console.log("La temperatura mínima es:", minima);