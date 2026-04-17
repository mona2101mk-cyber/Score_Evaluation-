import streamlit as st
from google import genai  # Use the new import
from google.genai import types

# Setup API Key
st.sidebar.header("API Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")


# client = genai.Client(api_key=api_key)
# print("Models supporting generateContent:")
# for m in client.models.list():
#     if "generateContent" in m.supported_actions:
#         print(f"- {m.name}")

if api_key:
    # Initialize the client
    client = genai.Client(api_key=api_key)

    if st.sidebar.button("Run Comparison"):
        # Placeholders for student text and question
        student_text = "Primary Key is a unique identifier for a record in a table."
        question = "What is a Primary Key?"
        threshold = 50 # Example threshold from your UI
        
        prompt = f"""
        You are an expert professor. Compare the Student Answer against the Textbook context.
        Question: {question}
        Student Answer: {student_text}
        
        Grading Criteria:
        1. Accuracy Threshold: {threshold}%
        2. Max Marks: 10
        
        Return the score and a brief justification.
        """
        
        try:
            response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)
            st.write("### Evaluation Result")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")


# - models/gemini-2.5-flash-image
# - models/gemini-3-pro-preview
# - models/gemini-3-flash-preview
# - models/gemini-3.1-pro-preview
# - models/gemini-3.1-pro-preview-customtools
# - models/gemini-3.1-flash-lite-preview
# - models/gemini-3-pro-image-preview
# - models/nano-banana-pro-preview
# - models/gemini-3.1-flash-image-preview
# - models/lyria-3-clip-preview
# - models/lyria-3-pro-preview
# - models/gemini-3.1-flash-tts-preview
# - models/gemini-robotics-er-1.5-preview
# - models/gemini-robotics-er-1.6-preview
# - models/gemini-2.5-computer-use-preview-10-2025
# - models/deep-research-pro-preview-12-2025