import streamlit as st
from io import StringIO

st.set_page_config(
    page_title="Personalized Job Hunt Copilot",
    page_icon="🧑‍💻",
    layout="centered",
)

st.title("🧑‍💻 Personalized Job Hunt Copilot")
st.subheader("Find your dream job with smart matching!")

st.markdown("---")

# Upload Resume
st.header("📄 Upload Your Resume")
uploaded_resume = st.file_uploader(
    "Choose your resume file (PDF or DOCX)", 
    type=["pdf", "docx"]
)

# Upload Job Description
st.header("💼 Upload Job Description (Optional)")
uploaded_jd = st.file_uploader(
    "Choose the job description file (PDF, DOCX, or TXT)", 
    type=["pdf", "docx", "txt"]
)

st.markdown("---")

# User Inputs
st.header("🛠️ Additional Details")

col1, col2 = st.columns(2)

with col1:
    job_role = st.text_input("Target Job Role", placeholder="e.g., Data Scientist")

with col2:
    location = st.text_input("Preferred Location", placeholder="e.g., Remote, New York")

experience = st.slider("Years of Experience", 0, 30, 1)

skills = st.text_area("Key Skills", placeholder="e.g., Python, Machine Learning, SQL")

st.markdown("---")

# Action Button
if st.button("🚀 Analyze and Suggest Jobs"):
    if uploaded_resume is not None:
        st.success("✅ Resume uploaded successfully!")
    else:
        st.error("⚠️ Please upload your resume to continue.")

    if uploaded_jd is not None:
        st.info("ℹ️ Job description uploaded. Will match your profile!")

    st.balloons()
    st.markdown("🎯 **Finding the best job matches for you...** *(Feature coming soon)*")

st.markdown("---")
st.caption("🔒 Your data stays private. Built with ❤️ by Shireen and your AI Copilot.")
