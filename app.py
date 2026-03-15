import streamlit as st
import pandas as pd

from src.feature_extraction import extract_experience, extract_skills, extract_languages
from src.scoring import compute_score

st.title("AI CV Screening Agent")

text = st.text_area("Paste CV text")

if st.button("Analyze CV"):

    experience = extract_experience(text)
    skills = extract_skills(text)
    languages = extract_languages(text)

    features = {
        "experience":experience,
        "skills":skills,
        "languages":languages
    }

    score = compute_score(features)

    st.write("Experience:",experience)
    st.write("Skills:",skills)
    st.write("Languages:",languages)
    st.write("Candidate Score:",score)
