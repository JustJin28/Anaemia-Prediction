# Anemia Prediction Model

## 1. Introduction
Anemia is a condition characterized by a lack of healthy red blood cells. This project aims to develop a machine learning model to predict anemia in patients using various medical features. The primary objective is to minimize false negatives to ensure accurate detection of anemic patients.

## 2. Data Description
### Dataset
The dataset includes the following columns:
- `Number`: Unique identifier for each entry
- `Sex`: Sex of the patient (M/F)
- `%Red Pixel`: Percentage of red pixels
- `%Green Pixel`: Percentage of green pixels
- `%Blue Pixel`: Percentage of blue pixels
- `Hb`: Hemoglobin level
- `Anaemic`: Indicates whether the patient is anemic (Yes/No)

### Initial Analysis
Basic statistics and visualizations of the data were conducted to understand the distribution and identify any anomalies.

## 3. Data Preprocessing
### Cleaning
- Handled missing values by imputing with mean for numerical features and mode for categorical features.
- One-hot encoded the `Sex` column.

### Feature Engineering
- Scaled numerical features using `StandardScaler`.

## 4. Model Building and Tuning
### Model Selection
- Logistic Regression
- Neural Network (MLPClassifier)

### Hyperparameter Tuning
- Used `GridSearchCV` for hyperparameter tuning.
- Logistic Regression: Tuned `C`, `penalty`, and `solver`.
- Neural Network: Tuned `hidden_layer_sizes`, `max_iter`, `alpha`, `learning_rate_init`, `learning_rate`, and `solver`.

## 5. Model Comparison and Results
### Performance Metrics
- Evaluated models using accuracy, precision, recall, F1-score, and ROC AUC.

### Visualizations
- **ROC Curve**:
  ![ROC Curve](roc_curve.png)

  The ROC curve shows the trade-off between true positive rate and false positive rate for both logistic regression and neural network models. The AUC values indicate excellent performance for both models:
  - Logistic Regression (AUC = 0.96)
  - Neural Network (AUC = 0.97)

### Logistic Regression Coefficients
The coefficients for the logistic regression model indicate the importance of each feature in predicting anemia:

| Feature       | Coefficient |
|---------------|-------------|
| Number        | 0.023533    |
| %Red Pixel    | -0.388539   |
| %Green Pixel  | 1.401409    |
| %Blue Pixel   | -0.587886   |
| Hb            | -2.907277   |
| Sex_F         | 0.396294    |
| Sex_M         | -0.170344   |

## 6. Model Interpretation
### Feature Importance
Used SHAP to interpret the models and identify the most influential features.

### Insights
Discussed insights gained from the interpretation, such as the impact of hemoglobin levels on the prediction.

## 7. Conclusion and Future Work
### Summary
The neural network and logistic regression models both performed well, with an accuracy of 88%. The models effectively minimized false negatives.

### Future Work
- Explore additional models and techniques to further improve performance.
- Collect more data to enhance the model's robustness.
- Implement the model in a clinical setting for real-time anemia prediction.

## Appendix
### Files in the Directory
- `data/`: Directory containing the dataset.
- `notebooks/`: Jupyter notebooks for data analysis, model building, and evaluation.
- `models/`: Directory containing saved models (`logistic_regression_model.pkl`, `neural_network_model.pkl`).
- `README.md`: This documentation file.