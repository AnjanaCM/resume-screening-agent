import os
import pandas as pd

from parser import extract_all_resumes
from scorer import calculate_similarity
from skill_matcher import compare_skills

# Load Job Description
with open("jd/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

# Read all resumes
resumes = extract_all_resumes("resumes")

results = []

# Count JD skills once
jd_skills, _ = compare_skills(job_description, job_description)
total_jd_skills = len(jd_skills)

for filename, resume_text in resumes.items():

    # AI Similarity Score
    ai_score = calculate_similarity(job_description, resume_text)

    # Skill Matching
    matched, missing = compare_skills(job_description, resume_text)

    if total_jd_skills > 0:
        skill_score = (len(matched) / total_jd_skills) * 100
    else:
        skill_score = 0

    # Final Score
    final_score = (0.7 * ai_score) + (0.3 * skill_score)

    # Recommendation
    if final_score >= 70:
        recommendation = "Shortlist"
    elif final_score >= 50:
        recommendation = "Consider"
    else:
        recommendation = "Reject"

    results.append({
        "Resume": filename,
        "AI Score": round(ai_score, 2),
        "Skill Score": round(skill_score, 2),
        "Final Score": round(final_score, 2),
        "Matched Skills": ", ".join(matched),
        "Missing Skills": ", ".join(missing),
        "Recommendation": recommendation
    })

# Sort by Final Score
results = sorted(results, key=lambda x: x["Final Score"], reverse=True)

# Create DataFrame
df = pd.DataFrame(results)

# Save CSV
os.makedirs("output", exist_ok=True)
df.to_csv("output/ranked_candidates.csv", index=False)

# Display results
print(df)

print("\nCSV saved successfully!")