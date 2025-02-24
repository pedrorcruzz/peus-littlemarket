const hamburguerBtn = document.getElementById("hamburguer-btn");
const hamburguerMenu = document.getElementById("hamburguer-menu");

hamburguerBtn.addEventListener("click", () => {
  hamburguerMenu.classList.toggle("hidden");
});
