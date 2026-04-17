import streamlit as st

st.set_page_config(page_title="AI Paper Grader", layout="wide")

st.title("📝 AI Student Paper Evaluator")
st.subheader("Automated grading based on reference textbooks")

with st.sidebar:
    st.header("Configuration")
    # 1. Upload Holybook
    holybook = st.file_uploader("Upload Reference Textbook (PDF)", type="pdf")
    
    # 2. Upload Question Paper
    q_paper = st.file_uploader("Upload Question Paper (PDF/Text)", type=["pdf", "txt"])
    
    # 3. Accuracy Threshold
    threshold = st.slider("Accuracy Threshold (%)", 0, 100, 50)
    
    st.info(f"The AI will award marks if the answer matches at least {threshold}% of the textbook's context.")

# Main UI
col1, col2 = st.columns(2)

with col1:
    st.header("Student Submission")
    # 4. Student Answer Sheet
    student_pdf = st.file_uploader("Upload Student Answer Sheet (Handwritten PDF)", type="pdf")

with col2:
    st.header("Grading Actions")
    if st.button("Analyze & Compare"):
        if not (holybook and student_pdf and q_paper):
            st.error("Please upload all required documents first.")
        else:
            with st.spinner("Processing Handwriting & Comparing with Textbook..."):
                # Placeholder for the logic we'll build next
                st.warning("OCR and LLM Logic will be integrated here.")
                
                # Mock Result
                st.success("Analysis Complete!")
                st.metric(label="Suggested Score", value="75/100")
