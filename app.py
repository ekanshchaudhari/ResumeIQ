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
st.markdown("""
<style>

/* Main container */
.block-container{
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Metric cards */
div[data-testid="metric-container"]{
    background-color:#1E1E1E;
    border:1px solid #333333;
    padding:18px;
    border-radius:15px;
    transition:0.3s;
}

div[data-testid="metric-container"]:hover{
    border-color:#00C853;
    transform:translateY(-2px);
}

/* Expanders */
.streamlit-expanderHeader{
    font-size:18px;
    font-weight:600;
}

/* Success boxes */
div[data-testid="stAlert"]{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

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
    
    with st.expander("🛠️ Skills Detected", expanded=True):

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
    st.metric("Resume Score", f"{score}/100")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📧 Email")
        if email:
            st.success(email)
        else:
           st.error("Not Found")

    with col2:
        st.subheader("📱 Phone")
        if phone:
            st.success(phone)
        else:
            st.error("Not Found")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("💼 LinkedIn")
        if linkedin:
            st.success(linkedin)
        else:
            st.error("Not Found")

    with col4:
        st.subheader("🐙 GitHub")
        if github:
            st.success(github)
        else:
            st.error("Not Found")
    
    
    st.subheader("📊 Resume Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Score", f"{score}/100")

    with col2:
        st.metric("Rating", rating)

    with col3:
        st.metric("Skills", len(skills))

    with col4:
        st.metric("Sections", f"{sum(sections.values())}/{len(sections)}")  
    
    st.progress(score / 100)
    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.warning(suggestion)
   
    st.divider()

    st.subheader("📄 Extracted Resume Text")
    
    st.text(resume_text)

    st.info("📄 PDF File Detected")