import streamlit as st
from utils.contact_detector import extract_email, extract_phone
from utils.pdf_reader import extract_text_from_pdf
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

    # Extract text from the uploaded PDF
    resume_text = extract_text_from_pdf(uploaded_file)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    st.divider()

    st.subheader("📧 Email Detected")

    if email:
        st.success(email)
    else:
        st.error("No email found.")
    
    st.subheader("📱 Phone Number Detected")

    if phone:
        st.success(phone)
    else:
        st.error("No phone number found.")
    
    st.divider()

    st.subheader("📄 Extracted Resume Text")
    
    st.text(resume_text)

    st.info("📄 PDF File Detected")