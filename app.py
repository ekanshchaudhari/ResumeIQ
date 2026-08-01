import streamlit as st
from utils.contact_detector import (
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github
)
from utils.skill_detector import extract_skills
from utils.section_detector import detect_sections
from utils.scorer import calculate_score
from utils.suggestions import generate_suggestions
from utils.pdf_reader import extract_text_from_pdf, extract_links_from_pdf
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
    links = extract_links_from_pdf(uploaded_file)
    combined_text = resume_text + "\n" + "\n".join(links)
    email = extract_email(combined_text)
    phone = extract_phone(combined_text)
    linkedin = extract_linkedin(combined_text)
    github = extract_github(combined_text)
    skills = extract_skills(resume_text)
    sections = detect_sections(resume_text)
    score = calculate_score(sections)
    suggestions = generate_suggestions(sections)
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
    
    st.subheader("💼 LinkedIn Profile")
    
    if linkedin:
        st.success(linkedin)
    else:
        st.error("No LinkedIn profile found.")
    st.subheader("🐙 GitHub Profile")

    if github:
        st.success(github)
    else:
        st.error("No GitHub profile found.")
    st.subheader("🛠️ Skills Detected")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.error("No skills found.")
    st.subheader("📂 Resume Sections")

    for section, found in sections.items():
        if found:
            st.success(f"✅ {section}")
        else:
            st.error(f"❌ {section}")
    if score >= 90:
        rating = "🟢 Excellent Resume"

    elif score >= 70:
        rating = "🟡 Good Resume"

    elif score >= 50:
        rating = "🟠 Needs Improvement"

    else:
        rating = "🔴 Poor Resume"

    st.subheader("💯 Resume Score")
    st.progress(score / 100)
    st.metric("Resume Score", f"{score}/100")
    st.markdown(f"### {rating}")

    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.warning(suggestion)
    
    st.divider()

    st.subheader("📄 Extracted Resume Text")
    
    st.text(resume_text)

    st.info("📄 PDF File Detected")