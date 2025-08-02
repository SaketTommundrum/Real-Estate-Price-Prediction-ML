import os
from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Global variables to store model and columns
__model = None
__data_columns = None
__locations = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    try:
        with open("columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

        if __model is None:
            with open('banglore_home_prices_model.pickle', 'rb') as f:
                __model = pickle.load(f)
        print("loading saved artifacts...done")
    except Exception as e:
        print(f"Error loading artifacts: {str(e)}")
        raise e

# Load artifacts when the module is imported (for Gunicorn)
load_saved_artifacts()

def get_estimated_price(location, sqft, bhk, bath):
    if __data_columns is None or __model is None:
        return None
        
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    predicted_price = round(__model.predict([x])[0], 2)
    
    # Return "Not Available" if prediction is negative
    if predicted_price <= 0:
        return "Not Available"
    
    return predicted_price

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': __model is not None,
        'columns_loaded': __data_columns is not None
    })

@app.route('/get_location_names', methods=['GET'])
def get_location_names_for_http():
    response = jsonify({
        'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = get_estimated_price(location, total_sqft, bhk, bath)
        
        if estimated_price is None:
            return jsonify({'error': 'Model not loaded properly'}), 500

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    # load_saved_artifacts() # Already called during module import
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
