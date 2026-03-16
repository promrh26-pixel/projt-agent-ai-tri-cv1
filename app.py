import streamlit as st
import pdfplumber

st.title("AI CV Screening Agent")

# zone texte
cv_text = st.text_area("Paste CV text")

# upload pdf
uploaded_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])

# lire le pdf
if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    cv_text = text
    st.text_area("Extracted CV Text", cv_text)

# bouton analyse
if st.button("Analyze CV"):

    skills = []
    languages = []

    skill_keywords = ["python","sql","machine learning","power bi","excel"]
    language_keywords = ["english","french","spanish","arabic"]

    for skill in skill_keywords:
        if skill in cv_text.lower():
            skills.append(skill)

    for lang in language_keywords:
        if lang in cv_text.lower():
            languages.append(lang)

    score = len(skills) * 10

    st.write("Experience:", 1)
    st.write("Skills:", skills)
    st.write("Languages:", languages)
    st.write("Candidate Score:", score)