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
   alert("validarContrasena")
   var pass = document.getElementsById("Contraseña").value;
   alert("pass");
   var repass = document.getElementsById
      ("ConfirmaContraseña").value;
   alert("repass");
   if (pass.length >= 8 || repass.length >= 8) {
      alert("if 1")
      if (pass == repass) { 
         alert("if 2")      
         return true;
      } else {
         alert('Las contraseñas no son iguales.');
         return false;
      }
   }
}


function alertaValidaciones() {
   if (validaNombre()) {
      alert("Bienvenido sin correo")
      if (validarEmail()) {
         alert("Bienvenido sin contraseña")
         if (validarContrasena()) {
            alert("Bienvenido a todo")
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