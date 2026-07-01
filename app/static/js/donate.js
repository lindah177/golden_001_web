// Runs as soon as the donate page loads
document.addEventListener("DOMContentLoaded", function () {
  // Set the first button (R50) as active by default
  const firstBtn = document.querySelector(".amount-btn");
  if (firstBtn) firstBtn.classList.add("active");
});

// Called when a preset amount button is clicked
function selectAmount(btn, amount) {
  // Remove active class from all buttons
  document.querySelectorAll(".amount-btn").forEach(function (b) {
    b.classList.remove("active");
  });

  // Add active class to the clicked button
  btn.classList.add("active");

  // Update the input field with the selected amount
  document.getElementById("donate-amount").value = amount;
}

// Called when the Donate button is clicked
async function handleDonate() {
  const amountInput = document.getElementById("donate-amount");
  const messageDiv = document.getElementById("donate-message");
  const amount = parseFloat(amountInput.value);

  // Basic validation
  if (!amount || amount <= 0) {
    showMessage("Please enter a valid amount.", "danger");
    return;
  }

  // Disable the button so they can't click twice
  const submitBtn = document.querySelector(".donate-submit") 
                 || document.querySelector("[onclick='handleDonate()']");
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.textContent = "Processing...";
  }

  try {
    // Send the donation to Flask backend
    const response = await fetch("/donations/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        amount: amount,
        message: "",
        is_anonymous: true,
      }),
    });

    const data = await response.json();

    if (data.success) {
      showMessage(data.message, "success");
      amountInput.value = "";
    } else {
      showMessage("Something went wrong: " + data.error, "danger");
    }

  } catch (error) {
    // This runs if the network request itself failed
    showMessage("Could not connect to the server. Please try again.", "danger");
    console.error("Donation error:", error);

  } finally {
    // Re-enable the button no matter what happened
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.textContent = "Donate";
    }
  }
}

// Helper function to show a coloured message below the form
function showMessage(text, type) {
  const messageDiv = document.getElementById("donate-message");
  messageDiv.innerHTML = `
    <div class="alert alert-${type} mt-3" role="alert">
      ${text}
    </div>
  `;
}