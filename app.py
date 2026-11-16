import pickle
import streamlit as st

st.title("☕ Starbucks Calorie Predictor")
st.write("Apni values enter kar ke Starbucks item ki calories predict karein!")

# Exact model file ka naam jo aap ki GitHub par mojood hai
model_filename = 'starbucks_model_20261116_130011.pkl'

# Model load karna
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# User Inputs (Sliders)
fat = st.slider('Total Fat (g)', 0.0, 50.0, 5.0)
sugar = st.slider('Sugars (g)', 0.0, 100.0, 15.0)
protein = st.slider('Protein (g)', 0.0, 40.0, 5.0)
carbs = st.slider('Total Carbohydrates (g)', 0.0, 100.0, 20.0)

if st.button('Predict Calories'):
    input_data = [[fat, sugar, protein, carbs]]
    prediction = model.predict(input_data)
    st.success(f"🌟 Predicted Calories: **{round(prediction[0], 2)} kcal**")
