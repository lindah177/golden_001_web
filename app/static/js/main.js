document.addEventListener("DOMContentLoaded", function () {

  // Auto-dismiss flash messages after 4 seconds
  const alerts = document.querySelectorAll(".alert-dismissible");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, 4000);
  });

  // Smooth scroll for any anchor link on the page
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // Highlight the active nav link based on current URL
  const currentPath = window.location.pathname;
  document.querySelectorAll(".nav-link").forEach(function (link) {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("fw-bold");
      link.style.color = "#F5A623";
    }
  });

});