import streamlit as st
from PyPDF2 import PdfReader

st.title("AI Resume Screening System")

st.write("Upload your resume in PDF format")

uploaded_file = st.file_uploader(
    "Choose a Resume",
    type=["pdf"]
)

# Skills list
skills = [
    "Python",
    "Java",
    "C++",
    "C",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Django",
    "Flask",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Data Science",
    "Git",
    "GitHub",
    "MySQL",
    "MongoDB"
]

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    # Show resume text
    st.subheader("Resume Text")

    st.text_area(
        "Extracted Resume Content",
        resume_text,
        height=300
    )

   # Find skills
resume_text_lower = resume_text.lower()

detected_skills = []

for skill in skills:
    if skill.lower() in resume_text_lower:
        detected_skills.append(skill)

# Show detected skills
st.subheader("Detected Skills")

if detected_skills:
    for skill in detected_skills:
        st.success("✓ " + skill)
else:
    st.warning("No skills detected.")

# Match Score
match_score = (len(detected_skills) / len(skills)) * 100

# ATS Score
st.subheader("📊 ATS Score")

st.progress(match_score / 100)

if match_score >= 80:
    st.success(f"ATS Score: {match_score:.2f}% — Excellent Match!")
elif match_score >= 60:
    st.info(f"ATS Score: {match_score:.2f}% — Good Match!")
else:
    st.warning(f"ATS Score: {match_score:.2f}% — Needs Improvement")

st.write(
    f"Your resume matches {match_score:.2f}% of the required skills."
)

# Missing Skills
missing_skills = []

for skill in skills:
    if skill not in detected_skills:
        missing_skills.append(skill)

st.subheader("Missing Skills")

if missing_skills:
    for skill in missing_skills:
        st.warning("✗ " + skill)
else:
    st.success("No missing skills")

# Recommendation
st.subheader("Recommendation")

if match_score >= 80:
    st.success("Excellent Match - Your resume matches most of the required skills.")
elif match_score >= 60:
    st.info("Good Match - Some skills can be improved.")
else:
    st.warning("Low Match - You should improve your resume by adding the missing skills.")

    # Resume Improvement Suggestions
st.subheader("Resume Improvement Suggestions")

if match_score < 50:
    st.warning("Your resume needs improvement.")
    st.write("• Add more relevant technical skills.")
    st.write("• Add projects related to the job role.")
    st.write("• Mention your programming and database skills.")
elif match_score < 80:
    st.info("Your resume is good, but some skills can be improved.")
    st.write("• Add the missing skills shown above.")
    st.write("• Add more relevant projects.")
    st.write("• Keep your resume updated.")
else:
    st.success("Excellent! Your resume has a strong skill match.")
    st.write("• Keep your skills section updated.")
    st.write("• Continue adding relevant projects and certifications.")