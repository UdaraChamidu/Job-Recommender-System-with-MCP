# 🤹 AI Job Recommender

An AI-powered job recommender system that analyzes resumes, identifies skill gaps, suggests career roadmaps, and fetches live job postings from **LinkedIn** and **Naukri** using [Apify](https://apify.com/) scrapers.  
Built with **Streamlit**, **OpenAI GPT**, and **Apify API**.  

---

## 🚀 Features
- Upload your **resume (PDF)** and extract text automatically.
- Get an **AI-generated summary** of your resume.
- Detect **skill gaps** and missing experiences for better opportunities.
- Generate a **personalized career roadmap**.
- Fetch real-time job postings from:
  - 💼 LinkedIn
  - 💼 Naukri (Sri Lanka)
- Optional: Integrate with **MCP (Model Context Protocol)** as tools for external agents.

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – frontend for user interaction.
- [OpenAI GPT-3.5](https://platform.openai.com/) – for resume analysis, summaries, and recommendations.
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) – PDF text extraction.
- [Apify Python Client](https://docs.apify.com/sdk/python) – fetch jobs from LinkedIn and Naukri scrapers.
- [MCP (FastMCP)](https://github.com/modelcontextprotocol/servers) – optional external tool integration.

---

## 📂 Project Structure

```
├── app.py # Streamlit app
├── mcp_server.py # MCP server exposing job tools
├── src
│ ├── helper.py # Resume parsing & OpenAI utilities
│ └── job_api.py # Job fetchers (LinkedIn & Naukri via Apify)
├── requirements.txt # Dependencies (create this yourself)
└── README.md # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/job-recommender.git
cd job-recommender
```

### Set up environment variables

- Create a .env file in the root folder:

```
OPENAI_API_KEY=your_openai_api_key
APIFY_API_KEY=your_apify_api_key

```










# helper.py

## to get apify api key, (for linkedin jobs)
- goto apify site and apify store
- goto store and search for linedin
- goto "LinkedIn Jobs Scraper" and goto API endpoints
- goto manage tokens and copy
- 
- then go back(goto api, api client) and find python related code (sdk)
- copy python command and paste inside the function in helper.py (before paste it, it was changed)

## Naukri Jobs Scraper (for nakuri jobs)
- do the same things as above

### one token is enough for all apify tools. also try to find free clients

# MCP part

- uv add "mcp[cli]"
- mcp dev mcp_server.py
