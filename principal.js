// ILBD — slider.js

const slides = document.querySelectorAll(".hero-slide");
const dots = document.querySelectorAll(".hero-dot");
let cur = 0;

function goTo(i) {
  slides[cur].classList.remove("active");
  dots[cur].classList.remove("active");
  cur = (i + slides.length) % slides.length;
  slides[cur].classList.add("active");
  dots[cur].classList.add("active");
}

document.getElementById("next").onclick = () => goTo(cur + 1);
document.getElementById("prev").onclick = () => goTo(cur - 1);
dots.forEach((d) => (d.onclick = () => goTo(+d.dataset.i)));

setInterval(() => goTo(cur + 1), 10000); //Tiempo entre cada cambio de slide (10 segundos)

// Navegación móvil (misma función en index)
const navToggleMain = document.querySelector(".nav-toggle");
const navLinksMain = document.querySelector(".nav-links");
if (navToggleMain && navLinksMain) {
  navToggleMain.addEventListener("click", () => {
    const expanded = navToggleMain.getAttribute("aria-expanded") === "true";
    navToggleMain.setAttribute("aria-expanded", String(!expanded));
    navLinksMain.classList.toggle("open");
  });

  navLinksMain.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinksMain.classList.remove("open");
      navToggleMain.setAttribute("aria-expanded", "false");
    });
  });
}
