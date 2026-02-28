import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Health Guidance | CardioScan", page_icon="🥗", layout="wide")

# --- 2. PREMIUM UI STYLING (Matching Home Page) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    .guide-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-top: 5px solid #0062FF;
        height: 100%;
        transition: 0.3s;
    }
    .guide-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .icon-circle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        margin-bottom: 15px;
    }
    h2, h3 { color: #1E293B; }
    .section-title { font-weight: 800; color: #1E293B; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
st.title("🥗 Personalized Heart Health Guidance")
st.markdown("Proactive steps to maintain a healthy heart and improve your long-term cardiovascular score.")
st.divider()

# --- 4. GRID LAYOUT FOR GUIDANCE ---

# Row 1: Diet & Exercise
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
        <div class="guide-card">
            <div class="icon-circle" style="background-color: #EBF5FF;">🥗</div>
            <h3 class="section-title">Cardio-Protective Diet</h3>
            <p style='color: #64748B;'>The foundation of heart health starts in the kitchen.</p>
            <ul>
                <li><b>The DASH Diet:</b> Focus on fruits, vegetables, and whole grains.</li>
                <li><b>Reduce Sodium:</b> Aim for less than 2,300mg of salt per day.</li>
                <li><b>Healthy Fats:</b> Switch to Olive Oil, Avocado, and Omega-3 rich Fish.</li>
                <li><b>Zero Trans-Fats:</b> Avoid processed snacks and fried bakery items.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="guide-card">
            <div class="icon-circle" style="background-color: #FFF0F0;">🏃‍♂️</div>
            <h3 class="section-title">Physical Activity Plan</h3>
            <p style='color: #64748B;'>Keep your heart muscle strong with consistent movement.</p>
            <ul>
                <li><b>Moderate Intensity:</b> 150 minutes of brisk walking per week.</li>
                <li><b>Vigorous Activity:</b> 75 minutes of running or swimming per week.</li>
                <li><b>Strength Training:</b> Use weights 2x a week to improve metabolism.</li>
                <li><b>Consistency:</b> Even a 10-minute walk after meals helps lower BP.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)



st.write("##") # Vertical spacing

# Row 2: Sleep, Stress, and Habits
col3, col4, col5 = st.columns(3, gap="medium")

with col3:
    st.markdown("""
        <div class="guide-card">
            <div class="icon-circle" style="background-color: #F0FFF4;">😴</div>
            <h3 class="section-title">Sleep Quality</h3>
            <p style='color: #64748B;'>Sleep allows your heart rate and BP to drop naturally.</p>
            <p>Aim for <b>7-9 hours</b> of high-quality sleep. Poor sleep is linked to high blood pressure and arterial plaque.</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="guide-card">
            <div class="icon-circle" style="background-color: #FAF5FF;">🧘‍♀️</div>
            <h3 class="section-title">Stress Management</h3>
            <p style='color: #64748B;'>High cortisol levels can damage arteries over time.</p>
            <p>Practice <b>Deep Breathing, Meditation, or Yoga</b> for 15 minutes daily to regulate your nervous system.</p>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
        <div class="guide-card">
            <div class="icon-circle" style="background-color: #FFFBEB;">🚫</div>
            <h3 class="section-title">Habit Control</h3>
            <p style='color: #64748B;'>Eliminate toxic factors for immediate results.</p>
            <p><b>Quit Smoking:</b> Heart rate drops 20 mins after quitting. <b>Limit Alcohol:</b> Excess drinking weakens heart muscles.</p>
        </div>
    """, unsafe_allow_html=True)

# --- 5. INTERACTIVE FEATURE: CALCULATE YOUR DAILY GOAL ---
st.write("##")
st.divider()
st.subheader("🎯 Set Your Heart Goal for Today")
goal_col1, goal_col2 = st.columns([1, 2])

with goal_col1:
    goal_type = st.selectbox("Choose a goal:", ["Walk 10,000 Steps", "Eat 5 Servings of Veggies", "8 Hours Sleep", "No Added Sugar"])
    if st.button("Set Daily Challenge"):
        st.success(f"Goal set! You've committed to: **{goal_type}**")

with goal_col2:
    st.info("**Did you know?** Walking just 30 minutes a day can reduce your risk of cardiovascular disease by up to 35%. Start small, stay consistent!")

# --- 6. FOOTER ---
st.divider()
st.caption("CardioScan Health Coach | Scientific Guidelines | © 2026")