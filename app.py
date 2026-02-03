import streamlit as st
import pypdf
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Page Config
st.set_page_config(page_title="AI Resume Roaster", page_icon="🔥")

# 2. Main Title
st.title("🔥 AI Resume Roaster")

# 3. Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key:", type="password")

# 4. Functions
def extract_text_from_pdf(file):
    pdf_reader = pypdf.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text, job_desc, api_key):
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7, openai_api_key=api_key)
    
    prompt_text = """
    You are a harsh technical recruiter. 
    Job Description: {job_desc}
    Resume Text: {resume_text}
    
    Task:
    1. Match score (0-100).
    2. 3 Missing keywords.
    3. Brutal critique.
    4. Rewrite one bullet point.
    """
    
    prompt = ChatPromptTemplate.from_template(prompt_text)
    chain = prompt | llm
    return chain.invoke({"job_desc": job_desc, "resume_text": resume_text}).content

# 5. UI Layout
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
with col2:
    job_description = st.text_area("Paste Job Description")

if st.button("🔥 Roast My Resume"):
    if not api_key:
        st.error("Please enter an API Key in the sidebar.")
    elif uploaded_file and job_description:
        with st.spinner("Analyzing..."):
            try:
                text = extract_text_from_pdf(uploaded_file)
                response = analyze_resume(text, job_description, api_key)
                st.markdown(response)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Upload both files first!")