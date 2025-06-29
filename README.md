# 🚗 Car Price Prediction using Machine Learning

This project aims to predict the **price of used cars** based on various features like make, model, engine specifications, and mileage. It uses a **Linear Regression** model to estimate prices, making it a simple but effective baseline solution.

## 📁 Project Structure

```
Car_Price_Prediction_Professional.ipynb  # Jupyter Notebook with full ML pipeline
final_car_with_performance.csv                   # Dataset used
requirements.txt                         # Python dependencies
README.md                                # Project documentation
```

## 📊 Features Used

- Name
- Model
- Variant
- Ex-Showroom Price
- Displacement
- Cylinders
- Fuel Type
- Ground Clearance
- Power
- Torque
- Type
- ARAI Certified Mileage

## 📦 Libraries Used

- pandas
- numpy
- scikit-learn
- joblib (for saving model)

## 🔍 Machine Learning Model

- **Model Used**: RandomForestRegressor  
- **Target Variable**: Ex-Showroom Price  
- **Evaluation Metric**: R² Score (coefficient of determination)

## ✅ Results

- 📈 The model provides a basic estimation of car prices using easily available car features.
- 📊 Accuracy (R² Score): 0.88 (88%)


## 📌 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/car-price-prediction.git
   cd car-price-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook:
   ```bash
   jupyter notebook Car_Price_Prediction_Professional.ipynb
   ```

## 🧠 Author

**Parth Vinay Bhagwat**  
[LinkedIn](https://www.linkedin.com/in/parthbhagwat/) | [GitHub](https://github.com/parthbhagwat22)
