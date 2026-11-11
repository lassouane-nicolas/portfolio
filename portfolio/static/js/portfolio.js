
const mobileMenu = document.querySelector(".mobile-menu");

if (mobileMenu) {
    // Close the mobile menu with Escape and restore keyboard focus.
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && mobileMenu.open) {
            mobileMenu.open = false;
            mobileMenu.querySelector("summary").focus();
        }
    });

    // Close the menu when clicking outside its interactive elements.
    document.addEventListener("click", (event) => {
        if (!mobileMenu.open) {
            return;
        }

        const summary = mobileMenu.querySelector("summary");
        const nav = mobileMenu.querySelector("nav");

        // The backdrop belongs to <details>, so check its children instead.
        if (!summary.contains(event.target) && !nav.contains(event.target)) {
            mobileMenu.open = false;
        }
    });
}

const galleries = document.querySelectorAll(".project-gallery");
const reducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
);

galleries.forEach((gallery) => {
    const slides = Array.from(
        gallery.querySelectorAll(".project-gallery-slide")
    );

    if (slides.length <= 1) {
        return;
    }

    const previousButton = gallery.querySelector(".project-gallery-prev");
    const nextButton = gallery.querySelector(".project-gallery-next");
    const counter = gallery.querySelector(".project-gallery-counter");

    let currentIndex = 0;
    let intervalId = null;
    let isPaused = gallery.matches(":hover");

    function showSlide(index) {
        currentIndex = (index + slides.length) % slides.length;

        slides.forEach((slide, slideIndex) => {
            slide.hidden = slideIndex !== currentIndex;
        });

        if (counter) {
            counter.textContent = `${currentIndex + 1} / ${slides.length}`;
        }
    }

    function stopAutoplay() {
        if (intervalId !== null) {
            clearInterval(intervalId);
            intervalId = null;
        }
    }

    function startAutoplay() {
        stopAutoplay();

        if (isPaused || reducedMotion.matches || document.hidden) {
            return;
        }

        intervalId = setInterval(() => {
            showSlide(currentIndex + 1);
        }, 5000);
    }

    function navigate(direction) {
        showSlide(currentIndex + direction);
        startAutoplay();
    }

    previousButton?.addEventListener("click", () => {
        navigate(-1);
    });

    nextButton?.addEventListener("click", () => {
        navigate(1);
    });

    gallery.addEventListener("mouseenter", () => {
        isPaused = true;
        stopAutoplay();
    });

    gallery.addEventListener("mouseleave", () => {
        isPaused = gallery.contains(document.activeElement);

        if (!isPaused) {
            startAutoplay();
        }
    });

    gallery.addEventListener("focusin", () => {
        isPaused = true;
        stopAutoplay();
    });

    gallery.addEventListener("focusout", (event) => {
        if (!gallery.contains(event.relatedTarget)) {
            isPaused = gallery.matches(":hover");

            if (!isPaused) {
                startAutoplay();
            }
        }
    });

    document.addEventListener("visibilitychange", () => {
        if (document.hidden) {
            stopAutoplay();
        } else {
            startAutoplay();
        }
    });

    reducedMotion.addEventListener("change", startAutoplay);

    showSlide(0);
    startAutoplay();
});
