/* jQuery.noConflict();
(function($) {
  $(document).ready(function() {
    $('.owl-carousel').owlCarousel({
      loop:true,
      margin:10,
      nav:true,
      dots:true,
      autoplay:true,
      autoplayTimeout:3000,
      responsive:{
          0:{
              items:1
          },
          768:{
              items:2
          },
          1280:{
              items:3
          }
      }
    })
  });
})(jQuery); */

document.addEventListener("DOMContentLoaded", function () {
  window.addEventListener("scroll", function () {
    if (window.scrollY > 50) {
      document.getElementById("navbar-top").classList.add("fixed-top");
      // add padding top to show content behind navbar
      navbar_height = document.querySelector(".navbar").offsetHeight;
      document.body.style.paddingTop = navbar_height + "px";
    } else {
      document.getElementById("navbar-top").classList.remove("fixed-top");
      // remove padding top from body
      document.body.style.paddingTop = "0";
    }
  });
});

setTimeout(function () {
  var messageAlert = document.getElementById("message-alert");
  messageAlert.style.transition = "opacity 1s";
  messageAlert.style.opacity = "0";
  setTimeout(function () {
    messageAlert.style.display = "none";
  }, 1000); // 1000 ms = 1 segundo
}, 5000); // 5000 ms = 5 segundos
