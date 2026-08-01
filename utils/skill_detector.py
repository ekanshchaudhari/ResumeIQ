import re

SKILLS = [

    # Programming Languages
    "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript",
    "Go", "Rust", "Kotlin", "Swift", "PHP", "Ruby", "R",
    "MATLAB", "Scala", "Perl", "Dart", "SQL", "NoSQL",

    # Web Development
    "HTML", "CSS", "React", "Angular", "Vue", "Next.js",
    "Node.js", "Express.js", "Bootstrap", "Tailwind CSS",
    "jQuery", "REST API", "GraphQL",

    # Databases
    "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Firebase",
    "Oracle", "Redis", "MariaDB", "Cassandra", "DynamoDB",

    # Cloud
    "AWS", "Microsoft Azure", "Google Cloud", "Docker",
    "Kubernetes", "Terraform", "Heroku", "Netlify", "Vercel",

    # Version Control
    "Git", "GitHub", "GitLab", "Bitbucket",

    # Data Science
    "Pandas", "NumPy", "Matplotlib", "Scikit-learn",
    "TensorFlow", "PyTorch", "Keras", "OpenCV",
    "Power BI", "Tableau", "Excel", "Machine Learning",
    "Deep Learning", "Data Analysis", "Data Visualization",
    "Statistics", "NLP",

    # Cyber Security
    "Ethical Hacking", "Penetration Testing", "Network Security",
    "Cryptography", "Wireshark", "Burp Suite", "Linux",
    "Kali Linux", "SIEM",

    # Mobile Development
    "Android Studio", "Flutter", "React Native",
    "SwiftUI", "Xcode",

    # DevOps
    "CI/CD", "Jenkins", "Ansible", "Linux Administration",
    "Bash", "Shell Scripting",

    # Software Engineering
    "Object Oriented Programming", "Data Structures",
    "Algorithms", "Operating Systems", "Computer Networks",
    "DBMS", "System Design", "Microservices",
    "Software Testing", "Unit Testing",

    # Design
    "Canva", "Figma", "Adobe Photoshop",
    "Adobe Illustrator", "Adobe XD",
    "UI Design", "UX Design",

    # Finance
    "Financial Modeling", "Equity Research",
    "Valuation", "Financial Analysis",
    "Accounting", "Risk Management",
    "Investment Banking", "Portfolio Management",
    "Bloomberg Terminal", "Capital Markets",

    # Marketing
    "SEO", "SEM", "Google Analytics",
    "Social Media Marketing", "Email Marketing",
    "Content Marketing", "Copywriting",

    # HR
    "Recruitment", "Talent Acquisition",
    "Employee Relations", "HR Analytics",
    "Payroll", "Performance Management",

    # Project Management
    "Agile", "Scrum", "Kanban",
    "Jira", "Trello", "Asana",
    "Project Management",

    # Office Tools
    "Microsoft Word", "Microsoft Excel",
    "Microsoft PowerPoint", "Microsoft Office",
    "Google Sheets", "Google Docs",

    # Soft Skills
    "Leadership", "Teamwork", "Team Management",
    "Communication", "Professional Communication",
    "Critical Thinking", "Problem Solving",
    "Decision Making", "Adaptability",
    "Creativity", "Time Management",
    "Presentation Skills", "Negotiation",
    "Public Speaking", "Analytical Thinking",
    "Research", "Collaboration",
    "Attention to Detail", "Multitasking",

    # AI
    "Artificial Intelligence", "Generative AI",
    "Prompt Engineering", "LLMs",
    "ChatGPT", "LangChain", "RAG",
    "Vector Databases", "Hugging Face",

    # Misc
    "Networking", "Customer Service",
    "Sales", "Business Development",
    "Business Analysis", "Consulting",
    "Teaching", "Mentoring",
    "Event Management"
]


def extract_skills(text):
    detected_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            detected_skills.append(skill)

    return detected_skills