/*3. Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
onBlur)*/

function validar(control)
{
    if (control.value.length < 7 || control.value.length > 20)
    {
        alert('largo de clave incorrecto, ingresar entre 7 y 20 caracteres');
    } else
    {
        alert('datos correctos');
    }
}