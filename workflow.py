from langgraph.graph import StateGraph, END
from agents.core_agents import AgentState, run_intake, run_diagnostico, run_matcher

def build_workflow():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("intake", run_intake)
    workflow.add_node("diagnostico", run_diagnostico)
    workflow.add_node("matcher", run_matcher)
    
    workflow.set_entry_point("intake")
    
    workflow.add_edge("intake", "diagnostico")
    workflow.add_edge("diagnostico", "matcher")
    workflow.add_edge("matcher", END)
    
    return workflow.compile()
