
function ValidacionContactanos(){
    var nombreInput = document.getElementById('Nombre-Contactanos1').value;
    var nombreInput2 = document.getElementById('Nombre-Contactanos2').value;
    var nombreInput3 = document.getElementById('Nombre-Contactanos3').value;
    var telefonoInput = document.getElementById('Telefono-Contactanos1').value;
    var telefonoInput2 = document.getElementById('Telefono-Contactanos2').value;
    var telefonoInput3 = document.getElementById('Telefono-Contactanos3').value;
    var correoInput = document.getElementById('Correo-Contactanos1').value;
    var correoInput2 = document.getElementById('Correo-Contactanos2').value;
    var correoInput3 = document.getElementById('Correo-Contactanos3').value;
    var asuntoContactanos = document.getElementById('Asunto-Contactanos1').value;
    var asuntoContactanos2 = document.getElementById('Asunto-Contactanos2').value;
    var asuntoContactanos3 = document.getElementById('Asunto-Contactanos3').value;
    var mensajeContactanos = document.getElementById('Mensaje-Contactanos1').value;
    var mensajeContactanos2 = document.getElementById('Mensaje-Contactanos2').value;
    var mensajeContactanos3 = document.getElementById('Mensaje-Contactanos3').value;

    if(nombreInput.length < 3 && nombreInput2.length < 3 && nombreInput3.length < 3){
        alert('Debe escribir un nombre');
    } else if((telefonoInput.length !== 9 || isNaN(telefonoInput)) && (telefonoInput2.length !== 9 || isNaN(telefonoInput2)) && (telefonoInput3.length !== 9 || isNaN(telefonoInput3))) {
        alert('Número de telefono invalido');
    } else if ((correoInput.trim() === '' || !correoInput.includes('@') || !correoInput.includes('.')) && (correoInput2.trim() === '' || !correoInput2.includes('@') || !correoInput2.includes('.')) && (correoInput3.trim() === '' || !correoInput3.includes('@') || !correoInput3.includes('.'))) {
        alert('Ingrese un correo válido');
    } else if(asuntoContactanos.trim() === '' && asuntoContactanos2.trim() === '' && asuntoContactanos3.trim() === ''){
        alert('Debe escribir asunto');
    } else if (mensajeContactanos.trim()==='' && mensajeContactanos2.trim()==='' && mensajeContactanos3.trim()===''){
        alert('Debe escribir un mensaje');
    } else{
        document.forms[0].submit();
        alert('Tus datos fueron enviados de manera exitosa, estaremos contactandonos contigo')
    }
    
}

