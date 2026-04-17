import streamlit as st
from google import genai
import time

st.set_page_config(page_title="AI Text Grader", layout="centered")
st.title("📝 AI Paper Grader (Fast-Text Version)")

# 1. API Initialization
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
client = None
if api_key:
    client = genai.Client(api_key=api_key)

# 2. Textbook (Holybook) Input
st.header("1. Reference Material")
uploaded_holy_txt = st.file_uploader("Upload Textbook (.txt)", type="txt", key="holy")

# 3. Student Answer Input
st.header("2. Student Submission")
uploaded_student_txt = st.file_uploader("Upload Student Answer (.txt)", type="txt", key="student")

# 4. Question Paper & Settings
st.header("3. Questions & Evaluation")
q_paper = st.text_area("Paste Question Paper (e.g. Q1. What is DBMS?)", height=100)
threshold = st.slider("Accuracy Threshold (%)", 0, 100, 50)

if st.button("🚀 Compare and Grade"):
    if not (client and uploaded_holy_txt and uploaded_student_txt and q_paper):
        st.error("Please provide the API Key, Textbook, Student Answer, and Questions.")
    else:
        with st.spinner("Analyzing text and grading..."):
            try:
                # Read contents of both text files
                holy_content = uploaded_holy_txt.read().decode("utf-8")
                student_content = uploaded_student_txt.read().decode("utf-8")

                # The Prompt - Pure Text Comparison
                prompt = f"""
                You are a College Professor. Grade the student's answer based on the textbook.

                TEXTBOOK REFERENCE:
                {holy_content[:20000]} 

                STUDENT'S WRITTEN ANSWER:
                {student_content}

                QUESTION PAPER:
                {q_paper}

                GRADING RULES:
                1. Accuracy Threshold: {threshold}%.
                2. Only award full marks if the student's answer captures the core concepts found in the textbook.
                3. If accuracy is below {threshold}%, be strict with marks.
                4. Provide a score per question and a brief justification.
                """

                st.info("Waiting 20 seconds to respect API rate limits...")
                time.sleep(20)

                # Direct text-to-text call (No file uploads needed)
                response = client.models.generate_content(
                    model='gemma-3-1b-it',
                    contents=prompt
                )
                
                st.markdown("---")
                st.markdown("### 📊 Evaluation Results")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
