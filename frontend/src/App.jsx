import React from 'react';
import './index.css';

function App() {
    return (
        <div className="bg-background text-on-surface min-h-screen flex flex-col font-body-sm relative overflow-x-hidden">
{/* Mobile Top Header */}
<header className="glass-panel w-full h-16 sticky top-0 z-50 flex justify-between items-center px-4 md:hidden border-b-0 shadow-sm">
<button className="text-primary hover:bg-white/5 p-2 rounded-lg transition-colors" id="mobile-menu-btn">
<span className="material-symbols-outlined" style={{"fontVariationSettings": "'FILL' 1"}}>menu</span>
</button>
<h1 className="font-headline-sm text-headline-sm font-black bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary truncate mx-2">Command Center</h1>
<div className="flex gap-2">
<button className="text-on-surface-variant hover:text-on-surface p-2 hover:bg-white/5 rounded-lg">
<span className="material-symbols-outlined">notifications</span>
</button>
</div>
</header>
{/* SideNavBar (Hidden on Mobile, toggled via JS) */}
<nav className="fixed inset-y-0 left-0 z-[60] w-72 transform -translate-x-full transition-transform duration-300 md:hidden bg-surface/90 backdrop-blur-2xl border-r border-white/10 shadow-2xl flex flex-col py-stack-lg" id="mobile-drawer">
<div className="px-6 mb-8 flex justify-between items-center">
<div>
<h2 className="font-headline-sm text-headline-sm font-bold text-primary">Command Center</h2>
<p className="font-label-mono text-label-mono text-on-surface-variant">LangGraph Orchestrator</p>
</div>
<button className="text-on-surface-variant p-1" id="close-menu-btn">
<span className="material-symbols-outlined">close</span>
</button>
</div>
<div className="flex-1 px-4 space-y-2">
<a className="flex items-center gap-3 py-3 font-label-mono text-label-mono text-primary border-l-2 border-primary pl-4 hover:bg-white/5 transition-colors duration-200" href="#">
<span className="material-symbols-outlined">dashboard</span>
                Dashboard
            </a>
<a className="flex items-center gap-3 py-3 font-label-mono text-label-mono text-on-surface-variant pl-4 hover:bg-white/5 transition-colors duration-200" href="#">
<span className="material-symbols-outlined">folder_shared</span>
                Client Vault
            </a>
<a className="flex items-center gap-3 py-3 font-label-mono text-label-mono text-on-surface-variant pl-4 hover:bg-white/5 transition-colors duration-200" href="#">
<span className="material-symbols-outlined">account_tree</span>
                Pipelines
            </a>
<a className="flex items-center gap-3 py-3 font-label-mono text-label-mono text-on-surface-variant pl-4 hover:bg-white/5 transition-colors duration-200" href="#">
<span className="material-symbols-outlined">terminal</span>
                Logs
            </a>
<a className="flex items-center gap-3 py-3 font-label-mono text-label-mono text-on-surface-variant pl-4 hover:bg-white/5 transition-colors duration-200" href="#">
<span className="material-symbols-outlined">settings</span>
                Settings
            </a>
</div>
<div className="px-4 mt-auto">
<button className="w-full py-3 rounded-lg border border-primary text-primary font-label-mono text-label-mono hover:bg-primary/10 transition-colors">
                Register New Client
            </button>
</div>
</nav>
{/* Overlay */}
<div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-[55] hidden transition-opacity duration-300 opacity-0 md:hidden" id="drawer-overlay"></div>
{/* Main Content */}
<main className="flex-1 p-4 md:p-8 flex flex-col gap-4">
{/* Hero Card */}
<section className="glass-panel rounded-xl p-6 relative overflow-hidden">
{/* Decorative Glow */}
<div className="absolute top-0 right-0 w-32 h-32 bg-primary-fixed/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>
<h2 className="font-display-lg text-display-lg text-gradient mb-2 text-2xl md:text-4xl">Agentic Orchestration</h2>
<p className="font-body-sm text-body-sm text-on-surface-variant mb-6 max-w-sm">
                Deploy, monitor, and scale multi-agent cognitive pipelines. System ready for input.
            </p>
<button className="w-full bg-gradient-action text-black font-headline-sm text-sm py-4 rounded-lg shadow-[0_0_20px_rgba(0,220,230,0.3)] active:scale-95 transition-transform flex justify-center items-center gap-2">
<span className="material-symbols-outlined">rocket_launch</span>
                Initialize Agentic Pipeline
            </button>
</section>
{/* Metrics Grid */}
<section className="grid grid-cols-2 gap-3">
<div className="glass-panel rounded-lg p-4 flex flex-col justify-between">
<div className="flex items-center gap-2 text-on-surface-variant mb-2">
<span className="material-symbols-outlined text-sm">speed</span>
<span className="font-label-mono text-xs">Processing</span>
</div>
<div className="font-headline-md text-headline-md text-primary">124ms</div>
</div>
<div className="glass-panel rounded-lg p-4 flex flex-col justify-between">
<div className="flex items-center gap-2 text-on-surface-variant mb-2">
<span className="material-symbols-outlined text-sm">check_circle</span>
<span className="font-label-mono text-xs">Success Rate</span>
</div>
<div className="font-headline-md text-headline-md text-secondary">99.8%</div>
</div>
<div className="glass-panel rounded-lg p-4 flex flex-col justify-between">
<div className="flex items-center gap-2 text-on-surface-variant mb-2">
<span className="material-symbols-outlined text-sm">data_usage</span>
<span className="font-label-mono text-xs">Token Usage</span>
</div>
<div className="font-headline-md text-headline-md text-primary">45.2k</div>
</div>
<div className="glass-panel rounded-lg p-4 flex flex-col justify-between">
<div className="flex items-center gap-2 text-on-surface-variant mb-2">
<span className="material-symbols-outlined text-sm">hub</span>
<span className="font-label-mono text-xs">Active Nodes</span>
</div>
<div className="font-headline-md text-headline-md text-tertiary-fixed">8/12</div>
</div>
</section>
{/* Pipeline Status */}
<section className="glass-panel rounded-xl p-5">
<h3 className="font-label-mono text-label-mono text-on-surface-variant mb-4 flex items-center gap-2 uppercase tracking-wider text-xs">
<span className="material-symbols-outlined text-sm">memory</span>
                Pipeline Status
            </h3>
<div className="flex flex-col gap-3 relative">
{/* Vertical Line Connector */}
<div className="absolute left-[11px] top-4 bottom-4 w-px bg-white/10 z-0"></div>
<div className="flex items-center gap-3 relative z-10">
<div className="w-6 h-6 rounded-full bg-primary/20 border border-primary flex items-center justify-center shadow-[0_0_10px_rgba(224,253,255,0.4)]">
<div className="w-2 h-2 rounded-full bg-primary"></div>
</div>
<span className="font-body-sm text-body-sm text-on-surface flex-1">Data Ingestion</span>
<span className="material-symbols-outlined text-primary text-sm">done</span>
</div>
<div className="flex items-center gap-3 relative z-10">
<div className="w-6 h-6 rounded-full bg-secondary/20 border border-secondary flex items-center justify-center animate-pulse shadow-[0_0_10px_rgba(209,188,255,0.4)]">
<div className="w-2 h-2 rounded-full bg-secondary"></div>
</div>
<span className="font-body-sm text-body-sm text-secondary flex-1 font-medium">Context Analysis</span>
<span className="material-symbols-outlined text-secondary text-sm animate-spin">sync</span>
</div>
<div className="flex items-center gap-3 relative z-10">
<div className="w-6 h-6 rounded-full bg-surface-variant border border-outline flex items-center justify-center">
<div className="w-2 h-2 rounded-full bg-outline"></div>
</div>
<span className="font-body-sm text-body-sm text-on-surface-variant flex-1">Strategy Generation</span>
<span className="material-symbols-outlined text-on-surface-variant text-sm">pending</span>
</div>
<div className="flex items-center gap-3 relative z-10">
<div className="w-6 h-6 rounded-full bg-surface-variant border border-outline flex items-center justify-center">
<div className="w-2 h-2 rounded-full bg-outline"></div>
</div>
<span className="font-body-sm text-body-sm text-on-surface-variant flex-1">Peer Review</span>
<span className="material-symbols-outlined text-on-surface-variant text-sm">pending</span>
</div>
<div className="flex items-center gap-3 relative z-10">
<div className="w-6 h-6 rounded-full bg-surface-variant border border-outline flex items-center justify-center">
<div className="w-2 h-2 rounded-full bg-outline"></div>
</div>
<span className="font-body-sm text-body-sm text-on-surface-variant flex-1">Final Output</span>
<span className="material-symbols-outlined text-on-surface-variant text-sm">pending</span>
</div>
</div>
</section>
{/* Terminal */}
<section className="bg-black border border-white/10 rounded-xl overflow-hidden flex flex-col flex-1 min-h-[250px]">
<div className="bg-surface-container-high px-4 py-2 border-b border-white/10 flex items-center gap-2">
<span className="material-symbols-outlined text-on-surface-variant text-sm">terminal</span>
<span className="font-label-mono text-xs text-on-surface-variant">agent_logs.sh</span>
</div>
<div className="p-4 font-console-text text-console-text text-primary-fixed-dim terminal-scroll overflow-y-auto flex-1">
<div className="opacity-70 mb-1">[SYS] Initializing LangGraph Environment v2.4.1...</div>
<div className="opacity-70 mb-1">[SYS] Loading custom toolsets (8/8) OK</div>
<div className="opacity-70 mb-1">[AGENT:Router] Incoming request ID: 8943-AF</div>
<div className="opacity-70 mb-1">[AGENT:Router] Routing to Specialist Node: DataEng</div>
<div className="opacity-70 mb-1">[AGENT:DataEng] Querying vector DB for context...</div>
<div className="mb-1 text-primary">[AGENT:DataEng] Found 14 relevant documents (latency: 45ms)</div>
<div className="mb-1 flex">
<span className="mr-2">&gt;</span>
<span className="animate-pulse block w-2 h-[1em] bg-primary"></span>
</div>
</div>
</section>
{/* Spacer for bottom padding on mobile */}
<div className="h-4"></div>
</main>

</div>
    );
}

export default App;
