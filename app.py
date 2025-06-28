import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# === Load files ===
model = joblib.load("car_price_model.pkl")
le_fuel = joblib.load("fuel_encoder.pkl")
le_type = joblib.load("type_encoder.pkl")
df = pd.read_csv("final_car_with_performance.csv")

# === Performance to BHP mapping ===
performance_bhp_map = {
    'Low': 62,
    'Medium': 92,
    'High': 135
}

# === Estimate weight based on CC ===
def estimate_weight(cc):
    if cc <= 1000:
        return 850
    elif cc <= 1500:
        return 1000
    elif cc <= 2000:
        return 1250
    else:
        return 1500

# === Streamlit Page Config ===
st.set_page_config(layout="centered")
st.markdown("""
    <style>
        body { font-family: 'Segoe UI', sans-serif; }
        .center-title {
            text-align: center;
            font-weight: bold;
            font-size: 32px;
            margin-bottom: 10px;
        }
        .prediction {
            font-size: 26px;
            color: green;
            font-weight: bold;
        }
        .sub {
            font-size: 20px;
            font-weight: 600;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# === Title ===
st.markdown("<div class='center-title'>🚘 Car Price Predictor & Recommender</div>", unsafe_allow_html=True)

# === Input Form ===
with st.form("car_form"):
    col1, col2, col3 = st.columns([1.2, 1.2, 1.2])

    with col1:
        cc = st.number_input("🔧 Engine CC", min_value=600, max_value=5000, value=1200, step=50)

    with col2:
        # Cylinder rule: <=1000 → [3,4]; >1000 → [4]
        cylinders = st.selectbox("⚙️ Cylinders", [3, 4] if cc <= 1000 else [4])

    with col3:
        fuel_type = st.selectbox("⛽ Fuel Type", le_fuel.classes_)

    col4, col5, col6 = st.columns([1.2, 1.2, 1.2])

    with col4:
        ground_clearance = st.number_input("🚗 Ground Clearance (mm)", min_value=100, max_value=300, value=170)

    with col5:
        mileage = st.number_input("⛽ Mileage (km/l)", min_value=5.0, max_value=40.0, value=18.0)

    with col6:
        trans_type = st.selectbox("🕹️ Transmission", le_type.classes_)

    performance = st.selectbox("💥 Performance Preference", ['Low', 'Medium', 'High'])

    submitted = st.form_submit_button("🔍 Predict Price")

# === On Submit ===
if submitted:
    bhp = performance_bhp_map[performance]
    weight = estimate_weight(cc)
    fuel_encoded = le_fuel.transform([fuel_type])[0]
    type_encoded = le_type.transform([trans_type])[0]

    X_input = [[cc, cylinders, fuel_encoded, ground_clearance, bhp, mileage, type_encoded, weight]]

    # 🌀 Cool animated loading
    loader = st.empty()
    loading_msgs = [
        "🔧 Starting engine...",
        "⛽ Filling virtual fuel...",
        "⚙️ Calculating torque and BHP...",
        "🧠 Predicting with ML magic...",
        "🚗 Finalizing car price..."
    ]
    for msg in loading_msgs:
        loader.markdown(f"### {msg}")
        time.sleep(0.6)

    predicted_price = model.predict(X_input)[0]
    loader.empty()

    # 💸 Show predicted price
    st.markdown(f"<div class='prediction'>💸 Predicted Ex-Showroom Price: ₹{predicted_price:,.0f}</div>", unsafe_allow_html=True)

    # 🎯 Car Recommendations
    st.markdown("<div class='sub'>🎯 Cars You Might Like in Similar Price Range</div>", unsafe_allow_html=True)

    price_range = 50000
    lower = predicted_price - price_range
    upper = predicted_price + price_range

    recommended = df[
        (df['Ex-Showroom_Price'] >= lower) &
        (df['Ex-Showroom_Price'] <= upper)
    ].copy()

    if not recommended.empty:
        recommended['Price_Diff'] = abs(recommended['Ex-Showroom_Price'] - predicted_price)

        table = recommended[['Name', 'Model', 'Ex-Showroom_Price', 'Fuel_Type', 'BHP', 'Type', 'Price_Diff']] \
            .sort_values(by='Price_Diff') \
            .drop(columns='Price_Diff') \
            .reset_index(drop=True)

        table.columns = ['Car Name', 'Model', 'Price (₹)', 'Fuel Type', 'BHP', 'Transmission']
        table.index += 1

        st.dataframe(table.head(5), use_container_width=True)
    else:
        st.warning("⚠️ No similar cars found in the predicted price range.")
