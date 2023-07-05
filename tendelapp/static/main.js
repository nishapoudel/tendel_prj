//add color when nav-link is clicked
$(document).ready(function () {
    var activeNavItem = localStorage.getItem('activeNavItem');

   // If there is an active state, set it on the nav-item
   if (activeNavItem) {
     $('.navbar-light .navbar-nav .nav-link').removeClass('active');
     $('#' + activeNavItem).addClass('active');
   }

   // Add a click event listener to the nav-items
   $('.navbar-light .navbar-nav .nav-link').click(function() {

     $('navbar-light .navbar-nav .nav-link').removeClass('active');

     $(this).addClass('active');


     localStorage.setItem('activeNavItem', $(this).attr('id'));
   });
});


(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
      setTimeout(function () {
          if ($('#spinner').length > 0) {
              $('#spinner').removeClass('show');
          }
      }, 1);
  };
  spinner();


  // Initiate the wowjs
  new WOW().init();


//   Sticky Navbar
$(window).scroll(function () {
    if ($(this).scrollTop() > 45) {
        $('.nav-blue').addClass('sticky-top shadow-sm');
    } else {
        $('.nav-blue').removeClass('sticky-top shadow-sm');
    }
});

$(window).scroll(function () {
      if ($(this).scrollTop() > 45) {
          $('.nav-blue').addClass('sticky-top shadow-sm');
      } else {
          $('.nav-blue').removeClass('sticky-top shadow-sm');
      }
  });


  // Smooth scrolling on the navbar links
//   $(".navbar-nav a").on('click', function (event) {
//       if (this.hash !== "") {
//           event.preventDefault();

//           $('html, body').animate({
//               scrollTop: $(this.hash).offset().top - 45
//           }, 1500, 'easeInOutExpo');

//           if ($(this).parents('.navbar-nav').length) {
//               $('.navbar-nav .active').removeClass('active');
//               $(this).closest('a').addClass('active');
//           }
//       }
//   });


  // Back to top button
  $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {
          $('.back-to-top').fadeIn('slow');
      } else {
          $('.back-to-top').fadeOut('slow');
      }
  });
  $('.back-to-top').click(function () {
      $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
      return false;
  });



    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


})(jQuery);


