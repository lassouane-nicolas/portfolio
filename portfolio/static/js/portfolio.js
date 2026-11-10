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
