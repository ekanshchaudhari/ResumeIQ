def calculate_score(sections):

    score = 0

    for section in sections:
        if sections[section]:
            score += 25

    return score