import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ----------------------------
# Load trained model
# ----------------------------
model = joblib.load("sales_prediction_model.pkl")

# ----------------------------
# App Title
# ----------------------------
st.set_page_config(page_title="Financial Sales Intelligence Platform")

st.title("📊 Financial Sales Intelligence Platform")
st.subheader("AI Sales Prediction System")

st.write("Enter the sales information below and click **Predict Sales**.")

# ----------------------------
# User Inputs
# ----------------------------

segment = st.selectbox(
    "Segment",
    [
        "Channel Partners",
        "Enterprise",
        "Government",
        "Midmarket",
        "Small Business"
    ]
)

country = st.selectbox(
    "Country",
    [
        "Canada",
        "France",
        "Germany",
        "Mexico",
        "United States of America"
    ]
)

product = st.selectbox(
    "Product",
    [
        "Amarilla",
        "Carretera",
        "Montana",
        "Paseo",
        "VTT",
        "Velo"
    ]
)

discount = st.selectbox(
    "Discount Band",
    [
        "No Discount",
        "Low",
        "Medium",
        "High"
    ]
)

units = st.number_input(
    "Units Sold",
    min_value=0.0,
    value=100.0
)

manufacturing = st.number_input(
    "Manufacturing Price",
    min_value=0.0,
    value=10.0
)

sale_price = st.number_input(
    "Sale Price",
    min_value=0.0,
    value=20.0
)

month = st.number_input(
    "Month Number",
    min_value=1,
    max_value=12,
    value=1
)

year = st.number_input(
    "Year",
    min_value=2013,
    max_value=2035,
    value=2014
)

# Convert No Discount back to NaN
if discount == "No Discount":
    discount = np.nan

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict Sales"):

    input_df = pd.DataFrame({
        "Segment": [segment],
        "Country": [country],
        "Product": [product],
        "Discount Band": [discount],
        "Units Sold": [units],
        "Manufacturing Price": [manufacturing],
        "Sale Price": [sale_price],
        "Month Number": [month],
        "Year": [year]
    })

    prediction = model.predict(input_df)

    st.success("Prediction Completed!")

    st.metric(
        label="Predicted Sales",
        value=f"${prediction[0]:,.2f}"
    )