"use strict";

/*MARQUEE*/
function Marquee(selector, speed) {
  const parentSelector = document.querySelector(selector);
  const clone = parentSelector.innerHTML;
  const firstElement = parentSelector.children[0];
  let i = 0;
  parentSelector.insertAdjacentHTML("beforeend", clone);
  parentSelector.insertAdjacentHTML("beforeend", clone);
  setInterval(function () {
    firstElement.style.marginLeft = `-${i}px`;
    if (i > firstElement.clientWidth) {
      i = 0;
    }
    i = i + speed;
  }, 0);
}

if (document.querySelector(".marquee-1")) {
  window.addEventListener("load", Marquee(".marquee-1", 0.5));
}

if (document.querySelector(".marquee-2")) {
  window.addEventListener("load", Marquee(".marquee-2", 0.4));
}

if (document.querySelector(".marquee-3")) {
  window.addEventListener("load", Marquee(".marquee-3", 0.55));
}

if (document.querySelector(".marquee-3")) {
  window.addEventListener("load", Marquee(".marquee-4", 0.4));
}
