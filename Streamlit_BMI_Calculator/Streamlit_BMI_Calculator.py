
#------------------------------------------ STREAMLIT BMI CALCULATOR ----------------------------------------------#

import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm): ", 100,250,175)
weight = st.slider("Enter your weight (in kg): ", 40,250,75)

BMI = weight/((height/100)**2)

if st.button("Calculate"):
    st.success(f"Your BMI is {BMI:.2f}.")

st.subheader("BMI Categories")
st.write("> BMI less than 18.5       --> Underweight.")
st.write("> BMI between 18.5 to 24.9 --> Normal Weight")
st.write("> BMI between 25 to 29.9   --> Overweight")
st.write("> BMI 30 or greater        --> Obesity")

st.image(r"https://westmedical.com/wp-content/uploads/2022/12/3932e867ae54709fb3d2b4f4ebebca7e6f8f6ff4-1993x1199-1.jpg")


