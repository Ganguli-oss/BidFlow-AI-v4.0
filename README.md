🏛️ BidFlow AI v4.0: Global Response Architecture Engine

BidFlow AI is an advanced, multi-agent strategic response engine designed to automate the bridge between complex client requirements (RFPs/Tenders) and high-value technical proposals.

Unlike standard "narrative" AI generators, v4.0 focuses on Response Architecture—decomposing tender packs into structured requirements and scaling evidence density based on evaluation weightings.

🚀 Live Demo: https://bidflow-ai-v40-8m764nydqv6kt95tuubpbo.streamlit.app

🌟 Key Features (The v4.0 Evolution)

Following industry insights from professional bid strategists, BidFlow AI v4.0 operates in two distinct, intelligence-driven phases:

Phase 1: Tender Decomposition & Compliance Gating

Project Vault Ingestion: Simultaneously processes multiple documents (ITT, KPIs, Annexes, Pricing).

Compliance Auditor: Automatically flags "Pass/Fail" gates (ISO certifications, GDPR, SOC2, TUPE) against your business identity.

Requirement Mapping: Extracts specific scored questions, word limits, and section weightings.

Phase 2: Weighted Evidence Mapping

Response Architecture: Adjusts detail density proportionally to score weighting (e.g., 30% questions get deep operational modeling; 5% questions get concise compliance clarity).

Evidence Density: Automatically injects relevant KPIs and case studies from institutional knowledge to "prove" capability.

1:1 Mapping: Generates structured, question-by-question responses to prevent "narrative drift."

🛠️ Tech Stack

Orchestration: CrewAI (Multi-Agent Agentic Framework)

Inference: Groq Cloud (Llama-3.3-70B-Versatile)

Frontend: Streamlit

Document Processing: PyPDF2

Architecture: RAG (Retrieval-Augmented Generation)

💻 Local Installation

Clone the repository:

git clone [https://github.com/Ganguli-oss/BidFlow-AI-v4.0.git](https://github.com/Ganguli-oss/BidFlow-AI-v4.0.git)
cd BidFlow-AI-v4.0


Set up Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:

pip install -r requirements.txt


Environment Variables:
Create a .env file and add your Groq API Key:

GROQ_API_KEY=your_api_key_here


Run the App:

streamlit run app.py


🤝 Acknowledgments

Special thanks to Mr. Mo Mohamud for providing the industry insights on tender decomposition and weighted response architecture that shaped version 4.0.

📄 License

Distributed under the MIT License. See LICENSE for more information.
