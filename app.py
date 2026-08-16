import streamlit as st
from PyPDF2 import PdfReader

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
    }

    .score-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #ddd;
        margin: 10px 0;
    }

    .score-number {
        font-size: 40px;
        font-weight: bold;
    }

    .skill-box {
        padding: 10px 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 8px;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">📄 AI Resume Screening System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze your resume • Detect skills • Check ATS-style score • Get improvement suggestions</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📌 About Project")

    st.write(
        "This application analyzes a PDF resume and identifies "
        "technical skills mentioned in the resume."
    )

    st.write("### Technologies")
    st.write("🐍 Python")
    st.write("🌐 Streamlit")
    st.write("📄 PyPDF2")
    st.write("🔢 NumPy")
    st.write("🐙 Git & GitHub")

    st.divider()

    st.write("### How it works")
    st.write("1. Upload Resume")
    st.write("2. Extract Text")
    st.write("3. Detect Skills")
    st.write("4. Calculate ATS Score")
    st.write("5. Show Recommendations")


# ---------------- SKILLS LIST ----------------
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


# ---------------- UPLOAD SECTION ----------------
st.markdown(
    '<div class="section-title">📤 Upload Your Resume</div>',
    unsafe_allow_html=True
)

st.write("Upload your resume in PDF format to start the analysis.")

uploaded_file = st.file_uploader(
    "Choose a Resume",
    type=["pdf"],
    help="Only PDF files are supported."
)


# ---------------- RESUME ANALYSIS ----------------
if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    # ---------------- RESUME TEXT ----------------
    st.markdown(
        '<div class="section-title">📄 Extracted Resume Text</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    # Convert text to lowercase
    resume_text_lower = resume_text.lower()

    # ---------------- DETECT SKILLS ----------------
    detected_skills = []

    for skill in skills:
        if skill.lower() in resume_text_lower:
            detected_skills.append(skill)

    # ---------------- MISSING SKILLS ----------------
    missing_skills = []

    for skill in skills:
        if skill not in detected_skills:
            missing_skills.append(skill)

    # ---------------- ATS SCORE ----------------
    match_score = (len(detected_skills) / len(skills)) * 100

    # ---------------- SUMMARY CARDS ----------------
    st.markdown(
        '<div class="section-title">📊 Resume Analysis</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{match_score:.2f}%"
        )

    with col2:
        st.metric(
            "Skills Detected",
            len(detected_skills)
        )

    with col3:
        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

    # ---------------- ATS SCORE ----------------
    st.markdown(
        '<div class="section-title">🎯 ATS Score</div>',
        unsafe_allow_html=True
    )

    st.progress(match_score / 100)

    if match_score >= 80:
        st.success(
            f"🌟 ATS Score: {match_score:.2f}% — Excellent Match!"
        )

    elif match_score >= 60:
        st.info(
            f"👍 ATS Score: {match_score:.2f}% — Good Match!"
        )

    else:
        st.warning(
            f"⚠️ ATS Score: {match_score:.2f}% — Needs Improvement"
        )

    st.write(
        f"Your resume matches {match_score:.2f}% "
        "of the skills in the current screening list."
    )

    # ---------------- SKILLS COLUMNS ----------------
    col1, col2 = st.columns(2)

    # Detected Skills
    with col1:

        st.markdown(
            '<div class="section-title">✅ Detected Skills</div>',
            unsafe_allow_html=True
        )

        if detected_skills:

            for skill in detected_skills:
                st.success("✓ " + skill)

        else:
            st.warning("No skills detected.")

    # Missing Skills
    with col2:

        st.markdown(
            '<div class="section-title">⚠️ Missing Skills</div>',
            unsafe_allow_html=True
        )

        if missing_skills:

            for skill in missing_skills:
                st.warning("✗ " + skill)

        else:
            st.success("🎉 No missing skills!")

    # ---------------- RECOMMENDATION ----------------
    st.markdown(
        '<div class="section-title">💡 Recommendation</div>',
        unsafe_allow_html=True
    )

    if match_score >= 80:

        st.success(
            "Excellent Match! Your resume contains most of the skills "
            "from the screening list."
        )

    elif match_score >= 60:

        st.info(
            "Good Match! Consider adding some of the missing skills "
            "if they are relevant to your career goal."
        )

    else:

        st.warning(
            "Your resume could be improved by adding relevant skills "
            "and projects that match your target job."
        )

    # ---------------- IMPROVEMENT SUGGESTIONS ----------------
    st.markdown(
        '<div class="section-title">🚀 Resume Improvement Suggestions</div>',
        unsafe_allow_html=True
    )

    if match_score < 50:

        st.warning("Your resume needs improvement.")

        st.write("• Add relevant technical skills.")
        st.write("• Add projects related to your target job.")
        st.write("• Mention programming and database skills.")
        st.write("• Keep your resume focused on the desired job role.")

    elif match_score < 80:

        st.info("Your resume is good, but some areas can be improved.")

        st.write("• Add relevant missing skills.")
        st.write("• Add more practical projects.")
        st.write("• Keep your skills section updated.")
        st.write("• Highlight important technical experience.")

    else:

        st.success("Excellent! Your resume has a strong skill match.")

        st.write("• Keep your skills section updated.")
        st.write("• Continue adding relevant projects.")
        st.write("• Add relevant certifications when available.")

    # ---------------- FOOTER ----------------
    st.divider()

    st.caption(
        "AI Resume Screening System | Developed using Python & Streamlit"
    )

else:

    st.info(
        "👆 Upload a PDF resume above to start the screening process."
    )

    st.markdown(
        "### ✨ What you'll get"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("📄 **Resume Text Extraction**")
        st.caption("Extract text automatically from your PDF.")

    with col2:
        st.write("🎯 **ATS-style Score**")
        st.caption("Check your skill match percentage.")

    with col3:
        st.write("💡 **Improvement Tips**")
        st.caption("Get suggestions for improving your resume.")