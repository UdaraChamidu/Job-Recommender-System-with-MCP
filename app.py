import streamlit as  st  
from src.helper import extract_text_from_pdf, ask_openai
from src.job_api import fetch_linkedin_jobs, fetch_nakuri_jobs

# set the configuration
st.set_page_config(
    page_title="Job Search Assistant",
    layout="wide"
)
st.title("AI Job Recommender 🤹")
st.markdown("Upload your resume and get job recommendations!")

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text from Rusume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted successfully!")

    with st.expander("Summarizing Your Resume..."):
        summary = ask_openai(f"Summarize the following resume highlighting the skills, education, projects, and experience:\n\n{resume_text}", max_tokens=100)
        
    with st.expander("Finding skill Gaps..."):
        gaps = ask_openai(f"Analyze the following resume and highlight missing skills, projects and experiences needed for better Job opportunities:\n\n{resume_text}", max_tokens=400)

    with st.expander("Creating future roadmaps..."):
        roadmap = ask_openai(f"Based on this resume, what are the potential career paths and skill development opportunities?\n\n{resume_text}", max_tokens=400)

    # Display in a nice format
    st.markdown("---")
    st.header("Resume Summary")
    st.markdown(f"<div style='background-color:#f0f0f0; padding:10px; border-radius:5px;'>{summary}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("Skill Gaps Analysis")
    st.markdown(f"<div style='background-color:#f0f0f0; padding:10px; border-radius:5px;'>{gaps}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("Future Career Roadmap")
    st.markdown(f"<div style='background-color:#f0f0f0; padding:10px; border-radius:5px;'>{roadmap}</div>", unsafe_allow_html=True)          
    
    st.success("Analysis complete Successfully !")
    
    
    # fetch jobs
    if st.button("Set Job Recommendations"):
        with st.spinner("Finding Job Recommendations..."):
            keywords = ask_openai(f"Extract keywords, best job titles from the following resume. Give a comma separated list. no explain needed:\n\n{summary}", max_tokens=100)
            
            search_keywords_clean = keywords.replace("\n", "").strip()
            
        st.success(f"Extracted Job keywords: {search_keywords_clean}")

        with st.spinner("Finding Jobs ..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)
            nakuri_jobs = fetch_nakuri_jobs(search_keywords_clean, rows=60)           