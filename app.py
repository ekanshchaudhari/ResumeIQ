import streamlit as st

# Configure the page
st.set_page_config(
    page_title="ResumeIQ",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 ResumeIQ")

# Subtitle
st.subheader("Your Smart Resume Analyzer")

# Welcome message
st.write("""
Welcome to ResumeIQ!

This application analyzes resumes and provides:
- 📧 Contact information detection
- 🛠️ Skill detection
- 📚 Resume section analysis
- 📊 Resume score
- 💡 Personalized suggestions
""")

st.info("🚀 Upload functionality will be added in the next step.")
