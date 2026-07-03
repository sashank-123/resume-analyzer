import streamlit as st
import pdfplumber
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6LfOfOwchVttNAcDL6Y1KgQG_OVWH6m9OTphkB4BGt5zg")

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

st.title("AI Resume Analyzer")
job_role = st.text_input(
    "Target Job Role"
)
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    response = model.generate_content(
        f"""
You are an ATS Resume Analyzer.

Analyze this resume.

Give:

1. Resume Score out of 100

2. Strengths

3. Weak Areas

4. ATS Feedback

5. Missing Skills

6. Improvement Suggestions

Resume:

{text}
"""
    )

    st.write(response.text)