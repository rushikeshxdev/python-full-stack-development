# 📋 Task Manager REST API (`task_manager`)

A production-grade, enterprise-architected Task Management API built with **Django**, **Django REST Framework (DRF)**, and **drf-spectacular** (OpenAPI 3.0 & Swagger UI).

---

## 🌟 Key Architecture & Lead Best Practices

- **Master Data Pattern (`tasks/constants.py`)**: Centralized `TaskStatus` and `TaskPriority` using Django's `models.TextChoices` to guarantee data integrity across the system.
- **Service Layer (`tasks/services.py`)**: Reusable, decoupled business functions (`get_task_metrics`, `get_overdue_tasks`, `mark_task_as_done`) callable by Views, Celery workers, or CLI scripts.
- **Explicit Generic Views (`tasks/views.py`)**: Built with standard DRF `generics.ListCreateAPIView` and `generics.RetrieveUpdateDestroyAPIView` rather than opaque magic.
- **API Versioning (`/api/v1/`)**: Versioned routing ensuring non-breaking mobile & external client contracts.
- **Search, Filter & Sorting**: Multi-field querying via `DjangoFilterBackend`, keyword `SearchFilter`, and dynamic `OrderingFilter`.
- **Automated Test Suite (`tasks/tests.py`)**: Full coverage across CRUD, status patch, and service metric endpoints.

---

## 🏗️ Project Structure

```text
task_manager/
├── config/                  # Central Project Gateway
│   ├── settings.py          # Installed apps, DB engines, DRF config
│   ├── urls.py              # Root router including /api/v1/ and Swagger docs
│   ├── wsgi.py              # Synchronous WSGI server interface
│   └── asgi.py              # Asynchronous ASGI interface
├── tasks/                   # Tasks Feature Module
│   ├── constants.py         # Master Data choices (TaskStatus, TaskPriority)
│   ├── models.py            # Task data model referencing master constants
│   ├── serializers.py       # DRF ModelSerializer & field validation
│   ├── services.py          # Decoupled business logic & analytics functions
│   ├── views.py             # DRF Generic Views & Service APIView
│   ├── urls.py              # App-level URL routing
│   ├── admin.py             # Customized Django Admin panel
│   ├── tests.py             # Automated unit & integration tests
│   └── migrations/          # Version-controlled schema migrations
├── templates/
│   └── index.html           # Dark-theme SPA dashboard consuming /api/v1/
├── manage.py                # Django CLI management script
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## 🚀 Getting Started

### 1. Run Automated Tests
```powershell
python manage.py test
```

### 2. Apply Migrations
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
| **GET** | `/api/v1/tasks/` | List paginated tasks | `?status=`, `?priority=`, `?search=`, `?ordering=`, `?page=` |
| **POST** | `/api/v1/tasks/` | Create a new task | JSON body |
| **GET** | `/api/v1/tasks/{id}/` | Retrieve task by ID | — |
| **PUT** | `/api/v1/tasks/{id}/` | Full task update | JSON body |
| **PATCH** | `/api/v1/tasks/{id}/` | Partial task update | JSON body |
| **DELETE** | `/api/v1/tasks/{id}/` | Delete task | — |
| **GET** | `/api/v1/tasks/metrics/` | Real-time task statistics | — |

---

## 🔐 Admin Dashboard
- **URL**: `http://127.0.0.1:8000/admin/`
- **Username**: `admin`
- **Password**: `admin123`
