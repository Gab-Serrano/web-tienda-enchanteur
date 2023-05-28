jQuery.noConflict();
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
})(jQuery);