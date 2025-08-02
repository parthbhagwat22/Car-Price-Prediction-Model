# 🚗 Used Car Price Prediction Model

A data-driven ML solution to estimate the price of used cars based on real-world features like mileage, engine specs, fuel type, etc. Includes full EDA, preprocessing, and model deployment via Streamlit.

## 🚀 Live Demo  
👉 [Click to View the App](https://carwise-ai.streamlit.app/)

## 📁 Project Structure
Used-Car-Price-Prediction-Model/  
┣ Car_Price_Prediction_Professional.ipynb  # Complete ML pipeline  
┣ final_car_with_performance.csv           # Cleaned dataset  
┣ requirements.txt                         # Project dependencies  
┗ README.md                                # Documentation

## 📊 Features Used
- Name, Model, Variant
- Ex-Showroom Price (target)
- Displacement, Cylinders, Power, Torque
- Fuel Type, Ground Clearance, Mileage
- Type (e.g., SUV, Sedan)

## 🔧 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit

## 🤖 Machine Learning Model
- Model Used: RandomForestRegressor
- Target Variable: Ex-Showroom Price
- Evaluation Metric: R² Score

## ✅ Results
- The model explains **88% of price variance (R² Score = 0.88)**
- Provides reliable baseline estimates for used car pricing
- 

## 🧠 Future Improvements
- Add model explainability using SHAP or LIME
- Include more vehicle features like year of manufacture or number of owners
- Optimize model using hyperparameter tuning
- Add deployment with Docker or on cloud (e.g., AWS/GCP)

## 📄 License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 🙏 Acknowledgements
- Dataset sourced from [Kaggle/car-dekho](https://www.kaggle.com/)
- Inspired by use-cases in automotive ML pricing

---

Thanks for checking out my project! If you like it or have feedback, feel free to connect on [LinkedIn](https://www.linkedin.com/in/parthbhagwat/).

