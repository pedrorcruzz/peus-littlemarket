document.addEventListener("DOMContentLoaded", () => {
  const prevButton = document.querySelector(".carousel-prev");
  const nextButton = document.querySelector(".carousel-next");
  const carouselItems = document.querySelector(".carousel-items");
  const carouselItemWidth =
    carouselItems.querySelector(".carousel-item").offsetWidth;
  let currentIndex = 0;

  const nextSlide = () => {
    if (currentIndex < carouselItems.children.length - 1) {
      currentIndex++;
    } else {
      currentIndex = 0;
    }
    updateCarousel();
  };

  const prevSlide = () => {
    if (currentIndex > 0) {
      currentIndex--;
    } else {
      currentIndex = carouselItems.children.length - 1;
    }
    updateCarousel();
  };

  const updateCarousel = () => {
    carouselItems.style.transform = `translateX(-${currentIndex * carouselItemWidth}px)`;
  };

  nextButton.addEventListener("click", nextSlide);
  prevButton.addEventListener("click", prevSlide);

  setInterval(nextSlide, 5000);
});
