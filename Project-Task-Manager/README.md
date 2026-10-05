# 📋 Task Manager REST API

A production-ready Task Management API built with **Django**, **Django REST Framework (DRF)**, and **drf-spectacular** (OpenAPI 3.0 & Swagger UI).

---

## 🌟 Key Features

- **Full RESTful CRUD**: Create, Retrieve, Update, and Delete operations for tasks.
- **Advanced Querying**:
  - Exact filtering by `status` (`TODO`, `IN_PROGRESS`, `DONE`) and `priority` (`LOW`, `MEDIUM`, `HIGH`).
  - Text search across `title` and `description`.
  - Field sorting (`ordering=-created_at`, `ordering=due_date`, etc.).
- **Pagination**: Built-in `PageNumberPagination` (10 items per page).
- **Interactive API Documentation**: Live Swagger UI and ReDoc generated dynamically from serializers.
- **Admin Dashboard**: Configured Django Admin with search and filters.
- **Database Abstraction**: SQLite for local rapid development, ready for PostgreSQL in production.

---

## 🏗️ Architecture & Project Structure

```text
Project-Task-Manager/
├── config/                  # Project configuration
│   ├── settings.py          # DRF, Swagger, and DB configurations
│   ├── urls.py              # Central routing & Swagger endpoints
│   ├── wsgi.py              # WSGI entry point
│   └── asgi.py              # ASGI entry point
├── tasks/                   # Tasks application
│   ├── models.py            # Task data model & choices
│   ├── serializers.py       # DRF ModelSerializer & input validation
│   ├── views.py             # TaskViewSet with filter/search backends
│   ├── admin.py             # Django admin customization
│   └── migrations/          # Database migration history
├── manage.py                # Django CLI management script
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1. Environment & Dependencies
Ensure your virtual environment is active:
```powershell
..\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Apply Database Migrations
```powershell
python manage.py migrate
```

### 3. Start Development Server
```powershell
python manage.py runserver
```
Server runs at `http://127.0.0.1:8000/`.

---

## 📖 API Documentation & Endpoints

| Method | Endpoint | Description | Query Parameters |
|:---|:---|:---|:---|
| **GET** | `/api/docs/` | **Interactive Swagger UI** | — |
| **GET** | `/api/redoc/` | **ReDoc Documentation** | — |
| **GET** | `/api/schema/` | **OpenAPI 3.0 Schema** | — |
| **GET** | `/api/tasks/` | List paginated tasks | `?status=`, `?priority=`, `?search=`, `?ordering=`, `?page=` |
| **POST** | `/api/tasks/` | Create a new task | JSON body |
| **GET** | `/api/tasks/{id}/` | Retrieve task by ID | — |
| **PUT** | `/api/tasks/{id}/` | Full task update | JSON body |
| **PATCH** | `/api/tasks/{id}/` | Partial task update | JSON body |
| **DELETE** | `/api/tasks/{id}/` | Delete task | — |

---

## 🔐 Admin Dashboard
- **URL**: `http://127.0.0.1:8000/admin/`
- **Username**: `admin`
- **Password**: `admin123`
