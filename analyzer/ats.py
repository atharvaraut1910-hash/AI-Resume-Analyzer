def calculate_ats_score(text, job_description=""):
    text = text.lower()

    score = 0
    suggestions = []

    # Education
    if "bachelor" in text or "degree" in text:
        score += 20
    else:
        suggestions.append("Add Education Details")

    # Experience
    if "experience" in text or "internship" in text:
        score += 20
    else:
        suggestions.append("Add Internship or Experience")

    # Skills
    skills = [
        "python",
        "sql",
        "django",
        "html",
        "css",
        "javascript",
        "excel",
        "power bi",
        "machine learning",
    ]

    detected_skills = []
    missing_skills = []

    found = 0

    for skill in skills:
        if skill in text:
            found += 1
            detected_skills.append(skill.title())
        else:
            missing_skills.append(skill.title())

    score += found * 5

    # Projects
    if "project" in text:
        score += 20
    else:
        suggestions.append("Add Projects")

    # Contact
    if "@" in text and "+" in text:
        score += 15
    else:
        suggestions.append("Add Contact Details")

    # Max score
    if score > 100:
        score = 100

    # =========================
    # Job Description Match
    # =========================
    job_match = 0

    if job_description.strip():
        jd_words = set(job_description.lower().split())
        resume_words = set(text.lower().split())

        common = jd_words.intersection(resume_words)

        if len(jd_words) > 0:
            job_match = int((len(common) / len(jd_words)) * 100)

    return (
        score,
        suggestions,
        detected_skills,
        missing_skills,
        job_match,
    )