from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API de Gestión de Contactos"}

def test_create_contact():
    response = client.post(
        "/contacts/",
        json={"name": "Test User", "email": "test@email.com", "phone": "123456789"}
    )
    assert response.status_code == 200
    assert "message" in response.json()

def test_get_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
