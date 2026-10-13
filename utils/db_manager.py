import psycopg2
import json

DB_PARAMS = {
    "dbname": "agencia_db",
    "user": "agencia_user",
    "password": "agencia_password123",
    "host": "localhost",
    "port": "5435"
}

def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255),
            giro VARCHAR(255),
            empleados INTEGER,
            pain_points TEXT,
            sistemas_actuales TEXT,
            canal_entrada VARCHAR(100) DEFAULT 'lead',
            estado VARCHAR(100) DEFAULT 'lead',
            nivel_madurez VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS propuestas (
            id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES clients(id),
            productos_propuestos TEXT,
            precio_estimado NUMERIC(10, 2),
            timeline_dias INTEGER,
            pdf_path TEXT,
            aprobada BOOLEAN DEFAULT FALSE
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

def create_client(nombre, canal="web"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clients (nombre, canal_entrada) VALUES (%s, %s) RETURNING id", 
        (nombre, canal)
    )
    client_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return client_id

def update_client_diagnostico(client_id, giro, empleados, pain_points, sistemas, madurez):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients 
        SET giro=%s, empleados=%s, pain_points=%s, sistemas_actuales=%s, nivel_madurez=%s, estado='diagnosticado'
        WHERE id=%s
    """, (giro, empleados, pain_points, sistemas, madurez, client_id))
    conn.commit()
    cursor.close()
    conn.close()

def save_propuesta(client_id, productos_ids, precio, timeline, pdf_path=""):
    conn = get_connection()
    cursor = conn.cursor()
    # Guardar lista como JSON string
    cursor.execute("""
        INSERT INTO propuestas (client_id, productos_propuestos, precio_estimado, timeline_dias, pdf_path)
        VALUES (%s, %s, %s, %s, %s)
    """, (client_id, json.dumps(productos_ids), precio, timeline, pdf_path))
    
    # Update client status
    cursor.execute("UPDATE clients SET estado='propuesta_enviada' WHERE id=%s", (client_id,))
    
    conn.commit()
    cursor.close()
    conn.close()

# No inicializamos aquí para no romper el import si la DB aún no está lista. 
# Deberá llamarse a init_db() desde main.py.
