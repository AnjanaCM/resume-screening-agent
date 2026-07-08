import streamlit as st
import pandas as pd
from parser import extract_all_resumes
from scorer import calculate_similarity
from skill_matcher import compare_skills
import os

st.title("🤖 AI Resume Screening Agent")

with open("jd/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

st.subheader("Job Description")
st.text(job_description)

if st.button("Analyze Resumes"):

    resumes = extract_all_resumes("resumes")
    results = []

    jd_skills, _ = compare_skills(job_description, job_description)
    total_jd_skills = len(jd_skills)

    for filename, resume_text in resumes.items():

        ai_score = calculate_similarity(job_description, resume_text)

        matched, missing = compare_skills(job_description, resume_text)

        if total_jd_skills > 0:
            skill_score = (len(matched) / total_jd_skills) * 100
        else:
            skill_score = 0

        final_score = (0.7 * ai_score) + (0.3 * skill_score)

        if final_score >= 45:
            recommendation = "Shortlist"
        elif final_score >= 30:
            recommendation = "Consider"
        else:
            recommendation = "Reject"

        results.append({
            "Resume": filename,
            "AI Score": round(ai_score, 2),
            "Skill Score": round(skill_score, 2),
            "Final Score": round(final_score, 2),
            "Recommendation": recommendation
        })

    df = pd.DataFrame(results)
    df = df.sort_values("Final Score", ascending=False)

    st.success("Analysis Complete!")

    st.dataframe(df)

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        file_name="ranked_candidates.csv",
        mime="text/csv"
    )