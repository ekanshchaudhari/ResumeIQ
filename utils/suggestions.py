def generate_suggestions(sections):

    suggestions = []

    if not sections["Projects"]:
        suggestions.append("Add a Projects section.")
    
    if not sections["Education"]:
        suggestions.append("Add an Education section.")

    if not sections["Experience"]:
        suggestions.append("Add a Work Experience section.")

    if not sections["Skills"]:
        suggestions.append("Add a Skills section highlighting your technical and soft skills.")
    
    return suggestions
