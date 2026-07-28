import streamlit as st

st.set_page_config(
    page_title="ResumeIQ",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ResumeIQ")
st.subheader("Your Smart Resume Analyzer")

st.write("""
Upload your resume below and ResumeIQ will analyze it for:
- 📧 Contact Information
- 🛠 Skills
- 📚 Resume Sections
- 📊 Resume Score
- 💡 Suggestions
""")

st.divider()

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    st.write("### File Details")
    st.write(f"**Filename:** {uploaded_file.name}")
    st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")

    st.info("📄 PDF File Detected")