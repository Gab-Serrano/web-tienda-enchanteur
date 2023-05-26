function ValidacionContactanos(){
    var nombreInput = document.getElementById('Nombre-Contactanos').value;
    var telefonoInput = document.getElementById('Telefono-Contactanos').value;
    var correoInput = document.getElementById('Correo-Contactanos').value;
    var asuntoContactanos = document.getElementById('Asunto-Contactanos').value;
    var mensajeContactanos = document.getElementById('Mensaje-Contactanos').value;

    if(nombreInput.trim() === ''){
        alert('Debe escribir un nombre');
    } else if(telefonoInput.length !== 9) {
        alert('Número de telefono invalido');
    } else if (correoInput.trim() === '' || !correoInput.includes('@') || !correoInput.includes('.')){
        alert('Ingrese un correo válido');
    } else if(asuntoContactanos.trim() === ''){
        alert('Debe escribir asunto');
    } else if (mensajeContactanos.trim()===''){
        alert('Debe escribir un mensaje');
    } else{
        document.forms[0].submit();
    }
    


}