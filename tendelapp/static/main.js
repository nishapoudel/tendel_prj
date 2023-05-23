// const arrowIcon = document.getElementById('arrow-icon');
// const additionalInfo = document.getElementById('additional-info');

// arrowIcon.addEventListener('click', () => {
//   additionalInfo.classList.toggle('hidden');
//   arrowIcon.classList.toggle('active');
// });

// arrowIcon.addEventListener('keydown', (event) => {
//   if (event.key === 'Enter' || event.key === ' ') {
//     additionalInfo.classList.toggle('hidden');
//     arrowIcon.classList.toggle('active');
//   }
// });

// document.addEventListener('click', (event) => {
//   const isClickInside = arrowIcon.contains(event.target) || additionalInfo.contains(event.target);
//   if (!isClickInside) {
//     additionalInfo.classList.add('hidden');
//     arrowIcon.classList.remove('active');
//   }
// });
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





})(jQuery);

