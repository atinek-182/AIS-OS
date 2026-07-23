// App.js Interactivity Script
// Used for web speed optimization benchmarking tests.

document.addEventListener("DOMContentLoaded", function () {
    console.log("Interactive speed target site successfully loaded.");

    const ctaButton = document.getElementById("cta-button");

    if (ctaButton) {
        ctaButton.addEventListener("click", function () {
            // Click Handler Trigger
            alert("Hello from the speed optimized sandbox target site!");
            console.log("User successfully triggered the CTA callout action button.");
        });
    }

    // Heavy mock calculation to simulate render-blocking delays (for benchmarking)
    let sum = 0;
    for (let i = 0; i < 100000; i++) {
        sum += i;
    }
    console.log("Calculated mock value: " + sum);
});
