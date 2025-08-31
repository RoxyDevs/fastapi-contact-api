# Crear un README más profesional
cat > README.md << 'EOF'
# 🚀 FastAPI Contact Management API

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/RoxyDevs/fastapi-contact-api)](https://github.com/RoxyDevs/fastapi-contact-api/issues)
[![GitHub Forks](https://img.shields.io/github/forks/RoxyDevs/fastapi-contact-api)](https://github.com/RoxyDevs/fastapi-contact-api/network)
[![GitHub Stars](https://img.shields.io/github/stars/RoxyDevs/fastapi-contact-api)](https://github.com/RoxyDevs/fastapi-contact-api/stargazers)

Una API REST moderna y eficiente para la gestión de contactos, desarrollada con **FastAPI** y **SQLite**. Perfecta para demostrar habilidades en desarrollo backend con Python.

## ✨ Características

- ✅ **Operaciones CRUD completas** - Crear, leer, actualizar y eliminar contactos
- ✅ **Base de datos SQLite** - Almacenamiento persistente y ligero
- ✅ **Validación de datos** - Con Pydantic para entradas seguras
- ✅ **Documentación automática** - Interfaz Swagger/OpenAPI integrada
- ✅ **Manejo de errores** - Respuestas HTTP apropiadas
- ✅ **Ready for Production** - Estructura escalable y mantenible

## 🛠️ Stack Tecnológico

- **Python 3.11** - Lenguaje de programación principal
- **FastAPI** - Framework web moderno y rápido
- **SQLite** - Base de datos embebida
- **Pydantic** - Validación de datos y serialización
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **GitHub Actions** - CI/CD integrado

## 📦 Instalación y Uso

### Prerrequisitos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Instalación Local

1. **Clonar el repositorio**
```bash
git clone https://github.com/RoxyDevs/fastapi-contact-api.git
cd fastapi-contact-api
Crear entorno virtual

bash
python -m venv venv
source venv/Scripts/activate  # Git Bash
# o
venv\Scripts\activate.bat     # CMD
Instalar dependencias

bash
pip install -r requirements.txt
Ejecutar la aplicación

bash
uvicorn main:app --reload
Acceder a la API

🔗 API: http://127.0.0.1:8000

📖 Documentación Swagger: http://127.0.0.1:8000/docs

📚 Documentación Redoc: http://127.0.0.1:8000/redoc

📡 Endpoints de la API
🔹 Información General
GET / - Información básica de la API

🔹 Gestión de Contactos
POST /contacts/ - Crear un nuevo contacto

GET /contacts/ - Obtener todos los contactos

GET /contacts/{id} - Obtener un contacto específico

DELETE /contacts/{id} - Eliminar un contacto

🎯 Ejemplos de Uso
Crear un contacto
bash
curl -X POST "http://127.0.0.1:8000/contacts/" \
-H "Content-Type: application/json" \
-d '{"name": "Juan Perez", "email": "juan@email.com", "phone": "123456789"}'
Obtener todos los contactos
bash
curl "http://127.0.0.1:8000/contacts/"
🧪 Testing
bash
# Instalar pytest
pip install pytest

# Ejecutar tests
pytest
🤝 Contribución
¡Las contribuciones son bienvenidas!

Fork el proyecto

Crear una feature branch (git checkout -b feature/AmazingFeature)

Commit los cambios (git commit -m 'Add AmazingFeature')

Push a la branch (git push origin feature/AmazingFeature)

Abrir un Pull Request

📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE.md para más detalles.

👥 Autor
Roxana Rolón - GitHub - LinkedIn - 📧 roxdev2023@gmail.com
