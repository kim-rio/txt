document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('loginForm');

  form.addEventListener('submit', function (e) {
    e.preventDefault(); // Stop the browser's default submit popup

    // You can do validation here if you want

    // Submit form programmatically after preventing default
    form.submit();
  });
});
