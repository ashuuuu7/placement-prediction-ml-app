import streamlit as st
import pandas as pd
import joblib
model = joblib.load("Ashutosh's_Placement_Prediction")
scaler = joblib.load("scaler.pkl")
st.title("Placement Prediction App")
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0)
internships = st.number_input("Internships", min_value=0, max_value=2)
projects = st.number_input("Projects", min_value=0, max_value=3)
certifications = st.number_input("Workshops / Certifications", min_value=0, max_value=3)
aptitude = st.number_input("Aptitude Test Score", min_value=0, max_value=100)
softskills = st.number_input("Soft Skills Rating", min_value=0.0, max_value=5.0)
extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])
placementtraining = st.selectbox("Placement Training", ["No", "Yes"])
ssc = st.number_input("SSC Marks", min_value=0, max_value=100)
hsc = st.number_input("HSC Marks", min_value=0, max_value=100)
if extracurricular == "Yes":
    extracurricular = 1
else:
    extracurricular = 0
if placementtraining == "Yes":
    placementtraining = 1
else:
    placementtraining = 0
input_data = pd.DataFrame([[cgpa, internships, projects, certifications, aptitude, softskills, extracurricular, placementtraining, ssc, hsc]], 
columns=["CGPA", "Internships", "Projects", "Workshops/Certifications", "AptitudeTestScore", "SoftSkillsRating", "ExtracurricularActivities","PlacementTraining", "SSC_Marks", "HSC_Marks"])
scaled_data = scaler.transform(input_data)
if st.button("Predict Placement"):
    prediction = model.predict(scaled_data)
    if prediction[0] == 1:
        st.success("Placed ✅")
    else:
        st.error("Not Placed ❌")