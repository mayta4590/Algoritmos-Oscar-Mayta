/*
Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.
*/

function reservar_consecutivos(sala, fila, cantidad) {

    for (let i = 0; i <= sala[fila].length - cantidad; i++) {

        let se_puede = true;

        for (let j = 0; j < cantidad; j++) {
            if (sala[fila][i + j] === 1) {
                se_puede = false;
                break;
            }
        }
        if (se_puede) {
    
            let columnas = [];

            for (let j = 0; j < cantidad; j++) {
                sala[fila][i + j] = 1;
                columnas.push(i + j);
            }
            return "Reserva realizada en las columnas: " + columnas.join(", ");
        }
    }

    return "No se pudo hacer la reserva.";
}

let sala = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
];

console.log("Sala antes:");
for (let fila = 0; fila < sala.length; fila++) {
    console.log(sala[fila]);
}

console.log(reservar_consecutivos(sala, 0, 3));

console.log("Sala después:");
for (let fila = 0; fila < sala.length; fila++) {
    console.log(sala[fila]);
}