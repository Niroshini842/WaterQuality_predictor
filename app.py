# Import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

# Load the model and structure
model = joblib.load("ness_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# Page configuration
st.set_page_config(page_title="Water Pollutants Predictor", page_icon="💧", layout="centered")

# Header Section
st.markdown("<h1 style='color:#6A5ACD; text-align:center;'>💧 Water Quality Predictor</h1>", unsafe_allow_html=True)
st.markdown("### 🧪 Predict key water pollutant levels based on Year and Station ID")

# Input Section
col1, col2 = st.columns(2)

with col1:
    year_input = st.number_input("📅 Enter Year", min_value=2000, max_value=2100, value=2022)

with col2:
    station_id = st.text_input("📍 Enter Station ID", value='1')

# Predict Button
if st.button('🔍 Predict'):
    if not station_id.strip():
        st.warning('⚠️ Please enter the Station ID.')
    else:
        with st.spinner('Predicting pollutant levels...'):
            # Prepare the input
            input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
            input_encoded = pd.get_dummies(input_df, columns=['id'])

            # Align with model columns
            for col in model_cols:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0
            input_encoded = input_encoded[model_cols]

            # Predict
            predicted_pollutants = model.predict(input_encoded)[0]
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
            results = []

            # Define caution status function
            def pollutant_status(pollutant, value):
                thresholds = {
                    'O2': (5.0, 2.0),
                    'NO3': (45, 70),
                    'NO2': (3.0, 5.0),
                    'SO4': (200, 400),
                    'PO4': (0.1, 0.5),
                    'CL': (250, 400)
                }
                safe, caution = thresholds.get(pollutant, (0, 0))
                if value <= safe:
                    return "🟢 Safe"
                elif value <= caution:
                    return "🟡 Caution"
                else:
                    return "🔴 Hazard"

            # Build results table
            for p, val in zip(pollutants, predicted_pollutants):
                status = pollutant_status(p, val)
                results.append({'Pollutant': p, 'Value (mg/L)': round(val, 2), 'Status': status})

            # Display the table
            results_df = pd.DataFrame(results)
            st.subheader(f"Predicted pollutant levels for Station ID '{station_id}' in {year_input}:")
            st.dataframe(results_df, use_container_width=True)

        # Convert to CSV and provide download
        csv_data = results_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Report as CSV",
            data=csv_data,
            file_name=f"pollution_report_{station_id}_{year_input}.csv",
            mime='text/csv'
        )
