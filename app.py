import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM
import pypdf as PyPDF2
import os
from dotenv import load_dotenv

# --- 1. ENVIRONMENT SETUP ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Ultra-low temperature (0.1) for surgical precision in requirement mapping
my_llm = LLM(
    model="groq/llama-3.3-70b-versatile", 
    api_key=GROQ_API_KEY,
    temperature=0.1 
)

# --- 2. ADVANCED HELPER FUNCTIONS ---
def extract_text_from_multiple_pdfs(pdf_files):
    """Creates a 'Project Vault' context from all uploaded documents worldwide."""
    combined_text = ""
    for pdf_file in pdf_files:
        reader = PyPDF2.PdfReader(pdf_file)
        combined_text += f"\n--- SOURCE DOCUMENT: {pdf_file.name} ---\n"
        for page in reader.pages:
            content = page.extract_text()
            if content:
                combined_text += content
    return combined_text

def load_business_profile():
    """Loads your global company strengths."""
    try:
        # Changed to business_profile.txt to match your file naming
        with open("business_profile.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Global Software Engineering firm specializing in AI Automation and Enterprise RAG."

# --- 3. UI SETUP ---
st.set_page_config(page_title="BidFlow AI v4.0 | Global Response Architect", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 4px; font-weight: bold; height: 3.5em; background-color: #1E1E1E; color: white; }
    .status-box { padding: 20px; border-radius: 10px; background-color: white; border-left: 5px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ BidFlow AI v4.0: Global Response Architecture Engine")
st.markdown("**Worldwide Decomposition | Compliance Gating | Weighted Evidence Mapping**")
st.divider()

# --- 4. SIDEBAR: INSTITUTIONAL KNOWLEDGE ---
with st.sidebar:
    st.header("🗄️ Institutional Knowledge")
    profile = load_business_profile()
    if st.checkbox("View Global Business Identity"):
        st.info(profile)
    st.divider()
    st.caption("Standards: ISO/IEC, GDPR, SOC2 & Global Compliance Frameworks")

# --- 5. THE DECOMPOSITION PHASE ---
st.subheader("📂 Phase 1: Global Tender Pack Decomposition")
uploaded_files = st.file_uploader(
    "Upload Tender Pack (RFP, ITT, Statement of Work, Terms, etc.)", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files:
    if 'tender_vault' not in st.session_state:
        with st.spinner("Synchronizing Global Project Vault..."):
            st.session_state.tender_vault = extract_text_from_multiple_pdfs(uploaded_files)
            st.success(f"Vault synchronized with {len(uploaded_files)} international documents.")

    # DECOMPOSITION BUTTON
    if st.button("🔍 Decompose Tender & Audit Compliance Gates"):
        with st.status("Performing Phase 1: Global Tender Decomposition...", expanded=True) as status:
            
            analyst = Agent(
                role='Global Tender Analyst',
                goal='Identify scored questions, weightings, limits, and international compliance gates.',
                backstory='Expert in worldwide procurement frameworks (US Federal, EU, Middle East, UK). Specialist in identifying hidden requirements.',
                llm=my_llm,
                allow_delegation=False
            )

            decomposition_task = Task(
                description=(
                    f"Decompose this tender pack: {st.session_state.tender_vault[:15000]}. "
                    "1. Extract EVERY Scored Question/Section with its ID. "
                    "2. Extract the Weighting (%) and Word/Character Limit for each. "
                    "3. Identify all 'Pass/Fail' Compliance Gates (Insurance, ISO, GDPR, SOC2, Labor Laws, TUPE, etc.). "
                    "4. Flag all mandatory attachments required for submission."
                ),
                expected_output="A structured list of Questions, Weightings, Limits, and a 'Compliance Gate' checklist.",
                agent=analyst
            )

            gatekeeper = Agent(
                role='International Risk Auditor',
                goal='Compare business profile against global Pass/Fail gates to identify disqualification risks.',
                backstory='Specialist in vetting supplier eligibility for high-stakes international contracts.',
                llm=my_llm
            )

            compliance_task = Task(
                description=(
                    f"Compare the identified Pass/Fail gates against our profile: {profile}. "
                    "Look for gaps in security certifications, regional data laws, or mandatory operational levels."
                ),
                expected_output="A Global Pass/Fail risk report. If we fail a regional gate, explain the specific risk.",
                agent=gatekeeper
            )

            crew_v4_phase1 = Crew(
                agents=[analyst, gatekeeper],
                tasks=[decomposition_task, compliance_task],
                process=Process.sequential
            )

            results = crew_v4_phase1.kickoff()
            st.session_state.decomp_results = results
            status.update(label="Global Decomposition Complete!", state="complete", expanded=False)
        
        st.subheader("📋 Phase 1 Results: Compliance & Scored Map")
        st.markdown(st.session_state.decomp_results.raw)

    # --- 6. THE RESPONSE ARCHITECTURE PHASE ---
    if 'decomp_results' in st.session_state:
        st.divider()
        st.subheader("✍️ Phase 2: Weighted Evidence Mapping & Global Response")
        st.info("The AI is now scaling response depth based on the international weighting model.")
        
        if st.button("🚀 Generate Scored Weighted Responses"):
            with st.status("Architecting responses for global submission...", expanded=True) as status:
                
                bid_architect = Agent(
                    role='Senior Global Response Architect',
                    goal='Draft question-specific responses where depth is proportional to score weighting.',
                    backstory='World-class bid writer specializing in multi-million dollar international proposals.',
                    llm=my_llm,
                    verbose=True
                )

                writing_task = Task(
                    description=(
                        f"Based on the decomposition: {st.session_state.decomp_results.raw} "
                        f"and our profile: {profile}, generate structured responses for EACH question. "
                        "GLOBAL ARCHITECTURE INSTRUCTIONS: "
                        "1. Map answers 1:1 to Question IDs. "
                        "2. For high-weighting questions (>15%), use deep evidence and quantitative KPIs. "
                        "3. For low-weighting questions (<10%), provide surgical compliance clarity. "
                        "4. Ensure strict alignment with the regional evaluation methodology."
                    ),
                    expected_output="A comprehensive set of responses mapped 1:1 to the global tender question numbers.",
                    agent=bid_architect
                )

                crew_v4_phase2 = Crew(agents=[bid_architect], tasks=[writing_task])
                st.session_state.final_responses = crew_v4_phase2.kickoff()
                status.update(label="Global Response Generation Complete!", state="complete", expanded=False)

            st.divider()
            st.subheader("📄 Final Submission-Ready Pack")
            st.markdown(st.session_state.final_responses.raw)
            
            st.download_button(
                label="Download Global Bid Pack",
                data=str(st.session_state.final_responses.raw),
                file_name="Global_BidFlow_Submission.txt",
                mime="text/plain"
            )