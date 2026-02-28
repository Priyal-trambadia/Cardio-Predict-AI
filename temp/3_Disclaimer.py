import streamlit as st

st.set_page_config(page_title="Legal Disclaimer", page_icon="⚖️")

st.markdown("""
    <style>
    .report-container {
        background-color: #FFF5F5;
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #FEB2B2;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ Compliance & Disclaimer")

# st.markdown('<div class="report-container">', unsafe_allow_html=True)
st.error("### 🛑 Not a Medical Diagnostic Tool")
st.write("""
This software is a **Machine Learning Prototype** and is provided for informational and educational purposes only. 
The 97% accuracy reported is based on historical training data and does not guarantee real-world clinical performance.
""")

st.subheader("Key Terms of Use:")
st.markdown("""
- **Consult a Doctor:** Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
- **No Liability:** The developers of CardioScan AI are not responsible for any health decisions made based on this tool.
- **Data Usage:** This application does not store, share, or sell patient data entered during the session.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.info("For clinical partnerships or research inquiries, please contact: `research@cardioscan.ai`")