function validaNombre() {
   var nombre = document.getElementById("Nombre").value;
   if (nombre.length < 3) {
      return false;
   } else {
      return true;
   }
}


function validarEmail() {
   var email = document.getElementById("Correo").value;
   expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
   if (!expr.test(email)) {
      return false;
   } else {
      return true;
   }
}
/*
function validarContrasena() {
   var contrasena = document.getElementById("Contraseña").value;
   regContra= /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}[^'\s]/
   if (regContra.test(contrasena)) {
      return true;
   } else {
      return false;
   }
}
*/
function validarContrasena() {
   var pass = document.getElementsById("Contraseña").value;
   var repass = document.getElementsById
      ("ConfirmaContraseña").value;

   if (pass.length >= 8 || repass.length >= 8) {
      if (pass == repass) {       
         return true;
      } else {
         alert('Las contraseñas no son iguales.');
         return false;
      }
   }
}


function alertaValidaciones() {
   if (validaNombre()) {
      if (validarEmail()) {
         if (validarContrasena()) {
            alert("Bienvenido")
            return true;
         } else {
            alert("Contraseña invalida")
            return false;
         }
      } else {
         alert("Correo invalido")
         return false;
      }
   } else {
      alert("Nombre invalido")
      return false;
   }
}