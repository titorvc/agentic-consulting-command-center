import streamlit as st
import os
import re
from workflow import build_workflow, AgentState
from utils.obsidian_manager import (
    list_clients, 
    get_client_dir, 
    list_client_notes, 
    read_note, 
    write_note
)

# Page configuration
st.set_page_config(
    page_title="AI Agentic Consulting Command Center",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Vault configuration
VAULT_PATH = os.path.expanduser("~/Documents/Consultoria_IA_Agentica/Obsidian_Vault")
if not os.path.exists(VAULT_PATH):
    os.makedirs(VAULT_PATH, exist_ok=True)

# CSS Custom styling for Glassmorphism & Modern aesthetics
st.markdown("""
<style>
    /* Main container background */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(15, 23, 42, 1) 0%, rgba(9, 15, 29, 1) 90%);
        color: #e2e8f0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.85) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Headers typography */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Glassmorphic elements */
    .glass-card {
        background: rgba(30, 41, 59, 0.45);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.25);
        margin-bottom: 20px;
    }
    
    .glass-header {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Terminal Console style for logs */
    .console-log {
        font-family: 'Fira Code', 'Courier New', Courier, monospace;
        background-color: rgba(15, 23, 42, 0.9);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 15px;
        border-radius: 8px;
        height: 250px;
        overflow-y: auto;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    /* Status indicator styling */
    .status-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    /* Buttons customization */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25);
    }
    
    /* Custom divider line */
    .custom-hr {
        border: 0;
        height: 1px;
        background: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title Header
st.markdown("""
<div class="glass-header">
    <h1 style="margin:0; font-size: 2.2rem; background: linear-gradient(90deg, #38bdf8 0%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">
        🤖 AGENTIC CONSULTING COMMAND CENTER
    </h1>
    <p style="margin:6px 0 0 0; color: #94a3b8; font-size: 1rem; font-weight: 500;">
        Human-in-the-loop multi-agent system powered by LangGraph & Obsidian
    </p>
</div>
""", unsafe_allow_html=True)

# Build Graph once in session state
if "graph" not in st.session_state:
    st.session_state.graph = build_workflow()

# Sidebar: Client selection
st.sidebar.markdown("### 📁 Client Vault")
clients = list_clients(VAULT_PATH)

# Option to add a new client
new_client_name = st.sidebar.text_input("➕ Register New Client", placeholder="e.g. Acme Corp...")
if st.sidebar.button("Register Client") and new_client_name.strip():
    client_name = new_client_name.strip()
    # Write a dummy readme to trigger folder creation
    write_note(
        VAULT_PATH, 
        client_name, 
        "README.md", 
        f"# Client {client_name}\nCreated via AI Consulting Command Center.", 
        {"title": "README", "status": "Initialized"}
    )
    st.sidebar.success(f"Client '{client_name}' registered!")
    st.rerun()

# Select client dropdown
if clients:
    selected_client = st.sidebar.selectbox("Active Client Profile", clients)
else:
    selected_client = None
    st.sidebar.info("No clients registered yet. Register one above!")

if selected_client:
    # Set up thread config
    thread_id = re.sub(r'\W+', '_', selected_client).lower()
    config = {"configurable": {"thread_id": thread_id}}
    
    # Retrieve current state of graph
    state = st.session_state.graph.get_state(config)
    
    # Check if workflow is started for this client
    workflow_started = len(state.values) > 0
    
    # Sidebar status panel
    st.sidebar.markdown("<hr class='custom-hr'>", unsafe_allow_html=True)
    st.sidebar.markdown("### 📊 Agent Pipeline Status")
    
    # Helper to calculate step status
    # Stages order
    stages = [
        ("evaluator", "Evaluador"),
        ("data_engineer", "Data Engineer"),
        ("analyst", "Analista"),
        ("ml_architect", "ML Architect"),
        ("ml_builder", "ML Builder")
    ]
    
    current_active_agent = state.values.get("current_agent") if workflow_started else None
    
    # If completed
    is_completed = workflow_started and not state.next
    
    for key, name in stages:
        if is_completed:
            status_symbol = "🟢"
            status_text = "Approved"
        elif not workflow_started:
            status_symbol = "⚪"
            status_text = "Pending"
        else:
            # We determine based on: which is the current active agent in state
            # If current agent is further down in the list, previous ones are approved
            active_index = -1
            for idx, (k, _) in enumerate(stages):
                if k == current_active_agent:
                    active_index = idx
                    break
            
            # Find index of this key
            key_index = -1
            for idx, (k, _) in enumerate(stages):
                if k == key:
                    key_index = idx
                    break
            
            if key_index < active_index:
                status_symbol = "🟢"
                status_text = "Approved"
            elif key_index == active_index:
                if "human_approval" in state.next:
                    status_symbol = "⏳"
                    status_text = "Awaiting Approval"
                else:
                    status_symbol = "⚙️"
                    status_text = "Running..."
            else:
                status_symbol = "⚪"
                status_text = "Pending"
        
        st.sidebar.markdown(f"**{status_symbol} {name}**  \n*{status_text}*")
        
    st.sidebar.markdown("<hr class='custom-hr'>", unsafe_allow_html=True)
    
    # Main content panels
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Check workflow control
        if not workflow_started:
            st.markdown(f"""
            <div class="glass-card">
                <h3 style="margin-top:0;">🚀 Start Consulting Pipeline for <b>{selected_client}</b></h3>
                <p style="color: #94a3b8; line-height:1.6;">
                    Initiate the collaborative AI agent workflow. The pipeline consists of 5 expert agents cooperating to evaluate 
                    client requirements, write ETL logic, run data exploration, propose machine learning configurations, and build models.
                </p>
                <p style="color: #94a3b8; line-height:1.6;">
                    At each stage, the system will output structured markdown notes directly to your 
                    <b>Obsidian Vault</b> and pause, giving you full review and editing capabilities before proceeding.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Initialize Agentic Pipeline", type="primary", use_container_width=True):
                inputs = {
                    "client_name": selected_client,
                    "data_path": f"data/{thread_id}_leads.csv",
                    "vault_path": VAULT_PATH,
                    "current_agent": "",
                    "human_approved": False,
                    "feedback": "",
                    "logs": ["Workflow initiated by human architect."]
                }
                st.session_state.graph.invoke(inputs, config)
                st.success("Workflow successfully started! Running initial agent...")
                st.rerun()
                
        else:
            # We show active output/editor
            st.markdown(f"### 📝 Active Work Area")
            
            # Retrieve active agent values
            values = state.values
            curr_agent_key = values.get("current_agent")
            
            # Determine matching note filename
            note_filename = ""
            if curr_agent_key == "evaluator":
                note_filename = f"Evaluacion_{selected_client}.md"
                note_title = "Client Feasibility Evaluation"
            elif curr_agent_key == "data_engineer":
                note_filename = f"ETL_{selected_client}.md"
                note_title = "Data Engineering ETL Code"
            elif curr_agent_key == "analyst":
                note_filename = f"EDA_{selected_client}.md"
                note_title = "Exploratory Data Analysis"
            elif curr_agent_key == "ml_architect":
                note_filename = f"Propuesta_ML_{selected_client}.md"
                note_title = "Machine Learning Topology & Proposal"
            elif curr_agent_key == "ml_builder":
                note_filename = f"Entrenamiento_{selected_client}.md"
                note_title = "Model Training Script"
            else:
                note_filename = ""
                note_title = ""
                
            # Render Markdown
            if note_filename:
                metadata, body = read_note(VAULT_PATH, selected_client, note_filename)
                
                st.markdown(f"""
                <div class="glass-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                        <h4 style="margin:0;">📄 {note_title}</h4>
                        <span style="background-color:rgba(56, 189, 248, 0.15); color:#38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); padding:4px 12px; border-radius:12px; font-size:0.8rem; font-weight:600;">
                            Live Obsidian File
                        </span>
                    </div>
                    <div style="background-color: rgba(15, 23, 42, 0.3); border-radius: 8px; padding: 20px; border: 1px solid rgba(255, 255, 255, 0.05); color:#cbd5e1; line-height:1.6;">
                """, unsafe_allow_html=True)
                st.markdown(body)
                st.markdown("</div></div>", unsafe_allow_html=True)
            else:
                if is_completed:
                    st.success("🎉 All Agent stages have been fully completed and approved!")
                    st.markdown("""
                    <div class="glass-card" style="border: 1px solid rgba(34, 197, 94, 0.3); background-color: rgba(34, 197, 94, 0.02);">
                        <h4 style="color:#22c55e !important; margin-top:0;">🏁 Consulting Pipeline Finished</h4>
                        <p style="color:#cbd5e1; margin-bottom:0;">All target assets (ETL, EDA, ML models) have been successfully processed, refined, and documented in the client's Obsidian folder.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.info("Pipeline executing tasks...")
                    
            # Human Console section
            if "human_approval" in state.next:
                st.markdown("<hr class='custom-hr'>", unsafe_allow_html=True)
                st.markdown("### 🎛️ Human Decision Console")
                
                st.markdown(f"""
                <div class="glass-card" style="border: 1px solid rgba(139, 92, 246, 0.3); background-color: rgba(139, 92, 246, 0.02);">
                    <p style="margin:0; color:#c084fc;">The <b>{curr_agent_key.upper().replace('_', ' ')}</b> agent has finalized this step. Review the document above. You can approve to progress to the next agent, or request adjustments by supplying feedback.</p>
                </div>
                """, unsafe_allow_html=True)
                
                feedback_text = st.text_area("📝 Revision Instructions (Only used for Requesting Revision):", placeholder="Describe the changes you want the agent to make...")
                
                btn_col1, btn_col2 = st.columns(2)
                
                with btn_col1:
                    if st.button("🟢 Approve & Proceed", use_container_width=True):
                        # 1. Update state to approved
                        st.session_state.graph.update_state(
                            config,
                            {"human_approved": True, "feedback": ""},
                            as_node="human_approval"
                        )
                        # 2. Resume graph
                        st.session_state.graph.invoke(None, config)
                        st.success("Approved! Advancing workflow...")
                        st.rerun()
                        
                with btn_col2:
                    if st.button("🔴 Request Revision", use_container_width=True):
                        if not feedback_text.strip():
                            st.warning("Please provide clear feedback instructions in the box above so the agent knows what to fix!")
                        else:
                            # 1. Update state to rejected with feedback
                            st.session_state.graph.update_state(
                                config,
                                {"human_approved": False, "feedback": feedback_text.strip()},
                                as_node="human_approval"
                            )
                            # 2. Resume graph
                            st.session_state.graph.invoke(None, config)
                            st.warning("Revision requested! Sending feedback back to the agent...")
                            st.rerun()
            
            # Reset pipeline button in sidebar
            if st.sidebar.button("🔄 Reset Client Workflow State", use_container_width=True):
                st.session_state.graph.update_state(
                    config,
                    {
                        "feasibility_report": "",
                        "etl_code": "",
                        "eda_insights": "",
                        "model_topology": "",
                        "training_code": "",
                        "current_agent": "",
                        "human_approved": False,
                        "feedback": "",
                        "logs": ["Workflow reset by human supervisor."]
                    },
                    as_node="human_approval"
                )
                st.sidebar.warning("Pipeline state reset successfully!")
                st.rerun()

    with col2:
        # Logs and files inspector
        st.markdown("### 🗂️ Obsidian Vault Inspector")
        
        # Display folder content
        st.markdown(f"📁 **Client Folder:** `Obsidian_Vault/Clientes/{selected_client.replace(' ', '_')}/`")
        
        notes = list_client_notes(VAULT_PATH, selected_client)
        if notes:
            selected_note = st.selectbox("Select File to View", notes)
            if selected_note:
                note_meta, note_body = read_note(VAULT_PATH, selected_client, selected_note)
                
                # Show metadata as json
                if note_meta:
                    st.markdown("**YAML Frontmatter:**")
                    st.json(note_meta)
                
                # View text of note
                with st.expander(f"👁️ Preview: {selected_note}", expanded=True):
                    st.code(note_body, language="markdown")
        else:
            st.info("No files in this client folder yet.")
            
        st.markdown("<hr class='custom-hr'>", unsafe_allow_html=True)
        st.markdown("### 🖥️ Workflow Execution Logs")
        
        if workflow_started:
            logs = state.values.get("logs", [])
            log_text = "\n".join([f"[{i+1:02d}] {log}" for i, log in enumerate(logs)])
            st.markdown(f'<div class="console-log">{log_text}</div>', unsafe_allow_html=True)
        else:
            st.info("Initiate pipeline to inspect logs.")
