import re

SECTIONS = {
    "Education": [
        "Education",
        "Educational Qualifications",
        "Academic Qualifications",
        "Academic Background",
        "E D U C A T I O N"
    ],

    "Experience": [
        "Experience",
        "Work Experience",
        "Professional Experience",
        "Employment",
        "Internships",
        "Positions of Responsibility",
        "W O R K E X P E R I E N C E"
    ],

    "Projects": [
        "Projects",
        "Academic Projects",
        "Personal Projects",
        "P R O J E C T S"
    ],

    "Skills": [
        "Skills",
        "S K I L L S",
        "Technical Skills",
        "Core Competencies",
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