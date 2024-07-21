document.addEventListener("DOMContentLoaded", function () {
  const gallery = document.getElementById("gallery");
  const items = gallery.getElementsByClassName("masonry-item");

  function randomizeImageSizes() {
    Array.from(items).forEach((item) => {
      const img = item.querySelector("img");
      const randomHeight = Math.floor(Math.random() * (400 - 200 + 1)) + 350; // Random height between 200px and 400px
      img.style.height = `${randomHeight}px`;
      img.style.objectFit = "cover";
    });
  }

  randomizeImageSizes();

  // Optional: Re-run on window resize if you want to maintain the randomness
  window.addEventListener("resize", randomizeImageSizes);
});
