from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(job_description, resume_text):
    """
    Returns similarity score between JD and Resume.
    """

    jd_embedding = model.encode(job_description)
    resume_embedding = model.encode(resume_text)

    score = cosine_similarity(
        [jd_embedding],
        [resume_embedding]
    )[0][0]

    return round(score * 100, 2)