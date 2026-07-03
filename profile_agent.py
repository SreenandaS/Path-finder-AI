import re


def extract_name(resume_text):

    lines = resume_text.split("\n")

    ignore_words = [
        "computer science",
        "engineering",
        "department",
        "resume",
        "curriculum vitae",
        "college",
        "university"
    ]

    for line in lines[:15]:

        line = line.strip()

        if not line:
            continue

        if any(word in line.lower() for word in ignore_words):
            continue

        if "@" in line:
            continue

        if any(char.isdigit() for char in line):
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            return line

    return "Unknown"


def extract_email(resume_text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    return match.group() if match else "Not Found"


def extract_phone(resume_text):

    match = re.search(
        r"(\+91[\-\s]?)?[6-9]\d{9}",
        resume_text
    )

    return match.group() if match else "Not Found"


def extract_education(resume_text):

    education_keywords = [
        "B.Tech",
        "B.E",
        "BCA",
        "M.Tech",
        "MCA",
        "MBA",
        "BSc",
        "MSc"
    ]

    for degree in education_keywords:

        if degree.lower() in resume_text.lower():
            return degree

    return "Not Found"


def extract_skills(resume_text):

    skill_list = [
        "Python",
        "Java",
        "JavaScript",
        "SQL",
        "HTML",
        "CSS",
        "React",
        "Node.js",
        "FastAPI",
        "Flask",
        "Git",
        "C",
        "C++",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Power BI",
        "Excel",
        "MongoDB",
        "MySQL",
        "PostgreSQL",
        "Docker",
        "AWS"
    ]

    found_skills = []

    text = resume_text.lower()

    for skill in skill_list:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


def create_profile(resume_text, student_data):

    profile = {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "phone": extract_phone(resume_text),
        "education": extract_education(resume_text),
        "skills": extract_skills(resume_text),
        "age": student_data["age"],
        "annual_income": student_data["annual_income"],
        "category": student_data["category"],
        "state": student_data["state"],
        "career_interest": student_data["career_interest"]
    }

    return profile
