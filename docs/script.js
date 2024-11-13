document.getElementById("prediction-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const featuresInput = document.getElementById("features").value;
    const featuresArray = featuresInput.split(",").map(Number);

    try {
        const response = await fetch("https://crop-classification-project.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ features: featuresArray }),
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById("prediction-result").innerText = `Prediction: ${result.prediction}`;
        } else {
            const error = await response.json();
            document.getElementById("prediction-result").innerText = `Error: ${error.detail}`;
        }
    } catch (error) {
        document.getElementById("prediction-result").innerText = `Error: ${error.message}`;
    }
});
