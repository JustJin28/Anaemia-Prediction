# Anaemia Prediction

This project involves building machine learning models to predict anaemia in patients based on several features derived from medical data. The models used include Logistic Regression and a Neural Network. A Flask web application is provided to allow users to input the required features and get predictions.

## Project Structure

- `data_prep.ipynb`: Jupyter notebook containing data preprocessing and model training.
- `app.py`: Flask web application for user interaction and prediction.
- `templates/index.html`: HTML template for the Flask web application.
- `requirements.txt`: List of Python packages required for the project.
- `logistic_regression_model.pkl`: Trained Logistic Regression model.
- `neural_network_model.pkl`: Trained Neural Network model.
- `scaler.pkl`: Scaler used for feature scaling.

## Features

- `%Red Pixel`
- `%Green Pixel`
- `%Blue Pixel`
- `Hb`
- `Sex`

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/anaemia-prediction.git
    cd anaemia-prediction
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the necessary model files (`logistic_regression_model.pkl`, `neural_network_model.pkl`, `scaler.pkl`) are in the project directory.

### Running the Application

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the web application.

### Usage

- Enter the values for `%Red Pixel`, `%Green Pixel`, `%Blue Pixel`, `Hb`, and `Sex`.
- Click "Predict" to get predictions from both the Logistic Regression and Neural Network models.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.