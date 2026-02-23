import streamlit as st
import pandas as pd
import numpy as np

st.title("Personalised Workout & Diet Planner with AI")

age = st.number_input("Enter Age")
weight = st.number_input("Enter Weight (kg)")
height = st.number_input("Enter Height (m)")
goal = st.selectbox("Select Goal", ["Weight Loss", "Muscle Gain", "Maintain"])

if st.button("Generate Plan"):
    bmi = weight / (height ** 2)
    st.write("Your BMI:", round(bmi, 2))
    
    if goal == "Weight Loss":
        st.write("Workout: Cardio + HIIT (5 days/week)")
        st.write("Diet: Low calorie, high protein diet")
        
    elif goal == "Muscle Gain":
        st.write("Workout: Strength training (4-5 days/week)")
        st.write("Diet: High protein, calorie surplus")
        
    else:
        st.write("Workout: Mixed training (3-4 days/week)")
        st.write("Diet: Balanced maintenance diet")
