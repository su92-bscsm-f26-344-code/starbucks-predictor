import pickle
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title='Starbucks Calorie Predictor', page_icon='☕', layout='centered'
)

# Luxury Dark Neumorphism Soft UI CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    /* Main Dark Neumorphic Background */
    .stApp {
        background-color: #21242b;
        font-family: 'Poppins', sans-serif;
        color: #e2e8f0;
    }

    /* Hide default Streamlit header/footer for clean mobile-app look */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Glowing Circular Coffee Cup Avatar */
    .cup-circle {
        width: 130px;
        height: 130px;
        margin: 10px auto 25px auto;
        border-radius: 50%;
        background: #252932;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 62px;
        box-shadow: 
            12px 12px 24px #16181d, 
            -12px -12px 24px #2c3039,
            0 0 35px rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Multi-color Hero Title matching reference */
    .hero-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 16px;
        letter-spacing: -0.5px;
    }
    .title-white { color: #dce4f2; display: block; }
    .title-gold  { color: #b5835a; display: block; }
    .title-blue  { color: #c7d5e8; display: block; }

    /* Subtitle Text */
    .hero-subtitle {
        text-align: center;
        color: #8b95a5;
        font-size: 1.02rem;
        line-height: 1.6;
        max-width: 440px;
        margin: 0 auto 28px auto;
        font-weight: 400;
    }

    /* 3D Embossed Pill Badges Stack */
    .badges-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 14px;
        margin-bottom: 35px;
    }

    .neu-pill {
        background: linear-gradient(145deg, #252830, #1e2027);
        padding: 12px 28px;
        border-radius: 50px;
        color: #e2e8f0;
        font-weight: 600;
        font-size: 0.95rem;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        box-shadow: 
            6px 6px 14px #15171c, 
            -6px -6px 14px #2d313a;
        border: 1px solid rgba(255, 255, 255, 0.06);
        min-width: 220px;
        justify-content: center;
    }

    /* Sliders Styling */
    .stSlider label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* 3D Neumorphic Caramel-Accent Predict Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(145deg, #b5835a, #966844);
        color: #ffffff;
        border: none;
        border-radius: 50px;
        padding: 15px 24px;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 0.5px;
        box-shadow: 
            8px 8px 18px #15171c, 
            -6px -6px 16px #2d313a;
        transition: all 0.25s ease;
        margin-top: 10px;
    }

    .stButton>button:hover {
        background: linear-gradient(145deg, #c49168, #a3724c);
        transform: translateY(-2px);
        box-shadow: 
            10px 10px 22px #121418, 
            -6px -6px 18px #323640;
        color: #ffffff;
    }

    /* Result Card (Inset Neumorphism) */
    .result-card {
        background: #1c1f26;
        border-radius: 24px;
        padding: 24px;
        text-align: center;
        margin-top: 24px;
        box-shadow: 
            inset 6px 6px 14px #13151a, 
            inset -6px -6px 14px #252932;
        border: 1px solid rgba(181, 131, 90, 0.25);
    }
    .result-kcal {
        font-size: 2.2rem;
        font-weight: 800;
        color: #e2e8f0;
        margin: 6px 0;
    }
    .result-badge {
        display: inline-block;
        padding: 6px 18px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-top: 6px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 1. Glowing Coffee Cup Avatar + Multi-color Title + Pill Badges
st.markdown(
    """
    <div class="cup-circle">☕</div>
    
    <div class="hero-title">
        <span class="title-white">Starbucks</span>
        <span class="title-gold">Calorie Level</span>
        <span class="title-blue">Predictor</span>
    </div>

    <div class="hero-subtitle">
        Enter a drink's fat, sugar, protein and carbs. A Decision Tree trained on the full Starbucks menu predicts its exact calories and level.
    </div>

    <div class="badges-container">
        <div class="neu-pill">🎯 High Accuracy Model</div>
        <div class="neu-pill">🌳 Decision Tree</div>
        <div class="neu-pill">☕ 242 Starbucks Drinks</div>
    </div>
""",
    unsafe_allow_html=True,
)

# 2. Load Trained Model
model_filename = 'starbucks_model_20261116_130011.pkl'
with open(model_filename, 'rb') as file:
  model = pickle.load(file)

# 3. Clean 2-Column Sliders
col1, col2 = st.columns(2, gap='large')

with col1:
  fat = st.slider('🧈 Total Fat (g)', 0.0, 50.0, 5.0)
  protein = st.slider('💪 Protein (g)', 0.0, 40.0, 5.0)

with col2:
  sugar = st.slider('🍬 Sugars (g)', 0.0, 100.0, 15.0)
  carbs = st.slider('🌾 Total Carbs (g)', 0.0, 100.0, 20.0)

# 4. Predict Button & Custom Neumorphic Result Card
if st.button('☕ Predict Calorie Level'):
  input_data = [[fat, sugar, protein, carbs]]
  calories = round(float(model.predict(input_data)[0]), 1)

  # Calorie Level Category (Low / Medium / High)
  if calories < 150:
    level_text = '🟢 Low Calorie Drink'
    badge_bg = 'rgba(74, 222, 128, 0.15)'
    badge_color = '#4ade80'
  elif calories <= 300:
    level_text = '🟡 Medium Calorie Drink'
    badge_bg = 'rgba(250, 204, 21, 0.15)'
    badge_color = '#facc15'
  else:
    level_text = '🔴 High Calorie Drink'
    badge_bg = 'rgba(248, 113, 113, 0.15)'
    badge_color = '#f87171'

  st.markdown(
      f"""
        <div class="result-card">
            <div style="color: #8b95a5; font-size: 0.9rem; font-weight: 600;">PREDICTED ENERGY</div>
            <div class="result-kcal">{calories} kcal</div>
            <div class="result-badge" style="background: {badge_bg}; color: {badge_color};">
                {level_text}
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )
