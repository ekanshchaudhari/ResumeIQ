import re

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Git",
    "GitHub",
    "Streamlit",
    "Microsoft Office",
    "Excel",
    "Power BI",
    "Canva",
    "Machine Learning",
    "Data Analysis",
    "Problem Solving",
    "Team Management",
    "Communication"
]

def extract_skills(text):
    detected_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            detected_skills.append(skill)

    return detected_skills