# 🔥 AI Resume Roaster

A Streamlit-based web application that utilizes LangChain and OpenAI's GPT-4o to provide brutal, honest feedback on your resume. It compares your PDF resume against a specific job description to give you a match score, identify missing keywords, and offer actionable (if harsh) improvements.

## 🚀 Features
* **PDF Text Extraction:** Automatically parses uploaded PDF resumes using `pypdf`.
* **AI-Powered Analysis:** Leverages the `gpt-4o` model for high-level reasoning and critique.
* **Recruiter Persona:** Configured to act as a "harsh technical recruiter" to provide realistic, no-nonsense feedback.
* **Actionable Output:** * Match score (0-100).
    * Identification of 3 missing keywords.
    * A brutal critique of the overall profile.
    * A professional rewrite of one specific bullet point.

## 🛠️ Tech Stack
* **Language:** Python
* **Web Framework:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/)
* **AI Model:** OpenAI GPT-4o
* **PDF Library:** PyPDF
