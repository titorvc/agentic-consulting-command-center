# AI Agentic Consulting Command Center

A multi-agent system that automates the intake → diagnosis → proposal workflow of an AI consulting practice.

## Architecture
- **LangGraph workflow** (`workflow.py`, `agents/core_agents.py`): typed shared state (`AgentState`) flows through specialized agents that assess a client's digital maturity, select products from a catalog (`data/catalogo.json`), estimate pricing and draft a proposal.
- **Persistence:** PostgreSQL (`utils/db_manager.py`, Docker Compose) for clients, diagnoses and proposals.
- **Knowledge layer:** every artifact is also written as Markdown into an Obsidian vault (`utils/obsidian_manager.py`), so humans and agents share the same context.
- **Interfaces:** Streamlit command center (`app.py`), FastAPI service (`api/main.py`) and a Vite + Tailwind frontend (`frontend/`).

## Design notes
- Agents are currently deterministic, rule-based nodes with a typed state contract, so LLM-backed agents can be swapped in later without changing the graph or persistence layer.
- Client data (vault, `pgdata/`) is excluded from this repository.

## Run
```bash
docker compose up -d          # PostgreSQL
pip install -r requirements.txt
streamlit run app.py          # or: uvicorn api.main:app --reload
```

**Stack:** Python · LangGraph · FastAPI · Streamlit · PostgreSQL · Docker · React/Vite · Tailwind
