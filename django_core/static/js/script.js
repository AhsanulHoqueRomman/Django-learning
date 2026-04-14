// CONTACT FORM
function sendMsg() {
    alert("Message sent successfully!");
    return false; // prevent page reload
}

// SMOOTH SCROLL (for future anchors)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// SIMPLE ANIMATION ON SCROLL
const cards = document.querySelectorAll(".card");

window.addEventListener("scroll", () => {
    cards.forEach(card => {
        const position = card.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 50) {
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }
    });
});

// INITIAL STATE FOR ANIMATION
cards.forEach(card => {
    card.style.opacity = 0;
    card.style.transform = "translateY(50px)";
    card.style.transition = "0.5s";
});