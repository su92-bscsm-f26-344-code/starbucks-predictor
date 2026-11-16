import pickle
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title='Starbucks Calorie Level Predictor', page_icon='☕', layout='centered'
)

# Neumorphism Dark UI CSS Styling
st.markdown(
    """
    <style>
    /* Main Background */
    .stApp {
        background-color: #1e2229;
        color: #ffffff;
    }
    
    /* Input Sliders & Text Styling */
    .stSlider label, p, h3 {
        color: #d1d5db !important;
    }

    /* Buttons Styling */
    .stButton>button {
        width: 100%;
        background-color: #262b35;
        color: #ffffff;
        border: none;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 6px 6px 12px #14171c, -6px -6px 12px #383f4e;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2e3542;
        box-shadow: inset 4px 4px 8px #14171c, inset -4px -4px 8px #383f4e;
        color: #f3f4f6;
    }

    /* Success Box Styling */
    .stSuccess {
        background-color: #262b35 !important;
        color: #4ade80 !important;
        border-radius: 12px;
        box-shadow: inset 3px 3px 6px #14171c, inset -3px -3px 6px #383f4e;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header & Title
st.markdown(
    "<h1 style='text-align: center; color: #f3f4f6;'>☕ Starbucks Calorie Predictor</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #9ca3af;'>Enter a drink's fat, sugar, protein and carbs to predict its calories using a Decision Tree model.</p>",
    unsafe_allow_html=True,
)

st.markdown('---')

# Load Model
model_filename = 'starbucks_model_20261116_130011.pkl'
with open(model_filename, 'rb') as file:
  model = pickle.load(file)

# User Inputs (Sliders)
fat = st.slider('Total Fat (g)', 0.0, 50.0, 5.0)
sugar = st.slider('Sugars (g)', 0.0, 100.0, 15.0)
protein = st.slider('Protein (g)', 0.0, 40.0, 5.0)
carbs = st.slider('Total Carbohydrates (g)', 0.0, 100.0, 20.0)

st.markdown('')

# Prediction Button
if st.button('Predict Calories'):
  input_data = [[fat, sugar, protein, carbs]]
  prediction = model.predict(input_data)
  st.success(f'🌟 Predicted Calories: **{round(prediction[0], 2)} kcal**')
