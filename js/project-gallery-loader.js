document.addEventListener("DOMContentLoaded", () => {
  if (typeof folder === "undefined" || typeof imageCount === "undefined") {
    console.error("🛑 Fehler: 'folder' oder 'imageCount' ist nicht definiert.");
    return;
  }

  const gallery = document.getElementById("project-gallery");
  const modalImg = document.getElementById("modalImage");

  const modal = new bootstrap.Modal(document.getElementById("imageModal"));
  let currentIndex = 0;
  const modalImages = [];

  for (let i = 0; i < imageCount; i++) {
    const src = `${folder}${i}.jpg`;

    const col = document.createElement("div");
    col.className = "col-md-6 col-lg-4";

    const wrapper = document.createElement("div");
    wrapper.className = "img-tile-large";

    const img = document.createElement("img");
    img.src = src;
    img.alt = `Bild ${i}`;
    img.className = "img-fluid img-thumb";
    img.dataset.index = modalImages.length; // 🔁 Index = aktuelle Länge = Position

    modalImages.push(src); // Wichtig: erst pushen, dann index setzen

    wrapper.appendChild(img);
    col.appendChild(wrapper);
    gallery.appendChild(col);
  }

  // Klick auf Bild → Modal öffnen
  document.querySelectorAll(".img-thumb").forEach(img => {
    img.addEventListener("click", () => {
      currentIndex = parseInt(img.dataset.index);
      modalImg.src = modalImages[currentIndex];
      modal.show();  // ← Jetzt funktioniert das Vergrößern wieder
    });
  });


  // Tastennavigation im Modal
  document.addEventListener("keydown", (event) => {
    const modalVisible = document.getElementById("imageModal").classList.contains("show");
    if (!modalVisible) return;

    if (event.key === "ArrowRight") {
      currentIndex = (currentIndex + 1) % modalImages.length;
      modalImg.src = modalImages[currentIndex];
    } else if (event.key === "ArrowLeft") {
      currentIndex = (currentIndex - 1 + modalImages.length) % modalImages.length;
      modalImg.src = modalImages[currentIndex];
    }
  });


  // Sichtbare Pfeilbuttons (links/rechts)
  document.getElementById("prevBtn").addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + modalImages.length) % modalImages.length;
    modalImg.src = modalImages[currentIndex];
  });

  document.getElementById("nextBtn").addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % modalImages.length;
    modalImg.src = modalImages[currentIndex];
  });

});
