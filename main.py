# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
import os


# Define input data model
class InputData(BaseModel):
    features: list[float]


# Initialize FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load models
def load_model(path):
    with open(path, "rb") as file:
        return pickle.load(file)


# Paths to models
pca_path = os.path.join("Backend", "models", "PCA_model.pkl")
dt_model_path = os.path.join("Backend", "models", "DTR_Classifier.pkl")
ANN_model_path = os.path.join("Backend", "models", "ANN_Classifier.pkl")


# Load models
pca = load_model(pca_path)
dt_model = load_model(dt_model_path)
ANN_model = load_model(ANN_model_path)


@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post("/predict")
async def predict(data: InputData):
    try:
        # Convert input data to numpy array
        features = np.array(data.features).reshape(1, -1)
    
        # Apply PCA transformation
        features_pca = pca.transform(features)
    
        # Perform prediction (Decision Tree Model as default)
        prediction = dt_model.predict(features_pca)
        # Optionally switch to ANN model by uncommenting:
        # prediction = ANN_model.predict(features_pca)

        return {"prediction": int(prediction[0])}
 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
