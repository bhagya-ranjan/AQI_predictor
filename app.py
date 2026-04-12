import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="AQI Predictor", page_icon="🌫️", layout="centered")

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

# AQI Category + Color
def get_aqi_info(aqi):
    if aqi <= 50:
        return "Good ! ", "#00E400"
    elif aqi <= 100:
        return "Satisfactory ", "#9CFF00"
    elif aqi <= 200:
        return "Moderate ", "#FFE600"
    elif aqi <= 300:
        return "Poor ", "#FF7E00"
    elif aqi <= 400:
        return "Very Poor ", "#FF0000"
    else:
        return "Severe ", "#8F3F97"

# Title
st.markdown(
    "<h1 style='text-align: center; color: #00C9A7;'>🌫️ AQI Prediction App</h1>",
    unsafe_allow_html=True
)

st.markdown("### Enter Air Quality Parameters")

# Layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5", value=50.0)
    pm10 = st.number_input("PM10", value=80.0)
    no = st.number_input("NO", value=20.0)
    no2 = st.number_input("NO2", value=30.0)
    nox = st.number_input("NOx", value=40.0)

with col2:
    nh3 = st.number_input("NH3", value=10.0)
    co = st.number_input("CO", value=1.0)
    so2 = st.number_input("SO2", value=15.0)
    o3 = st.number_input("O3", value=25.0)

# Date
st.markdown("### Date Information")
col3, col4, col5 = st.columns(3)

with col3:
    year = st.number_input("Year", value=2020)
with col4:
    month = st.number_input("Month", min_value=1, max_value=12, value=1)
with col5:
    day = st.number_input("Day", min_value=1, max_value=31, value=1)

# City dropdown
cities = sorted([col.replace("City_", "") for col in columns if col.startswith("City_")])
selected_city = st.selectbox("Select City", cities)

# Predict button
if st.button("Predict AQI"):

    input_dict = dict.fromkeys(columns, 0)

    input_dict.update({
        'PM2.5': pm25,
        'PM10': pm10,
        'NO': no,
        'NO2': no2,
        'NOx': nox,
        'NH3': nh3,
        'CO': co,
        'SO2': so2,
        'O3': o3,
        'year': year,
        'month': month,
        'day': day
    })

    city_col = f"City_{selected_city}"
    if city_col in input_dict:
        input_dict[city_col] = 1

    input_df = pd.DataFrame([input_dict])
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]
    category, color = get_aqi_info(prediction)

    # Output
    st.markdown("## Result")

    st.markdown(
        f"""
        <div style="background-color:#111;padding:20px;border-radius:15px;text-align:center;">
            <h2 style="color:{color};">AQI: {prediction:.2f}</h2>
            <h3 style="color:{color};">{category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Description
    st.markdown("### Health Advice")

    if prediction <= 50:
        st.success("Air quality is good. Enjoy outdoor activities!")
    elif prediction <= 100:
        st.info("Air quality is acceptable.")
    elif prediction <= 200:
        st.warning("Sensitive groups should reduce outdoor activity.")
    else:
        st.error("Avoid outdoor activities. Health risk is high!")

# Footer
st.markdown("---")