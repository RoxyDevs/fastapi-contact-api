from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Modelo de datos
class Contact(BaseModel):
    name: str
    email: str
    phone: str

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('contacts.db')
    conn.row_factory = sqlite3.Row
    return conn

# Crear tabla si no existe
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Rutas de la API
@app.get("/")
def read_root():
    return {"message": "API de Gestión de Contactos con FastAPI"}

@app.post("/contacts/")
def create_contact(contact: Contact):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
        (contact.name, contact.email, contact.phone)
    )
    conn.commit()
    conn.close()
    return {"message": "Contacto creado correctamente"}

@app.get("/contacts/")
def get_contacts():
    conn = get_db_connection()
    contacts = conn.execute("SELECT * FROM contacts").fetchall()
    conn.close()
    return {"contacts": [dict(contact) for contact in contacts]}

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    conn = get_db_connection()
    conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
    return {"message": "Contacto eliminado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
