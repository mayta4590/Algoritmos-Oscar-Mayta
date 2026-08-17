/*
Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = ["Boca", "River", "Racing"] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8).
*/

function ingresar(equipos, puntos, diferencia_gol){
    for(let x=0; x<3; x++){
        let equipo = prompt("Ingrese el nombre del equipo: ");
        equipos.push(equipo);
        let punto = parseInt(prompt("Ingrese los puntos del equipo: "));
        puntos.push(punto);
        let dif = parseInt(prompt("Ingrese la diferencia de goles del equipo: "));
        diferencia_gol.push(dif);
    }
}

function ordenar_tabla(equipos, puntos, diferencia_gol){
    let aux;

    for(let i=0; i<equipos.length; i++){
        for(let j=0; j<equipos.length - 1; j++){

            if(puntos[j] < puntos[j + 1]){
                aux = puntos[j];
                puntos[j] = puntos[j + 1];
                puntos[j + 1] = aux;

                aux = equipos[j];
                equipos[j] = equipos[j + 1];
                equipos[j + 1] = aux;

                aux = diferencia_gol[j];
                diferencia_gol[j] = diferencia_gol[j + 1];
                diferencia_gol[j + 1] = aux;
            }

            else if(puntos[j] == puntos[j + 1]){

                if(diferencia_gol[j] < diferencia_gol[j + 1]){
                    aux = puntos[j];
                    puntos[j] = puntos[j + 1];
                    puntos[j + 1] = aux;

                    aux = equipos[j];
                    equipos[j] = equipos[j + 1];
                    equipos[j + 1] = aux;

                    aux = diferencia_gol[j];
                    diferencia_gol[j] = diferencia_gol[j + 1];
                    diferencia_gol[j + 1] = aux;
                }
            }
        }
    }
}


let equipos = [];
let puntos = [];
let diferencia_gol = [];
ingresar(equipos, puntos, diferencia_gol);
ordenar_tabla(equipos, puntos, diferencia_gol);

console.log("Tabla de posiciones:");

for(let i=0; i<equipos.length; i++){
    console.log(i + 1, " ", equipos[i], " ", puntos[i], "pts  DG", diferencia_gol[i]);
}