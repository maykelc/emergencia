document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".slide");
  const prevButton = document.querySelector(".prevbanner");
  const nextButton = document.querySelector(".nextbanner");
  const slideContainer = document.querySelector(".slides");
  const totalSlides = slides.length;
  let currentIndex = 0;
  const slideInterval = 5000; // Intervalo en milisegundos (5000 ms = 5 segundos)

  if (!slides.length) {
    console.error("No slides found");
    return;
  }

  function showSlide(index) {
    if (index >= totalSlides) {
      currentIndex = 0;
    } else if (index < 0) {
      currentIndex = totalSlides - 1;
    } else {
      currentIndex = index;
    }

    const offset = -currentIndex * 100;
    slideContainer.style.transform = `translateX(${offset}%)`;
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  function prevSlide() {
    showSlide(currentIndex - 1);
  }

  prevButton.addEventListener("click", function () {
    prevSlide();
  });

  nextButton.addEventListener("click", function () {
    nextSlide();
  });

  setInterval(nextSlide, slideInterval);

  showSlide(currentIndex);
});











