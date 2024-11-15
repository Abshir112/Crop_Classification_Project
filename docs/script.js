document.getElementById("prediction-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const featuresInput = document.getElementById("features").value;
    const featuresArray = featuresInput.split(",").map(item => Number(item.trim()));

     // Define the crop names mapping
     const cropNames = {
        1: 'Corn',
        2: 'Wheat',
        3: 'Soybeans',
        4: 'Canola',
        5: 'Peas',
        6: 'Oats',
        7: 'Barley'
    };
    
    // Clear any previous message styles
    const resultElement = document.getElementById("prediction-result");
    resultElement.classList.remove("error");

    // Check if the input has exactly 174 features
    if (featuresArray.length !== 174) {
        resultElement.innerText = `Error: You entered ${featuresArray.length} features. The model expects 174 comma-separated features.`;
        resultElement.classList.add("error");
        return;
    }

    // Check if all entries are valid numbers
    if (featuresArray.some(isNaN)) {
        resultElement.innerText = "Error: Please make sure all features are valid numbers.";
        resultElement.classList.add("error");
        return;
    }

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
            const cropId = result.prediction;
            const cropName = cropNames[cropId] || "Unknown Crop"; // Map prediction to crop name
            resultElement.innerText = `Prediction: ${cropName}`;
        } else {
            const error = await response.json();
            const errorMessage = typeof error.detail === 'string' ? error.detail : JSON.stringify(error.detail);
            resultElement.innerText = `Error: ${errorMessage}`;
            resultElement.classList.add("error");
        }
    } catch (error) {
        resultElement.innerText = `Error: ${error.message}`;
        resultElement.classList.add("error");
    }
});
