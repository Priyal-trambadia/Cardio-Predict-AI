import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CardioScan AI | Heart Risk Assessment",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL UI STYLING (Internal CSS) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Custom Header */
    .main-header {
        font-family: 'Inter', sans-serif;
        color: #1E293B;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 10px;
    }
    
    /* Subtext */
    .sub-text {
        color: #64748B;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Prediction Card */
    .prediction-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #0062FF;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #0062FF 0%, #0045B5 100%);
        color: white;
        border-radius: 10px;
        padding: 15px;
        font-size: 18px;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION & INFO ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/833/833472.png", width=80)
    st.title("CardioScan Navigation")
    st.info("Current Page: **Home & Diagnostics**")
    st.markdown("---")
    st.write("🩺 **How to use:**")
    st.caption("1. Enter patient vitals in the form.")
    st.caption("2. Review lifestyle factors.")
    st.caption("3. Click 'Run Heart Analysis'.")

# --- 4. MAIN PAGE CONTENT ---
st.markdown('<h1 class="main-header">❤️ CardioScan AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Advanced Machine Learning for early Cardiovascular Risk Detection.</p>', unsafe_allow_html=True)

# Layout Split
col_input, col_result = st.columns([1.2, 1], gap="large")

with col_input:
    st.subheader("📋 Patient Diagnostic Data")
    
    # Organizing inputs into tabs for a cleaner UI
    tab1, tab2 = st.tabs(["Physical Vitals", "Lifestyle & Habits"])
    
    with tab1:
        c1, c2 = st.columns(2)
        age = c1.number_input("Age (Years)", 18, 110, 45)
        gender = c2.selectbox("Gender", ["Male", "Female"])
        
        c3, c4 = st.columns(2)
        height = c3.slider("Height (cm)", 100, 220, 170)
        weight = c4.slider("Weight (kg)", 30, 200, 70)
        
        bp_sys = st.number_input("Systolic BP (High value)", 80, 220, 120)
        bp_dia = st.number_input("Diastolic BP (Low value)", 50, 150, 80)

    with tab2:
        chol = st.select_slider("Cholesterol Level", options=["Normal", "Above Normal", "Well Above Normal"])
        gluc = st.select_slider("Glucose Level", options=["Normal", "Above Normal", "Well Above Normal"])
        
        smoke = st.checkbox("Current Smoker")
        alcohol = st.checkbox("Consumes Alcohol")
        active = st.checkbox("Physically Active", value=True)

    # Trigger Button
    analyze_btn = st.button("🚀 Run Heart Analysis")

# --- 5. PREDICTION LOGIC & DISPLAY ---
with col_result:
    st.subheader("📊 Analysis Result")
    
    if analyze_btn:
        with st.spinner('Model calculating risk factors...'):
            time.sleep(1.5) # Simulate processing
            
            # --- MOCK PREDICTION LOGIC ---
            # Replace this block with: prediction = model.predict(data)
            risk_score = 15 # Default
            if bp_sys > 140 or chol != "Normal" or smoke:
                risk_score = np.random.randint(65, 94)
            else:
                risk_score = np.random.randint(5, 25)
            # ------------------------------

            st.markdown(f"""
                <div class="prediction-card">
                    <h2 style="color: #1E293B;">Result: {risk_score}% Risk</h2>
                    <p style="color: #64748B;">Based on our XGBoost model analysis</p>
                </div>
            """, unsafe_allow_html=True)

            if risk_score > 50:
                st.error("### ⚠️ WARNING: High Risk Detected")
                st.write("The system has identified multiple indicators associated with cardiovascular issues. We strongly recommend scheduling a clinical examination.")
                st.progress(risk_score)
            else:
                st.success("### ✅ Heart Status: Healthy")
                st.write("Your vital signs and lifestyle factors fall within the statistical safe range. Maintain your current activity levels!")
                st.progress(risk_score)
                st.balloons()
    else:
        st.info("Please fill in the patient data and click **Run Heart Analysis** to see the prediction results.")



# --- 6. FOOTER ---
st.markdown("---")
st.caption("© 2024 CardioScan AI - Professional Medical ML Suite")








# import streamlit as st
# import pickle
# import numpy as np
# import plotly.graph_objects as go

# # --------------------------------------------------
# # Page Setup
# # --------------------------------------------------
# st.set_page_config(page_title="CardioGuard Elite", layout="wide")

# # --------------------------------------------------
# # Professional Color Palette & Glassmorphism CSS
# # --------------------------------------------------
# st.markdown("""
# <style>
#     /* Professional Color Palette */
#     :root {
#         --bg-color: #0F172A;
#         --card-bg: #1E293B;
#         --accent-blue: #38BDF8;
#         --accent-green: #10B981;
#         --accent-red: #EF4444;
#         --text-main: #F8FAFC;
#     }

#     .stApp {
#         background-color: var(--bg-color);
#         color: var(--text-main);
#     }

#     /* Modern Card Design */
#     .element-container img { border-radius: 20px; }
    
#     div[data-testid="stVerticalBlock"] > div:has(div.card-style) {
#         background-color: var(--card-bg);
#         padding: 2rem;
#         border-radius: 24px;
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
#     }

#     /* Input Field Styling */
#     .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
#         background-color: #0F172A !important;
#         border: 1px solid #334155 !important;
#         color: white !important;
#         border-radius: 12px !important;
#     }

#     /* Custom Header */
#     .main-header {
#         font-size: 3.5rem;
#         font-weight: 800;
#         letter-spacing: -1px;
#         background: linear-gradient(90deg, #38BDF8, #818CF8);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 0px;
#     }

#     /* Navigation/Tab Styling */
#     .stTabs [data-baseweb="tab-list"] {
#         background-color: #1E293B;
#         padding: 8px;
#         border-radius: 16px;
#         gap: 10px;
#     }

#     .stTabs [data-baseweb="tab"] {
#         color: #94A3B8;
#         padding: 10px 25px;
#         border-radius: 12px;
#     }

#     .stTabs [aria-selected="true"] {
#         background-color: #38BDF8 !important;
#         color: #0F172A !important;
#         font-weight: bold;
#     }

#     /* Massive Action Button */
#     .stButton > button {
#         width: 100%;
#         background: linear-gradient(90deg, #38BDF8, #2563EB) !important;
#         color: white !important;
#         border: none !important;
#         padding: 1.5rem !important;
#         font-size: 1.2rem !important;
#         font-weight: 700 !important;
#         border-radius: 16px !important;
#         box-shadow: 0 10px 15px -3px rgba(56, 189, 248, 0.3);
#     }
# </style>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # UI Structure
# # --------------------------------------------------
# st.markdown('<h1 class="main-header">CardioGuard Elite</h1>', unsafe_allow_html=True)
# st.markdown('<p style="color:#94A3B8; font-size:1.2rem; margin-bottom:2rem;">Advanced Cardiovascular Risk Intelligence Platform</p>', unsafe_allow_html=True)

# # Top Metric Row for immediate visual feedback
# top_col1, top_col2, top_col3 = st.columns(3)

# # Setup inputs in Tabs for "Clean" look
# tab1, tab2, tab3 = st.tabs(["📋 PATIENT PROFILE", "🧪 VITALS & LABS", "🏃 LIFESTYLE"])

# with tab1:
#     c1, c2 = st.columns(2)
#     with c1:
#         age = st.number_input("Age (Years)", 1, 120, 45)
#         sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
#     with c2:
#         height = st.number_input("Height (cm)", 100, 250, 175)
#         weight = st.number_input("Weight (kg)", 30, 200, 75)
#     bmi = round(weight / ((height/100)**2), 1)

# with tab2:
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         trestbps = st.number_input("Resting BP", 80, 200, 120)
#         chol = st.number_input("Cholesterol", 100, 600, 200)
#     with c2:
#         thalach = st.number_input("Max Heart Rate", 60, 220, 150)
#         fbs = st.selectbox("Fasting Sugar > 120", [0, 1], format_func=lambda x: "Normal" if x==0 else "High")
#     with c3:
#         cp = st.selectbox("Chest Pain Type", [0,1,2,3])
#         restecg = st.selectbox("Resting ECG", [0,1,2])

# with tab3:
#     c1, c2, c3 = st.columns(3)
#     with c1: exang = st.toggle("Exercise Angina")
#     with c2: slope = st.selectbox("ST Slope", [0,1,2])
#     with c3: thal = st.selectbox("Thalassemia", [0,1,2,3])
    
#     c4, c5 = st.columns(2)
#     with c4: oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)
#     with c5: ca = st.selectbox("Major Vessels", [0,1,2,3,4])

# # --------------------------------------------------
# # High-End Metric Cards
# # --------------------------------------------------
# with top_col1:
#     st.markdown(f"""<div style="background:#1E293B; padding:1.5rem; border-radius:20px; border-left:5px solid #38BDF8;">
#         <p style="color:#94A3B8; margin:0;">Body Mass Index</p>
#         <h2 style="margin:0;">{bmi}</h2>
#     </div>""", unsafe_allow_html=True)

# with top_col2:
#     status = "Healthy" if 110 <= trestbps <= 130 else "Alert"
#     color = "#10B981" if status == "Healthy" else "#EF4444"
#     st.markdown(f"""<div style="background:#1E293B; padding:1.5rem; border-radius:20px; border-left:5px solid {color};">
#         <p style="color:#94A3B8; margin:0;">BP Condition</p>
#         <h2 style="margin:0; color:{color};">{status}</h2>
#     </div>""", unsafe_allow_html=True)

# with top_col3:
#     st.markdown(f"""<div style="background:#1E293B; padding:1.5rem; border-radius:20px; border-left:5px solid #818CF8;">
#         <p style="color:#94A3B8; margin:0;">Analysis Ready</p>
#         <h2 style="margin:0;">13/13 <span style="font-size:1rem;">Inputs</span></h2>
#     </div>""", unsafe_allow_html=True)

# st.write("")
# # --------------------------------------------------
# # Analysis Button
# # --------------------------------------------------
# if st.button("RUN CLINICAL DIAGNOSTIC"):
#     with st.spinner("AI Engine Processing Clinical Markers..."):
#         import time; time.sleep(1.5)
        
#         # Result Layout
#         res_col1, res_col2 = st.columns([1.5, 1])
        
#         with res_col1:
#             # Custom Chart for "Fabulous" Look
#             fig = go.Figure(go.Bar(
#                 x=[age, trestbps, chol, thalach],
#                 y=['Age', 'BP', 'Chol', 'Rate'],
#                 orientation='h',
#                 marker=dict(color=['#38BDF8', '#818CF8', '#F472B6', '#FB7185'])
#             ))
#             fig.update_layout(
#                 title="Input Vector Analysis",
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 font_color="white",
#                 height=300
#             )
#             st.plotly_chart(fig, use_container_width=True)

#         with res_col2:
#             st.markdown("""
#                 <div style="background:rgba(16, 185, 129, 0.1); padding:2rem; border-radius:24px; border:1px solid #10B981; margin-top:30px;">
#                     <h2 style="color:#10B981; margin:0;">SUCCESS</h2>
#                     <p style="color:#F8FAFC; margin-top:10px; font-size:1.1rem;">
#                         <b>Low Risk Profile.</b><br>The AI model suggests no immediate indicators of heart disease.
#                     </p>
#                 </div>
#             """, unsafe_allow_html=True)

# st.markdown("---")
# st.caption("CardioGuard Elite v2.0 | Powered by Gradient Boosting Classifier | Confidential Clinical Data")








# import streamlit as st
# import numpy as np
# import joblib

# # Page config
# st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# # Load model
# model = joblib.load("heart_model.pkl")

# st.title("❤️ Heart Disease Prediction System")
# st.markdown("### Enter Patient Details Below")

# # Sidebar inputs
# st.sidebar.header("Patient Input Parameters")

# age = st.sidebar.slider("Age", 20, 100, 50)
# sex = st.sidebar.selectbox("Gender", ["Female", "Male"])
# cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
# trestbps = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
# chol = st.sidebar.slider("Cholesterol", 100, 600, 200)
# fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
# restecg = st.sidebar.selectbox("Resting ECG Results", [0, 1, 2])
# thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)
# exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
# oldpeak = st.sidebar.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
# slope = st.sidebar.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
# ca = st.sidebar.selectbox("Number of Major Vessels (0-4)", [0, 1, 2, 3, 4])
# thal = st.sidebar.selectbox("Thalassemia", [0, 1, 2, 3])

# # Convert categorical
# sex = 1 if sex == "Male" else 0

# # Prediction button
# if st.button("Predict Heart Disease"):

#     input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
#                             restecg, thalach, exang, oldpeak,
#                             slope, ca, thal]])

#     prediction = model.predict(input_data)
#     probability = model.predict_proba(input_data)

#     st.subheader("Prediction Result")

#     if prediction[0] == 1:
#         st.error("⚠ High Risk of Heart Disease")
#     else:
#         st.success("✅ Low Risk of Heart Disease")

#     st.write(f"Probability of Disease: {probability[0][1]*100:.2f}%")