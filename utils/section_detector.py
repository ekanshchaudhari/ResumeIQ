import re

SECTIONS = {
    "Education": [
        "Education",
        "Educational Qualifications",
        "Academic Qualifications",
        "Academic Background"
    ],

    "Experience": [
        "Experience",
        "Work Experience",
        "Professional Experience",
        "Employment",
        "Internships",
        "Positions of Responsibility"
    ],

    "Projects": [
        "Projects",
        "Academic Projects",
        "Personal Projects"
    ],

    "Skills": [
        "Skills",
        "Technical Skills",
        "Core Competencies"
    ]
}


def detect_sections(text):

    detected_sections = {}

    for section in SECTIONS:

        detected_sections[section] = False

        for heading in SECTIONS[section]:

            pattern = r"\b" + re.escape(heading) + r"\b"

            if re.search(pattern, text, re.IGNORECASE):
                detected_sections[section] = True
                break

    return detected_sections