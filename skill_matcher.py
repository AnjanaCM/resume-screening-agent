import re

# List of skills we want to detect
SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "flask",
    "django",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "opencv",
    "git",
    "github",
    "rest api",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "data structures",
    "algorithms"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return list(set(found_skills))


def compare_skills(jd_text, resume_text):

    jd_skills = extract_skills(jd_text)

    resume_skills = extract_skills(resume_text)

    matched = []

    missing = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing