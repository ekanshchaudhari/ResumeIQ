def compare_skills(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = resume_set.intersection(jd_set)
    missing = jd_set - resume_set
    extra = resume_set - jd_set

    if len(jd_set) > 0:
        match_score = round((len(matched) / len(jd_set)) * 100)
    else:
        match_score = 0

    return {
        "matched": sorted(matched),
        "missing": sorted(missing),
        "extra": sorted(extra),
        "match_score": match_score
    }