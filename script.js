// Simple JS for future interactivity
document.addEventListener("DOMContentLoaded", () => {
  console.log("Portfolio Loaded Successfully!");
});

function checkPassword() {
  let password = document.getElementById('password').value;
  let strength = 0;
  if(password.length >= 8) strength++;
  if(/[A-Z]/.test(password)) strength++;
  if(/[0-9]/.test(password)) strength++;
  if(/[@$!%*?&]/.test(password)) strength++;
  
  let msg = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"][strength];
  document.getElementById('result').innerText = "Strength: " + msg;
}



