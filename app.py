import pickle
import streamlit as st

# Model load karein
model_filename = (  # Apni file ka exact naam yahan likhein
    'starbucks_model_20261116.pkl'
)
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

st.setTitle('☕ Starbucks Nutritional Predictor')
st.write(
    'Milk, Sugar, Protein aur Fat ki values enter kar ke prediction check'
    ' karein!'
)

# User Inputs
milk = st.selectbox('Milk Type / Quantity', [0, 1, 2, 3])
sugar = st.slider('Sugar (grams)', 0, 100, 10)
protein = st.slider('Protein (grams)', 0, 50, 5)
fat = st.slider('Fat (grams)', 0, 50, 10)

if st.button('Predict'):
  # Prediction logic
  input_data = [[milk, sugar, protein, fat]]
  prediction = model.predict(input_data)
  st.success(f'Predicted Result: {prediction[0]}')