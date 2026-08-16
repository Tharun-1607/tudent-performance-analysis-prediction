document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form[action^='/delete/']").forEach(form => {
    form.addEventListener("submit", e => {
      if (!confirm("Delete this transaction?")) e.preventDefault();
    });
  });
});
