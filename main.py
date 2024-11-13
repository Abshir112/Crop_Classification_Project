# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle
import os

# Load models
pca_path = os.path.join("models", "PCA_model.pkl")
dt_model_path = os.path.join("models", "DTR_Classifier.pkl")
ANN_model_path = os.path.join("models", "ANN_Classifier.pkl")


with open(pca_path, "rb") as pca_file:
    pca = pickle.load(pca_file)
with open(dt_model_path, "rb") as model_file:
    dt_model = pickle.load(model_file)

with open(ANN_model_path, "rb") as model_file:
    ANN_model = pickle.load(model_file)


# Define input data model
class InputData(BaseModel):
    features: list[float]


# Initialize FastAPI app
app = FastAPI()


@app.post("/predict")
async def predict(data: InputData):
    try:
        # Convert input data to numpy array
        features = np.array(data.features).reshape(1, -1)
        print(f"Input shape before PCA: {features.shape}")  # Debugging statement
        
        # Apply PCA transformation
        features_pca = pca.transform(features)
        print(f"Shape after PCA transformation: {features_pca.shape}")  # Debugging statement
        
        # Perform prediction
        prediction = dt_model.predict(features_pca)
        # prediction = ANN_model.predict(features_pca)

        return {"prediction": int(prediction[0])}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
