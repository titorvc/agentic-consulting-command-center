from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from workflow import build_workflow
from utils.db_manager import init_db
from utils.obsidian_manager import list_clients, write_note

# Initialize database on startup
try:
    init_db()
    print("Base de datos PostgreSQL inicializada correctamente.")
except Exception as e:
    print(f"Advertencia al inicializar la base de datos: {e}")

app = FastAPI(title="Agencia IA - Command Center API")

# Configure CORS for Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VAULT_PATH = os.path.expanduser("~/Documents/Consultoria_IA_Agentica/Obsidian_Vault")
if not os.path.exists(VAULT_PATH):
    os.makedirs(VAULT_PATH, exist_ok=True)

# Build Graph globally
graph = build_workflow()

class LeadInput(BaseModel):
    client_name: str
    giro: str
    empleados: int
    pain_points: str
    sistemas: str
    canal_entrada: str = "web"

class ClientRegistration(BaseModel):
    client_name: str

class WorkflowInput(BaseModel):
    client_name: str

def procesar_lead_background(lead: LeadInput):
    initial_state = {
        "client_name": lead.client_name,
        "giro": lead.giro,
        "empleados": lead.empleados,
        "pain_points": lead.pain_points,
        "sistemas": lead.sistemas,
        "canal_entrada": lead.canal_entrada,
        "logs": []
    }
    graph.invoke(initial_state)

@app.get("/api/clients")
async def get_clients():
    clients = list_clients(VAULT_PATH)
    return {"clients": clients}

@app.post("/api/clients")
async def register_client(data: ClientRegistration):
    client_name = data.client_name.strip()
    if not client_name:
        raise HTTPException(status_code=400, detail="El nombre del cliente no puede estar vacío.")
    
    write_note(
        VAULT_PATH, 
        client_name, 
        "README.md", 
        f"# Client {client_name}\nCreated via AI Consulting Command Center.", 
        {"title": "README", "status": "Initialized"}
    )
    return {"status": "success", "client_name": client_name}

@app.post("/api/workflow/start")
async def start_workflow(data: WorkflowInput):
    thread_id = re.sub(r'\W+', '_', data.client_name).lower()
    config = {"configurable": {"thread_id": thread_id}}
    
    state = graph.get_state(config)
    
    if len(state.values) > 0:
        return {"status": "error", "message": "El pipeline ya fue inicializado para este cliente."}
        
    initial_inputs = {
        "client_name": data.client_name,
        "data_path": f"data/{thread_id}_leads.csv",
        "logs": [f"[{data.client_name}] Inicializando el sistema multi-agente..."]
    }
    
    # We run it synchronously up to the first interrupt for now, 
    # but could be backgrounded if it takes too long.
    # For a reactive UI, background tasks or WebSockets are better, 
    # but let's do synchronous invoke for the human-in-the-loop pause.
    graph.invoke(initial_inputs, config)
    
    return {"status": "success", "message": "Pipeline iniciado."}

@app.get("/api/workflow/status/{client_name}")
async def get_workflow_status(client_name: str):
    thread_id = re.sub(r'\W+', '_', client_name).lower()
    config = {"configurable": {"thread_id": thread_id}}
    
    state = graph.get_state(config)
    
    if len(state.values) == 0:
        return {"status": "pending", "current_agent": None, "logs": [], "is_completed": False}
        
    current_agent = state.values.get("current_agent")
    logs = state.values.get("logs", [])
    is_completed = not state.next
    awaiting_approval = "human_approval" in state.next
    
    return {
        "status": "running" if not is_completed else "completed",
        "current_agent": current_agent,
        "logs": logs,
        "is_completed": is_completed,
        "awaiting_approval": awaiting_approval
    }

@app.post("/api/workflow/resume/{client_name}")
async def resume_workflow(client_name: str, action: dict):
    # Action could be {"approval": "yes", "feedback": "..."}
    thread_id = re.sub(r'\W+', '_', client_name).lower()
    config = {"configurable": {"thread_id": thread_id}}
    
    state = graph.get_state(config)
    if "human_approval" not in state.next:
        raise HTTPException(status_code=400, detail="No está esperando aprobación humana.")
        
    graph.invoke({"approval_decision": action.get("approval", "yes")}, config)
    return {"status": "success", "message": "Pipeline continuado."}
