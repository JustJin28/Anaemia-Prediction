from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the trained models
log_reg_model = joblib.load('logistic_regression_model.pkl')
mlp_model = joblib.load('neural_network_model.pkl')

# Load the scaler used for feature scaling
scaler = joblib.load('scaler.pkl')

# Define the ranges for input variables for validation
input_ranges = {
    '%Red Pixel': (0, 100),
    '%Green Pixel': (0, 100),
    '%Blue Pixel': (0, 100),
    'Hb': (0, 20),
    'Sex': ['M', 'F']
}

@app.route('/')
def home():
    return render_template('index.html', input_ranges=input_ranges)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        features = [
            float(request.form['%Red Pixel']),
            float(request.form['%Green Pixel']),
            float(request.form['%Blue Pixel']),
            float(request.form['Hb']),
            request.form['Sex']
        ]

        # One-hot encode 'Sex' field
        sex_f = 1 if features[4] == 'F' else 0
        sex_m = 1 if features[4] == 'M' else 0
        numerical_features = features[0:4]  # only numerical features
        categorical_features = [sex_f, sex_m]  # one-hot encoded categorical features

        # Print features for debugging
        print("Original Features:", features)
        print("Numerical Features:", numerical_features)
        print("Categorical Features:", categorical_features)

        # Convert numerical features to numpy array and reshape
        numerical_features = np.array(numerical_features).reshape(1, -1)

        # Scale the numerical features
        numerical_features_scaled = scaler.transform(numerical_features)

        # Convert categorical features to numpy array and reshape
        categorical_features = np.array(categorical_features).reshape(1, -1)

        # Combine scaled numerical features with categorical features
        features_scaled = np.hstack((numerical_features_scaled, categorical_features))

        # Print scaled features for debugging
        print("Features Scaled:", features_scaled)

        # Verify the feature length
        expected_num_features = len(numerical_features[0]) + len(categorical_features[0])
        assert features_scaled.shape[1] == expected_num_features, f"Feature length mismatch: expected {expected_num_features}, got {features_scaled.shape[1]}"

        # Get predictions from both models
        log_reg_prediction = log_reg_model.predict(features_scaled)[0]
        mlp_prediction = mlp_model.predict(features_scaled)[0]

        # Convert numeric predictions to Yes/No
        log_reg_result = 'Yes' if log_reg_prediction == 1 else 'No'
        mlp_result = 'Yes' if mlp_prediction == 1 else 'No'

        return render_template('index.html',
                               log_reg_result=log_reg_result,
                               mlp_result=mlp_result,
                               input_ranges=input_ranges)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)