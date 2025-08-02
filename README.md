# Real-Estate-Price-Prediction-ML (https://bangalore-house-price-pred.uc.r.appspot.com)

🏡 **Bangalore House Price Prediction Web Application**

This project uses machine learning techniques to predict house prices in Bangalore based on various housing features. It includes data cleaning, exploratory analysis, feature engineering, model training, and a complete web application for real-time price predictions.

## 📌 Overview

The project consists of:

1. **Data Analysis & Model Training** - Jupyter notebook with complete ML pipeline
2. **Web Application** - Flask-based website for price predictions
3. **Machine Learning Model** - Trained Linear Regression model with feature engineering

## 🌐 Web Application Features

- **Interactive Web Interface** - Modern, responsive design
- **Real-time Predictions** - Get instant price estimates
- **Location Dropdown** - Select from available Bangalore locations
- **Input Validation** - Ensures data quality for predictions
- **Mobile Friendly** - Works on all devices

## ⚙️ Tech Stack

**Backend:**

- Python (Flask, Pandas, NumPy, Scikit-learn)
- Machine Learning: Linear Regression with feature engineering

**Frontend:**

- HTML5, CSS3, JavaScript
- jQuery for AJAX requests
- Responsive design

**Data Processing:**

- Jupyter Notebook
- Matplotlib, Seaborn for visualizations

## 📈 Dataset

The dataset is sourced from Kaggle: **[Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)**

**Dataset Features:**

- **Location** - Area/locality in Bangalore
- **Size** - Number of BHK (bedrooms)
- **Total Square Feet** - Total area of the property
- **Bath** - Number of bathrooms
- **Price** - Property price in lakhs (target variable)

**Data Processing Steps:**

1. Data cleaning and handling missing values
2. Feature engineering (price per sqft, location grouping)
3. Outlier removal using statistical methods
4. One-hot encoding for categorical variables

## 🚀 How to Run

### Prerequisites

```bash
pip install Flask numpy scikit-learn pandas
```

### Running the Web Application

1. Clone the repository
2. Navigate to the project directory
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000`

### Running the Jupyter Notebook

1. Open `House Sales Prediction.ipynb` in Jupyter Lab/Notebook
2. Install required packages if needed
3. Run all cells to reproduce the analysis and train the model

## 📁 Project Structure

```
Real-Estate-Price-Prediction-ML/
├── House Sales Prediction.ipynb    # Main analysis notebook
├── app.py                          # Flask web application
├── templates/
│   └── index.html                  # Web interface
├── banglore_home_prices_model.pickle # Trained model (auto-generated)
├── columns.json                    # Model features (auto-generated)
├── Bengaluru_House_Data.csv       # Dataset (download from Kaggle)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🎯 Model Performance

The final Linear Regression model was selected after comparing multiple algorithms:

- **Linear Regression** - Best performing model
- **Lasso Regression** - Alternative with regularization
- **Decision Tree** - Tree-based approach

The model includes sophisticated feature engineering:

- Price per square feet outlier removal
- Location-based statistical filtering
- Bathroom to bedroom ratio validation

## 🌟 Key Features

- **Data Quality**: Comprehensive data cleaning and outlier removal
- **Feature Engineering**: Smart location grouping and derived features
- **Model Selection**: Grid search with cross-validation
- **Web Interface**: User-friendly prediction interface
- **Error Handling**: Robust error handling in both model and web app

## 📊 Usage Example

**Web Application:**

1. Select location (e.g., "Whitefield", "Koramangala")
2. Enter total square feet (e.g., 1200)
3. Choose BHK (e.g., 2 BHK)
4. Select bathrooms (e.g., 2)
5. Click "Predict Price" to get estimate in lakhs

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.
<img width="498" height="924" alt="image" src="https://github.com/user-attachments/assets/0815a9bd-a956-4e0d-a0b1-f25169fd59f5" />

