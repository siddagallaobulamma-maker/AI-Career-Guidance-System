import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
career_info = {
    "Software Developer": {
        "skills": ["Python", "Java", "DSA", "Problem Solving"],
        "description": "Builds applications, websites, and software systems."
    },
    "Data Scientist": {
        "skills": ["Python", "Statistics", "Machine Learning", "Data Analysis"],
        "description": "Analyzes data to extract insights and build predictive models."
    },
    "Web Developer": {
        "skills": ["HTML", "CSS", "JavaScript", "React"],
        "description": "Creates user-friendly and responsive websites."
    },
    "AI Engineer": {
        "skills": ["Python", "Deep Learning", "Neural Networks"],
        "description": "Designs and develops AI and ML-based systems."
    },
    "Digital Marketer": {
        "skills": ["SEO", "Social Media Marketing", "Content Creation", "Google Ads"],
        "description": "Promotes products and services using digital platforms and analytics."
    }
}
import streamlit as st
st.set_page_config(page_title="AI Career Recommendation", page_icon="🎯")

st.title("🎓 AI-Based Career Recommendation System")
st.write("Enter your skills to get a suitable career suggestion 👇")
math = st.slider("📐 Math Skills", 1, 10, 5)
programming = st.slider("💻 Programming Skills", 1, 10, 5)
creativity = st.slider("🎨 Creativity", 1, 10, 5)
communication = st.slider("🗣️ Communication Skills", 1, 10, 5)
marks = st.slider("📊 Marks (%)", 40, 100, 70)
if "career" not in st.session_state:
    st.session_state.career = ""
    st.session_state.description = ""
if st.button("🔍 Get Career Recommendation"):
    if programming >= 7 and math >= 6 and marks >= 60:
        career = "Software Developer"
        description = "Builds applications, websites, and software solutions using programming skills."

    elif creativity >= 7 and communication >= 6:
        career = "Digital Marketer"
        description = "Promotes products and brands using SEO, social media, and online campaigns."

    elif math >= 7 and programming >= 6:
        career = "Data Analyst"
        description = "Analyzes data to find insights using Python, SQL, and statistics."

    elif communication >= 7:
        career = "HR / Manager"
        description = "Manages people, recruitment, communication, and team coordination."

    else:
        career = "General IT Professional"
        description = "Works in IT support, testing, operations, or entry-level tech roles."
    st.session_state.career = career
    st.session_state.description = description
if st.session_state.career != "":
    st.success(f"✅ Recommended Career: {st.session_state.career}")
    st.info(f"📌 Career Details: {st.session_state.description}")
