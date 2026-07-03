def create_profile(resume_text, student_data):

    skills = []

    skill_list = [
        "Python",
        "JavaScript",
        "SQL",
        "Java",
        "C",
        "C++",
        "HTML",
        "CSS",
        "React",
        "FastAPI",
        "Flask",
        "Git"
    ]

    for skill in skill_list:
        if skill.lower() in resume_text.lower():
            skills.append(skill)

    education = "Not Found"

    education_keywords = [
        "B.Tech",
        "B.E",
        "BCA",
        "M.Tech",
        "MCA",
        "MBA"
    ]

    for degree in education_keywords:
        if degree.lower() in resume_text.lower():
            education = degree
            break

    # Better Name Extraction

    name = "Unknown"

    ignore_words = [
        "cse",
        "computer science",
        "department",
        "resume",
        "curriculum vitae",
        "b.tech",
        "btech"
    ]

    lines = resume_text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if (
            line
            and line.lower() not in ignore_words
            and len(line.split()) >= 2
        ):
            name = line
            break

    profile = {
        "name": name,
        "age": student_data["age"],
        "education": education,
        "skills": skills,
        "annual_income": student_data["annual_income"],
        "category": student_data["category"],
        "state": student_data["state"],
        "career_interest": student_data["career_interest"]
    }

    return profile