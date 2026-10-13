import os
import re
import yaml
from datetime import datetime
from typing import Dict, Any, Tuple, List

def get_client_dir(vault_path: str, client_name: str) -> str:
    """Gets the path to the client's directory inside the Obsidian vault and creates it if it doesn't exist."""
    # Sanitize client name to be safe for directory names
    sanitized_name = re.sub(r'[\\/*?:"<>|]', "", client_name).strip().replace(" ", "_")
    client_dir = os.path.join(vault_path, "Clientes", sanitized_name)
    os.makedirs(client_dir, exist_ok=True)
    return client_dir

def list_clients(vault_path: str) -> List[str]:
    """Lists all clients (directories) inside the Obsidian Clientes folder."""
    clientes_dir = os.path.join(vault_path, "Clientes")
    if not os.path.exists(clientes_dir):
        os.makedirs(clientes_dir, exist_ok=True)
        return []
    
    clients = []
    for entry in os.scandir(clientes_dir):
        if entry.is_dir() and not entry.name.startswith("."):
            clients.append(entry.name.replace("_", " "))
    return sorted(clients)

def write_note(vault_path: str, client_name: str, filename: str, content: str, metadata: Dict[str, Any]) -> str:
    """Writes a note with YAML frontmatter to the client's directory."""
    client_dir = get_client_dir(vault_path, client_name)
    if not filename.endswith(".md"):
        filename += ".md"
    
    file_path = os.path.join(client_dir, filename)
    
    # Ensure standard metadata fields are present
    if "date" not in metadata:
        metadata["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "client" not in metadata:
        metadata["client"] = client_name
        
    # Build YAML frontmatter
    frontmatter = yaml.dump(metadata, sort_keys=False, default_flow_style=False)
    
    full_content = f"---\n{frontmatter}---\n\n{content}"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    return file_path

def read_note(vault_path: str, client_name: str, filename: str) -> Tuple[Dict[str, Any], str]:
    """Reads a note and parses its YAML frontmatter."""
    client_dir = get_client_dir(vault_path, client_name)
    if not filename.endswith(".md"):
        filename += ".md"
        
    file_path = os.path.join(client_dir, filename)
    if not os.path.exists(file_path):
        return {}, ""
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Match frontmatter using regex
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if frontmatter_match:
        yaml_content = frontmatter_match.group(1)
        body = frontmatter_match.group(2)
        try:
            metadata = yaml.safe_load(yaml_content) or {}
            return metadata, body
        except Exception:
            return {}, body
            
    return {}, content

def list_client_notes(vault_path: str, client_name: str) -> List[str]:
    """Lists all markdown notes for a specific client."""
    client_dir = get_client_dir(vault_path, client_name)
    notes = []
    for file in os.listdir(client_dir):
        if file.endswith(".md"):
            notes.append(file)
    return sorted(notes)
