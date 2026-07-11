import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

# API Key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the resume and return ONLY in this format.

Resume Summary:
(Write a professional summary in 3-4 lines.)

Strengths:
- Point 1
- Point 2
- Point 3

Weaknesses:
- Point 1
- Point 2

Suggestions:
- Point 1
- Point 2
- Point 3

Recommended Job Roles:
- Role 1
- Role 2
- Role 3

Resume:

{resume_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        return """
⚠️ AI service is temporarily unavailable.

Possible Reasons:
• Daily API quota exceeded
• Internet connection issue
• Google Gemini server unavailable

Please try again after a few minutes.
"""


def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are an HR Manager.

Generate a professional cover letter based on the following resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}

Write a one-page professional cover letter.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        return """
⚠️ Cover Letter could not be generated.

Possible Reasons:
• Daily API quota exceeded
• Internet connection issue
• Google Gemini server unavailable

Please try again later.
"""