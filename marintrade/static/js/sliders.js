const swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    loop: true,
    autoplay: {
      delay: 3000,
    },
    slidesPerView: 3,
    pagination: {
      el: ".swiper-pagination",
    },
    mousewheel: true,
    keyboard: true,
  });

swiper.mousewheel.disable()

const swiper2 = new Swiper(".portfolio__swiper", {
    // spaceBetween: 30,
    navigation: {
      nextEl: ".portfolio-button-next",
      prevEl: ".portfolio-button-prev",
    },
    loop: true,
    autoplay: {
      delay: 5000,
    },
    // pagination: {
    //   el: ".swiper-pagination",
    // },
    // mousewheel: true,
    keyboard: true,
  });