import streamlit as st
import PyPDF2

st.title("Resume Skill Checker")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")

skills = [
    "python","machine learning","sql","java","html","css","javascript",
    "data analysis","git","docker","linux","c++","c","tensorflow",
    "pandas","numpy","react","node","flask","django","streamlit",
    "deep learning","nlp","data science"
]

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    text = text.lower()

    found_skills = set()

    for skill in skills:
        if skill in text:
            found_skills.add(skill)

    st.subheader("Detected Skills")

    if found_skills:
        st.success("Skills found in resume:")
        for skill in sorted(found_skills):
            st.write("•", skill.title())
    else:
        st.warning("No skills detected in the resume.")
