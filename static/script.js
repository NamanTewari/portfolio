
document.addEventListener("DOMContentLoaded", function () {
    const githubLinks = document.querySelectorAll(".github-link");

    githubLinks.forEach(function (btn) {
        btn.addEventListener("click", function () {
            window.open("https://github.com/NamanTewari/Chicken_disease_end_to_end", "_blank");
        });
    });
});

function openGmail() {
    const email = "namantewari2517@gmail.com";
    const subject = "Contact from Portfolio";
    const body = "Hi Naman,I'm interested in connecting with you.";
    
    const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${email}&su=${subject}&body=${body}`;
    window.open(gmailUrl, "_blank");
  }