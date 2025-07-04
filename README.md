# WaterQuality_predictor
The Project aims to Predict Quality of Water based on few metrics using machine learning techniques specifically MultiOutputRegressor wrapped around a RandomForestRegressor.Then classify the water into categories by quality level.

# Overview Of Predicted Parameters
 Model predicts concentration (mg/L) of pollutants:
* Nutrients & Salts: NO₃, NO₂, SO₄, PO₄, CL
* Oxygen Metrics: O₂, BOD5
* Toxins: NH₄
* Physical Content: Colloids

Multi-target regression allows simultaneous prediction of these pollutants from a single input instance.

# Technoogy Used
* Python 3.12
* Pandas, NumPy – Data handling
* Scikit-learn – Machine learning model and evaluation
* Google Colab – Interactive experimentation

# Predicted Water Quality Parameters
The model predicts multiple water quality parameters such as:

* NH4
* BOD5 (BSK5)
* Colloids
* O2, NO3, NO2, SO4, PO4 and
* CL

# Model Performance
The model was evaluated using:
* R² Score
* Mean Squared Error (MSE)


Performance was acceptable across all parameters


# Internship Details
* Internship Type: AICTE Virtual Internship - Edunet Foundation
* Sponsor: Shell
* Duration: June 2025 (4 weeks)
* Focus Area: Artificial Intelligence & Machine Learning in Green Technology

