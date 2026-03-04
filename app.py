import streamlit as st
import PyPDF2

st.title("Resume Skill Checker")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")

skills = ["python", "machine learning", "sql", "java", "html", "css", "javascript", "data analysis", "git"]

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    st.subheader("Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.write(skill)
    else:
        st.write("No skills detected.")
