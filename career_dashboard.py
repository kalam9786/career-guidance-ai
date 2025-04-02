import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini AI
GEMINI_API_KEY = "AIzaSyCk1jS9MuMkLaaxrSL_-reTk9pyeAE9PdM"
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate career guidance
def get_career_advice(user_input):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # Best quality
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Career Guidance", layout="wide")

st.title("🎯 Personalized AI Career Guidance Dashboard")
st.write("🚀 Get career recommendations based on your educational background!")

# Sidebar for user selection
user_type = st.sidebar.selectbox(
    "Select your category:",
    ["12th Passed-Out Students", "UG Graduate Students", "PG Graduates & Job Seekers"]
)

st.sidebar.write("### 🔍 Enter Your Details:")

if user_type == "12th Passed-Out Students":
    percentage = st.sidebar.slider("12th Percentage", 0, 100, 75)
    stream = st.sidebar.selectbox("Stream", ["Science", "Commerce", "Arts", "Vocational"])
    entrance_exam = st.sidebar.text_input("Entrance Exam Scores (JEE, NEET, etc.)")
    extracurriculars = st.sidebar.text_input("Extracurricular Activities")
    interests = st.sidebar.text_area("Skills & Interests")
    career_pref = st.sidebar.selectbox("Career Preference", ["Job-Oriented", "Research", "Government Jobs","Higher studies"])
    financials = st.sidebar.selectbox("Financial Constraints", ["No Constraint", "Need Scholarships", "Budget Constraints"])
    location = st.sidebar.text_input("Preferred Study Location")

    user_data = f"""
    User Type: {user_type}
    Stream: {stream}
    Percentage: {percentage}
    Interests: {interests}
    Career Preference: {career_pref}
    Financial Constraints: {financials}
    """

elif user_type == "UG Graduate Students":
    degree = st.sidebar.selectbox("UG Degree & Specialization", ["B.Tech CSE", "B.Tech ECE", "B.Tech Mechanical", "BBA AIML", "BBA Finance", "B.Com", "B.Sc Physics", "BA Economics"])
    cgpa = st.sidebar.slider("CGPA / Percentage", 0.0, 10.0, 8.0)
    internships = st.sidebar.text_input("Number of Internships & Work Experience")
    projects = st.sidebar.text_area("Major Projects & Research")
    certifications = st.sidebar.text_area("Certifications & Online Courses")
    skills = st.sidebar.text_area("Technical & Soft Skills")
    job_or_pg = st.sidebar.selectbox("Career Path", ["Job", "Higher Studies"])
    exams = st.sidebar.text_input("Exams Cleared (CAT, GATE, GRE, etc.)")

    user_data = f"""
    User Type: {user_type}
    Degree: {degree}
    CGPA: {cgpa}
    Skills: {skills}
    Career Path: {job_or_pg}
    Certifications: {certifications}
    """

    if job_or_pg == "Higher Studies":
        user_data += "\nSuggested Universities and Programs: \n"
        user_data += "- MIT (MS in AI, Data Science)\n"
        user_data += "- Harvard (MBA, Finance)\n"
        user_data += "- IITs (M.Tech in Core Engineering Fields)\n"
        user_data += "- Alternative: Online Master's (Coursera, edX)"

else:  # PG Graduates & Job Seekers
    pg_degree = st.sidebar.selectbox("PG Degree & Specialization", ["MBA", "M.Tech", "M.Sc", "M.A Economics", "PG Diploma"])
    work_exp = st.sidebar.slider("Years of Work Experience", 0, 30, 2)
    job_roles = st.sidebar.text_area("Past Job Roles & Companies")
    skills = st.sidebar.text_area("Technical & Soft Skills")
    certifications = st.sidebar.text_area("Certifications & Executive Courses")
    industry_interest = st.sidebar.selectbox("Industry Interest", ["IT", "Finance", "Marketing", "Consulting", "Healthcare"])
    job_type = st.sidebar.selectbox("Job Type", ["Full-Time", "Remote", "Freelance", "Contract-Based"])
    salary = st.sidebar.text_input("Expected Salary Range")
    networking = st.sidebar.text_input("Industry Networking & LinkedIn Profile")

    user_data = f"""
    User Type: {user_type}
    PG Degree: {pg_degree}
    Work Experience: {work_exp}
    Industry Interest: {industry_interest}
    Job Type: {job_type}
    Certifications: {certifications}
    """

    user_data += "\nProfessional Development Suggestions: \n"
    user_data += "- Resume Tailoring: Highlight leadership & problem-solving\n"
    user_data += "- Certifications: PMP, CFA, AWS, Digital Marketing\n"
    user_data += "- Salary Improvement: Negotiation skills, Advanced technical training\n"
    user_data += "- Networking: Active LinkedIn presence, Industry conferences"

# Get career recommendations
if st.sidebar.button("Get Career Guidance"):
    with st.spinner("🤖 AI is analyzing your profile..."):
        advice = get_career_advice(user_data)
    
    st.subheader("🎯 AI Career Recommendation")
    st.write(advice)

# Footer
st.markdown("---")
st.markdown("💡 **Powered by Gemini AI | Built with ❤️ using Streamlit**")
