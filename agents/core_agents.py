from typing import TypedDict, List, Dict, Any
from utils.db_manager import create_client, update_client_diagnostico, save_propuesta
from utils.obsidian_manager import write_note
import json
from pathlib import Path

# Load catalog
with open(Path(__file__).parent.parent / "data" / "catalogo.json") as f:
    CATALOGO = json.load(f)

class AgentState(TypedDict):
    # Intake data
    client_name: str
    canal_entrada: str
    giro: str
    empleados: int
    pain_points: str
    sistemas: str
    
    # Generated state
    client_id: int
    nivel_madurez: str
    evaluacion_md: str
    productos_propuestos: List[str]
    precio_estimado: float
    propuesta_md: str
    
    current_agent: str
    logs: List[str]

def run_intake(state: AgentState) -> Dict[str, Any]:
    # 1. Store in DB
    client_id = create_client(state["client_name"], state.get("canal_entrada", "api"))
    
    # 2. Write to Obsidian
    obsidian_content = f"""## Perfil de Cliente: {state["client_name"]}
- **Canal**: {state.get("canal_entrada")}
- **Giro**: {state["giro"]}
- **Empleados**: {state["empleados"]}
- **Pain Points**: {state["pain_points"]}
- **Sistemas**: {state["sistemas"]}
"""
    vault_path = "/home/titorvc/Documents/Nexus_Vault"
    write_note(vault_path, state["client_name"], f"Perfil_{state['client_name']}.md", obsidian_content)
    
    return {
        "client_id": client_id,
        "current_agent": "intake",
        "logs": state.get("logs", []) + [f"Intake completed for {state['client_name']}"]
    }

def run_diagnostico(state: AgentState) -> Dict[str, Any]:
    # Simulated LLM diagnosis logic (Fast path for passive execution)
    sistemas = state["sistemas"].lower()
    if "ninguno" in sistemas or "excel" in sistemas:
        madurez = "Básico"
    elif "erp" in sistemas or "crm" in sistemas:
        madurez = "Proactivo"
    else:
        madurez = "Reactivo"
        
    update_client_diagnostico(
        state["client_id"], state["giro"], state["empleados"], 
        state["pain_points"], state["sistemas"], madurez
    )
    
    eval_content = f"""## Evaluación de Madurez Digital: {state["client_name"]}
- **Nivel Asignado**: {madurez}
- **Justificación**: Basado en sus sistemas actuales ({state["sistemas"]}) y sus pain points.
"""
    vault_path = "/home/titorvc/Documents/Nexus_Vault"
    write_note(vault_path, state["client_name"], f"Evaluacion_{state['client_name']}.md", eval_content)
    
    return {
        "nivel_madurez": madurez,
        "evaluacion_md": eval_content,
        "current_agent": "diagnostico",
        "logs": state.get("logs", []) + [f"Diagnosis completed: {madurez}"]
    }

def run_matcher(state: AgentState) -> Dict[str, Any]:
    # Match logic based on madurez
    madurez = state["nivel_madurez"]
    if madurez == "Básico":
        prods = ["P1", "P3"] # WhatsApp bot + Reportes
    elif madurez == "Reactivo":
        prods = ["P2", "P4"] # Dashboard + ETL
    else:
        prods = ["P5"] # CRM Inteligente
        
    precio = sum([p["precio_base"] for p in CATALOGO if p["id"] in prods])
    
    save_propuesta(state["client_id"], prods, precio, 14)
    
    propuesta_content = f"""## Propuesta Comercial: {state["client_name"]}
- **Nivel de Madurez**: {madurez}
- **Soluciones Propuestas**: {', '.join(prods)}
- **Inversión Estimada**: ${precio} USD
- **Timeline**: 14 días
"""
    vault_path = "/home/titorvc/Documents/Nexus_Vault"
    write_note(vault_path, state["client_name"], f"Propuesta_{state['client_name']}.md", propuesta_content)
    
    return {
        "productos_propuestos": prods,
        "precio_estimado": precio,
        "propuesta_md": propuesta_content,
        "current_agent": "matcher",
        "logs": state.get("logs", []) + [f"Matcher completed: {prods} for ${precio}"]
    }
