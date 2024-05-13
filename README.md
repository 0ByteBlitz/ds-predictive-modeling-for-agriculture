# Predictive Modeling for Agriculture using Scikit-learn

## Introduction

This is a simple example of how to use scikit-learn to create a predictive model for agriculture. The goal is to predict which crop will have the highest yield based on various soil measurements.

The dataset used for this project is called `soil_measures.csv` and it contains the following columns:

- `"N"`: Nitrogen content ratio in the soil
- `"P"`: Phosphorous content ratio in the soil
- `"K"`: Potassium content ratio in the soil
- `"pH"`: pH value of the soil
- `"crop"`: categorical values representing various crops (target variable)

Each row in the dataset represents different soil measurements for a specific field. Based on these measurements, the optimal crop for that field is determined by the value in the `"crop"` column.

In this project, we will build multi-class classification models to identify the most important feature for predictive performance. We will also build a simple Logistic Regression model to predict the crop based on the soil measurements and use the model to make predictions on the dataset.
