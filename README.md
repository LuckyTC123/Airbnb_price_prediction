# 🏡 Airbnb Price Prediction using Machine Learning

## 📌 Project Overview
This project focuses on predicting Airbnb listing prices using multiple features such as location, property type, amenities, and host details. By leveraging **data preprocessing techniques** and a **Random Forest Regressor**, the model aims to provide accurate and interpretable price predictions for short-term rental properties.

---

## 🚀 Key Features
- **Data Source**: Airbnb dataset containing property details, host information, and pricing.
- **Feature Engineering**:
  - One-Hot Encoding for categorical variables (e.g., property type, room type, amenities).
  - Handling missing values and scaling numerical features.
- **Modeling**:
  - Implemented **RandomForestRegressor** for robust and non-linear predictions.
  - Hyperparameter tuning for improved accuracy.
- **Evaluation**:
  - Metrics: RMSE, MAE, and R² Score.
  - Cross-validation for generalization.

---

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Libraries**:
  - `pandas`, `numpy` → Data manipulation
  - `scikit-learn` → Machine learning & preprocessing
  - `matplotlib`, `seaborn` → Visualization
- **Model**: Random Forest Regressor

---

## 📊 Workflow
1. **Data Collection**: Load Airbnb dataset.
2. **Data Cleaning**: Handle missing values, duplicates, and outliers.
3. **Feature Engineering**: Apply One-Hot Encoding and transformations.
4. **Model Training**: Train RandomForestRegressor with tuned hyperparameters.
5. **Evaluation**: Assess performance using regression metrics.
6. **Prediction**: Generate price predictions for new listings.

---

## 📈 Results
- Achieved strong predictive performance with Random Forest.
- Feature importance analysis highlights key drivers of Airbnb pricing (e.g., location, property type, number of reviews).
- Visualizations provide insights into pricing trends across different variables.

---

## 🔮 Future Improvements
- Experiment with advanced models (XGBoost, LightGBM).
- Incorporate NLP features from listing descriptions.
- Deploy as a web app using **Streamlit** or **Flask** for interactive predictions.

---

## 📂 Repository Structure
