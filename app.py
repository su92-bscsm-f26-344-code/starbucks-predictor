import pickle
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title='Starbucks Calorie Predictor', page_icon='☕', layout='centered'
)

# Modern Glassmorphism & Sleek Dashboard CSS Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Global Font & Modern Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #f8fafc;
    }

    /* Header Banner Styling */
    .main-header {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .main-header h1 {
        color: #ffffff;
        font-weight: 700;
        font-size: 2rem;
        margin-bottom: 8px;
    }

    .main-header p {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    /* Sliders Styling */
    .stSlider label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* Modern Glowing Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 12px 20px;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.6);
        transform: translateY(-2px);
    }

    /* Sleek Success Box */
    .stSuccess {
        background: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        color: #34d399 !important;
        border-radius: 14px;
        padding: 15px;
        backdrop-filter: blur(10px);
        font-weight: 600;
        font-size: 1.2rem;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header Section
st.markdown(
    """
    <div class="main-header">
        <h1>☕ Starbucks Calorie Predictor</h1>
        <p>AI-Powered Decision Tree Model for Smart Nutritional Insights</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Load Model
model_filename = 'starbucks_model_20261116_130011.pkl'
with open(model_filename, 'rb') as file:
  model = pickle.load(file)

# Modern 2-Column Layout for Inputs (Looks like a pro dashboard)
col1, col2 = st.columns(2, gap='medium')

with col1:
  fat = st.slider('Total Fat (g)', 0.0, 50.0, 5.0)
  protein = st.slider('Protein (g)', 0.0, 40.0, 5.0)

with col2:
  sugar = st.slider('Sugars (g)', 0.0, 100.0, 15.0)
  carbs = st.slider('Total Carbohydrates (g)', 0.0, 100.0, 20.0)

st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)

# Prediction Button & Result
if st.button('✨ Predict Calories'):
  input_data = [[fat, sugar, protein, carbs]]
  prediction = model.predict(input_data)
  st.success(f'🚀 Predicted Energy: **{round(prediction[0], 2)} kcal**')
