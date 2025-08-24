# 📄 AI Resume Matcher

An **AI-powered Resume vs Job Description Analyzer** that helps candidates and recruiters quickly check how well a resume matches a job description.  
Built with **Streamlit**, **Python**, and **TF-IDF (Cosine Similarity)**, this tool provides a **match score, keyword analysis, and missing skills**.

---

## 🚀 Features
- 📂 Upload **Resume (PDF/DOCX)** or paste text directly  
- 📝 Paste **Job Description** for comparison  
- 📊 Calculates **Match Score (%)** using TF-IDF + Cosine Similarity  
- 🔑 Highlights **Keyword Overlap** and **Missing Keywords**  
- 🎨 Clean and interactive **Streamlit UI**  

---

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** (for UI)  
- **Scikit-Learn** (TF-IDF, Cosine Similarity)  
- **PyPDF2** (PDF reader)  
- **python-docx** (DOCX reader)  

---

## 📥 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/23KarishmaB/AI_Resume_Matcher.git
   cd AI_Resume_Matcher

2.Create & activate a virtual environment 

python -m venv venv
# Activate on Mac/Linux
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate

3.Install dependencies

pip install -r requirements.txt

4.Run the Streamlit app

streamlit run app.py

5. Open in your browser:

http://localhost:8501