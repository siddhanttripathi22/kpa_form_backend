# 🚀 KPA Form Backend API

This is the **KPA Form Backend API**, a backend service developed using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It supports CRUD operations for managing **Wheel** and **Bogie** inspection forms, with Dockerized deployment and interactive API documentation.

---

## 📦 Features

- ⚡ High-performance API with FastAPI
- 🧱 SQLAlchemy ORM for PostgreSQL (or SQLite in development)
- 🧾 Pydantic for strict data validation
- 🧪 Modular architecture: `CRUD`, `routers`, `schemas`, `models`
- 📦 Docker and Docker Compose support
- 🧬 Auto-generated Swagger UI and Redoc docs
- 🛡️ Ready for production enhancements (Auth, Tests, CI/CD)

---

## 📁 Project Structure

kpa_form_backend/
├── app/
│ ├── init.py
│ ├── main.py # App entry point
│ ├── database.py # SQLAlchemy engine and session
│ ├── models/ # SQLAlchemy models
│ │ ├── init.py
│ │ ├── wheel.py
│ │ └── bogie.py
│ ├── schemas/ # Pydantic schemas
│ │ ├── init.py
│ │ ├── wheel.py
│ │ └── bogie.py
│ ├── crud/ # Business logic
│ │ ├── init.py
│ │ ├── wheel.py
│ │ └── bogie.py
│ └── routers/ # API route definitions
│ ├── init.py
│ ├── wheel.py
│ └── bogie.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## 🧰 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)

---

## 🏁 Getting Started

### ✅ Prerequisites

- Python 3.10 or higher
- Docker & Docker Compose (for containerized setup)

---

### 🔧 Installation (Local)

1. **Clone the Repository**

```bash git clone https://github.com/your-username/kpa-form-backend.git
cd kpa-form-backend
Set up virtual environment and install dependencies


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Run the development server


uvicorn app.main:app --reload
Access the API locally

Root: http://localhost:8000

Swagger UI: http://localhost:8000/docs



🐳 Run with Docker
1. Build and run containers

docker-compose up --build
2. Access the API
API Root: http://localhost:8000

Swagger UI: http://localhost:8000/docs



📜 API Endpoints Overview
Method	Endpoint	Description
GET	/	Root welcome message
GET	/api/forms/wheel-specifications	Get or filter wheel forms
POST	/api/forms/wheel-specifications	Submit a new wheel form
GET	/api/forms/bogie-checksheets	Get or filter bogie forms
POST	/api/forms/bogie-checksheets	Submit a new bogie form

🗂️ Sample JSON Payload
✅ Create Wheel Specification
json
Copy
Edit
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "EngineerX",
  "submittedDate": "2025-07-19",
  "fields": {
    "material": "Carbon Steel",
    "diameter": "800mm",
    "supplier": "XYZ Corp"
  }
}
🛠 Environment Variables
If you're using PostgreSQL, define the following in a .env file:

env

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/kpa_db
Or adjust inside app/database.py if hardcoded.

🐳 ##Docker Setup

Dockerfile
Dockerfile
Copy
Edit
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
🧪 Future Improvements
✅ Add Alembic for DB migrations

🔐 Implement authentication (JWT or OAuth2)

🧪 Add unit & integration tests

🚀 Setup CI/CD (GitHub Actions, etc.)

📊 Centralized logging & monitoring

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

🙋‍♂️ Author
Siddhant Tripathi
Backend Developer | FastAPI Enthusiast

📬 Contact
✉️ Email: siddhanttripathi22@gmail.com






