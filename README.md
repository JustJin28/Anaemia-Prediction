# Anemia Prediction Model

This repository contains a comprehensive data analysis and machine learning project aimed at predicting anemia in patients using various medical features. The project showcases data exploration, feature engineering, model building, and evaluation to provide accurate and actionable predictions.

## Project Overview

Anemia is a common condition characterized by a lack of healthy red blood cells. This project uses a dataset with patient information to build a model that predicts whether a patient is anemic based on their medical data.

## Dataset

The dataset includes the following columns:
- `Number`: Unique identifier for each entry
- `Sex`: Sex of the patient (M/F)
- `%Red Pixel`: Percentage of red pixels
- `%Green Pixel`: Percentage of green pixels
- `%Blue Pixel`: Percentage of blue pixels
- `Hb`: Hemoglobin level
- `Anaemic`: Indicates whether the patient is anemic (Yes/No)

## Project Structure

The project is divided into the following sections:

1. **Data Exploration and Cleaning**: 
   - Summary statistics and distribution plots for numerical features.
   - Handling missing values and encoding categorical variables.

2. **Feature Engineering**: 
   - Scaling numerical features.

3. **Model Building**:
   - Implementing k-Nearest Neighbors (k-NN) classifier.
   - Tuning hyperparameters and evaluating model performance.
   - Implementing additional models like logistic regression and neural networks.

4. **Model Evaluation**:
   - Confusion matrix and classification report to analyze precision, recall, and F1-score.

## How to Use

### Prerequisites

- Python 3.6+
- Virtual environment (recommended)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

### Create and activate a virtual environment  
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install the required packages 
pip install -r requirements.txt

### Running the project

**Data Preparation and EDA:**
- Run the Jupyter notebook data_exploration_and_cleaning.ipynb to explore and clean the data. 
- Model Building and Evaluation:
- Run the Jupyter notebook model_building_and_evaluation.ipynb to build and evaluate different models.

### Contributing
If you would like to contribute to this project, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License. See the LICENSE file for details.