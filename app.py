import streamlit as st
import re
import docx
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------- Page Setup -------------------
st.set_page_config(page_title="AI Resume Matcher", page_icon="🤖", layout="wide")

st.markdown(
    """
    <h1 style="text-align:center; color:#4CAF50;">🤖 AI Resume vs Job Description Matcher</h1>
    <p style="text-align:center; font-size:16px; color:gray;">
        Upload your resume & paste a job description to see how well they match!
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ------------------- Text Cleaning -------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# ------------------- File Readers -------------------
def read_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# ------------------- Upload Section -------------------
st.subheader("📂 Step 1: Upload Resume or Paste Text")

uploaded_resume = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
resume_text = ""

if uploaded_resume:
    if uploaded_resume.type == "application/pdf":
        resume_text = read_pdf(uploaded_resume)
    elif uploaded_resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = read_docx(uploaded_resume)

if not resume_text:
    resume_text = st.text_area("Or paste your resume text here ✍️", height=200)

# ------------------- Job Description -------------------
st.subheader("💼 Step 2: Paste Job Description")
jd_text = st.text_area("Paste the job description here", height=200)

# ------------------- Match Section -------------------
if st.button("🚀 Analyze Match"):
    if resume_text and jd_text:
        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd_text)

        docs = [resume_clean, jd_clean]
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(docs)

        # Cosine similarity score
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

        # Progress bar + Score
        st.subheader("📊 Match Score")
        st.progress(int(score))
        st.markdown(
            f"<h2 style='text-align:center; color:#2196F3;'>{score:.2f}%</h2>",
            unsafe_allow_html=True
        )

        # Keyword overlap
        resume_words = set(resume_clean.split())
        jd_words = set(jd_clean.split())
        overlap = resume_words.intersection(jd_words)
        missing = jd_words - resume_words
        overlap_percent = (len(overlap) / len(jd_words)) * 100 if jd_words else 0

        col1, col2 = st.columns(2)
        with col1:
            st.metric("✅ Keyword Overlap", f"{overlap_percent:.1f}%")
        with col2:
            st.metric("❌ Missing Keywords", len(missing))

        # Missing keywords section
        st.subheader("🔑 Missing Keywords You Should Add")
        if missing:
            st.info(", ".join(sorted(list(missing))[:30]))
        else:
            st.success("🎉 Great! No major keywords missing.")

        # Overlap section
        with st.expander("📌 Matched Keywords"):
            st.write(", ".join(sorted(list(overlap))[:30]))

    else:
        st.warning("⚠️ Please upload/paste a resume AND paste a job description.")
