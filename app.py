import streamlit as st
import google.generativeai as genai

# Connect to Gemini
genai.configure(api_key="PASTE_YOUR_GEMINI_KEY_HERE")
model = genai.GenerativeModel("gemini-1.5-flash")  # free and fast!

# --- Page Setup ---
st.title("📄 AI Resume Reviewer")
st.write("Paste your resume below and get instant AI feedback!")

# --- User Input ---
resume_text = st.text_area("Paste your resume here:", height=300)
job_title = st.text_input("What job are you applying for? (e.g. Software Engineer)")

# --- The Magic Button ---
if st.button("Review My Resume ✨"):

    if not resume_text:
        st.warning("Please paste your resume first!")
    else:456
        with st.spinner("AI is reviewing your resume..."):

            prompt = f"""
            You are an expert career coach and resume reviewer with 10 years of experience 
            helping candidates land jobs at top companies.

            Please review this resume for a {job_title} position.

            Give feedback on:
            1. ✅ What's strong about this resume
            2. ⚠️ What needs improvement
            3. 💡 3 specific suggestions to make it better
            4. ⭐ Overall score out of 10

            Resume:
            {resume_text}
            """

            response = model.generate_content(prompt)
            st.success("Review Complete!")
            st.markdown(response.text)