# 🤖 AI Resume Screening Agent

An AI-powered Resume Screening Agent that automatically compares multiple resumes with a Job Description (JD) using semantic similarity and skill matching. It ranks candidates and provides hiring recommendations.

---

## 🚀 Features

- 📄 Extracts text from PDF resumes
- 📋 Reads Job Description
- 🤖 Semantic similarity using Sentence Transformers
- 🛠️ Skill extraction and comparison
- 📊 Candidate ranking
- ✅ Hiring recommendation (Shortlist / Consider / Reject)
- 📁 Export ranked candidates to CSV
- 🌐 Streamlit Web Interface

---

## 🛠️ Tech Stack

- Python
- Sentence Transformers
- Scikit-learn
- Pandas
- Streamlit
- PyPDF2

---

## 📂 Project Structure

```
resume-screening-agent/
│
├── app.py
├── streamlit_app.py
├── parser.py
├── scorer.py
├── skill_matcher.py
├── requirements.txt
├── README.md
├── .gitignore
├── jd/
│   └── job_description.txt
├── resumes/
│   └── *.pdf
├── output/
│   └── ranked_candidates.csv
└── screenshots/
    ├── home.png
    ├── results.png
    └── download.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AnjanaCM/resume-screening-agent.git
```

Go to the project folder:

```bash
cd resume-screening-agent
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Command Line Version

```bash
python app.py
```

### Streamlit Web Interface

```bash
python -m streamlit run streamlit_app.py
```

---

## 📊 Sample Output

The application generates:

- AI Similarity Score
- Skill Match Score
- Final Score
- Matched Skills
- Missing Skills
- Recommendation
- Ranked Candidates CSV

---

## 📸 Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

### 📊 Results

![Results](screenshots/results.png)

### 📥 Download CSV

![Download](screenshots/download.png)

---

## 🔮 Future Improvements

- Upload resumes directly from the web interface
- Upload Job Description through UI
- ATS compatibility score
- Experience-based ranking
- Resume summarization using Large Language Models (LLMs)
- Email notification for shortlisted candidates

---

## 👩‍💻 Author

**Anjana C M**

GitHub: https://github.com/AnjanaCM