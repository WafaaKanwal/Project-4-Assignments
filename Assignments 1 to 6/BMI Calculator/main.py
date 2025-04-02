import streamlit as st
import time

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg)", 40, 200, 70)

bmi = weight / ((height/100)**2)

st.write(f"Calculating your BMI...")
time.sleep(1)

st.write(f"Your BMI is **{bmi:.2f}**")

if bmi < 18.5:
    st.markdown("<span style='color: blue; font-size: 18px;'>Underweight 🏋️‍♂️</span>", unsafe_allow_html=True)
elif 18.5 <= bmi < 24.9:
    st.markdown("<span style='color: green; font-size: 18px;'>Normal weight ✅</span>", unsafe_allow_html=True)
elif 25 <= bmi < 29.9:
    st.markdown("<span style='color: orange; font-size: 18px;'>Overweight ⚠️</span>", unsafe_allow_html=True)
else:
    st.markdown("<span style='color: red; font-size: 18px;'>Obesity ❌</span>", unsafe_allow_html=True)

st.write("### BMI Categories ###")
st.write("-- **Underweight:** BMI less than 18.5")
st.write("-- **Normal weight:** BMI between 18.5 and 24.9")
st.write("-- **Overweight:** BMI between 25 and 29.9")
st.write("-- **Obesity:** BMI of 30 or greater")

st.write("💡 Maintain a balanced diet and exercise regularly for a healthy BMI!")