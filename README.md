# Crop Classification with Machine Learning

This project focuses on classifying different crop types using various machine learning models. The dataset consists of features related to crop types and is used to train and evaluate models such as Random Forest, Logistic Regression, K-Nearest Neighbors (KNN), Decision Trees, Naive Bayes, and Artificial Neural Networks (ANN).

## Project Overview
The goal of this project is to build and evaluate machine learning models to classify crop types based on features extracted from agricultural data. The models are trained, evaluated, and optimized using hyperparameter tuning and cross-validation techniques. Additionally, techniques like SMOTE (Synthetic Minority Over-sampling Technique) are applied to handle class imbalance and improve model performance.

## Models Used
Random Forest Classifier
Logistic Regression
K-Nearest Neighbors (KNN)
Decision Tree Classifier
Naive Bayes
Artificial Neural Network (ANN)

## Table of Contents

- [Crop Classification with Random Forest and SMOTE](#crop-classification-with-random-forest-and-smote)
- [Table of Contents](#table-of-contents)
  - [Datasets Used](#datasets-used)
  - [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Install Dependencies](#install-dependencies)
- [Web Service](#web-service)
  - [Running the Service](#running-the-service)
  - [API Endpoints](#api-endpoints)
  - [Model Training and Testing](#model-training-and-testing)
    - [Training](#training)
    - [Evaluation](#evaluation)

## Datasets Used

The dataset used for training and testing the model includes crop information from Winnipeg. Features include soil type, climate data, and other agronomic details.

The dataset contains various features describing crop characteristics. The classes are as follows:

Class 1: Corn
Class 2: Wheat
Class 3: Soybeans
Class 4: Canola
Class 5: Peas
Class 6: Oats
Class 7: Barley

## Prerequisites

- Python 3.8 or higher
- pip
- Virtual Environment (recommended)

## Setup

1. Clone the Repository: Clone this repository to a folder of your choice.

    ```bash
    git clone https://github.com/Abshir112/Crop_Classification_Project
    ```

2. Navigate to the Project Folder: Move into the cloned project directory.

    ```bash
    cd Crop_Classification_Project
    ```

3. Virtual Environment (Recommended): It's often best to create a virtual environment to isolate package dependencies. To create a virtual environment, run the following command:

    ```bash
    python3 -m venv .venv
    ```

To activate the virtual environment, run:

- Linux/Mac:

    ```bash
    source .venv/bin/activate
    ```

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

### Install Dependencies

Install the necessary packages by running the following command:

```bash
pip install -r requirements.txt
```

> Ensure the `requirements.txt` file includes all necessary dependencies.

## Web Service

The web service is built using FastAPI and provides real-time inferences for crop classification.

### Running the Service

To run the web service on your local machine, execute:

```bash
uvicorn api:app --reload
```

This will start the FastAPI server, and you can access the API documentation at <http://127.0.0.1:8000/docs>.

### API Endpoints

- Predict: POST /predict/
  - Accepts a JSON object with crop features and returns the predicted crop type.

For detailed documentation, refer to the FastAPI-generated documentation at <http://127.0.0.1:8000/docs>.

## Model Training and Testing

The model is trained on a preprocessed dataset, including scaling and balancing, and evaluated for accuracy and robustness.

### Training

The model training includes:

- **Preprocessing**:
  - Missing value imputation using column means.
  - Scaling features with `StandardScaler`.
  - Handling imbalanced classes with SMOTE.

- **Training Algorithm**:
  - A `RandomForestClassifier` with balanced class weights to enhance predictions for minority classes.

- **Pickle Serialization**:
  - The trained Random Forest model and scaler are saved as `.pkl` files for deployment.

### Evaluation

Evaluation includes metrics such as:

- **Accuracy**: Overall correctness of predictions.
- **Confusion Matrix**: Insight into class-wise performance.
- **Precision/Recall/F1-Score**: Ensuring balanced performance for all crop classes.


## User Interface for Predictions

The web-based interface for predictions is hosted [here](https://abshir112.github.io/Crop_Classification_Project/). Users can input crop-related features and receive predictions directly through this interface.

## Conclusion
In this project, we evaluated several machine learning models for crop classification. The models showed varying performance, with Artificial Neural Network (ANN) performing the best with an accuracy of 99.76%, followed closely by K-Nearest Neighbors (KNN) at 99.71%. Random Forest also performed excellently, achieving an accuracy of 99.63%, and was chosen as the preferred model due to its strong predictive power.

Other models, such as Logistic Regression and Decision Trees, also demonstrated solid performance with accuracies of 99.01% and 98.82%, respectively. Naive Bayes, however, lagged behind with an accuracy of 91.61%, indicating it struggled with classifying the crop types compared to the other models.

Based on these results, Random Forest was selected for its ability to effectively predict crop types and its high accuracy across different crops


## Contributors

- **Abshir Muhumed Abdi**  [GitHub](https://github.com/Abshir112) 
- **Lakshmi Vishal Hayagrivan**
  [GitHub](https://github.com/lakshmivishal9496)  





