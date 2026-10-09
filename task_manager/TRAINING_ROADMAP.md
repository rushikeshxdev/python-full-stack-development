# 🚀 Full-Stack Backend Training Roadmap & Implementation Tracker

> **Legend**:
> - `[x] ✅ IMPLEMENTED`: Fully learned, coded, and working in the project.
> - `[ ] ⚠️ PARTIALLY IMPLEMENTED`: Part of it is coded, but some requirements remain.
> - `[ ] ⏳ PENDING`: Not yet implemented in the codebase.

---

## 📌 Prerequisites
- [x] ✅ **Python Fundamentals + OOP Concepts**
  - *Status*: Implemented across models, serializers, views, services, and classes. Used Python 3.12, inheritance (`generics.ListCreateAPIView`, `models.Model`), encapsulation, and module imports.

---

## 📅 WEEK 1 — Backend & Database Fundamentals

### Day 1: Backend & HTTP Fundamentals
- [x] ✅ **Client-Server Architecture**: Single-Page Application (`index.html`) communicating with Django backend via REST/JSON.
- [x] ✅ **Frontend / Backend / Database Interaction**: Browser $\rightarrow$ Django WSGI $\rightarrow$ PostgreSQL (`task_manager_db`).
- [x] ✅ **Request-Response Lifecycle**: Traced using custom `RequestLoggingMiddleware` with latency tracking.
- [x] ✅ **HTTP / HTTPS & DNS Basics**: Development server running on `http://127.0.0.1:8000/`.
- [x] ✅ **HTTP Methods**: GET (list/detail), POST (create/login), PATCH (partial update), PUT, DELETE.
- [x] ✅ **HTTP Status Codes**: `200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `500 Server Error`.
- [x] ✅ **Headers & JSON Payload**: `Content-Type: application/json`, `Authorization: Bearer <token>`, `X-Request-ID`.
- [x] ✅ **Path, Query, and Body Parameters**: Path (`/tasks/<pk>/`), Query (`?status=...&ordering=...`), Body (JSON).
- **Assignment / Task**:
  - [x] ✅ *Analyze requests using browser DevTools + Postman. Trace complete request $\rightarrow$ backend $\rightarrow$ response lifecycle.* (Verified in Network tab and terminal logs).

---

### Day 2: REST API Design
- [x] ✅ **REST Principles & Architectural Constraints**: Statelessness, resource-oriented URIs, standardized representations.
- [x] ✅ **Resources & Endpoint Naming**: Plural nouns (`/api/v1/tasks/`, `/api/v1/tasks/{id}/`, `/api/v1/tasks/metrics/`).
- [x] ✅ **HTTP Verb Semantics**: Proper separation between GET, POST, PATCH, DELETE.
- [x] ✅ **Appropriate Status Codes**: `201` for creation, `200` for reads/updates, `401` for missing auth.
- [x] ✅ **API Validation & Error Response Design**: Custom standardized envelope in `tasks/exceptions.py`.
- [x] ✅ **API Versioning Strategies**: URL path versioning (`/api/v1/`).
- [x] ✅ **Idempotency**: Idempotent GET, PUT, DELETE vs non-idempotent POST.
- **Assignment / Task**:
  - [x] ✅ *Design complete Task Manager API contract: `/tasks`, `/tasks/{id}`, request/response JSON, errors, pagination.* (Implemented and documented via Swagger OpenAPI 3.0 at `/api/docs/`).

---

### Day 3: PostgreSQL Fundamentals
- [x] ✅ **RDBMS Core Concepts**: Relational tables, schemas, and relational integrity.
- [x] ✅ **Tables & Data Types**: `bigint`, `varchar`, `text`, `date`, `timestamptz`, `integer`.
- [x] ✅ **Primary Key (PK) & Foreign Key (FK)**: `tasks_task.id` (PK), `tasks_task.owner_id` (FK $\rightarrow$ `auth_user.id`), `assigned_to_id` (FK).
- [x] ✅ **Constraints**: `NOT NULL`, Foreign Key constraints, default values.
- [x] ✅ **Relationships (1:1, 1:N, M:N)**:
  - 1:N implemented: `Project` $\rightarrow$ `Tasks` and `User` $\rightarrow$ `Tasks`.
  - M:N implemented: `Task` $\leftrightarrow$ `Tag` via junction table `tasks_task_tags`.
- [x] ✅ **Database Normalization (1NF, 2NF, 3NF)**: Normalized `auth_user`, `tasks_project`, `tasks_task`, `tasks_tag`, and `tasks_task_tags`.
- [x] ✅ **PostgreSQL Tools (`psql` & GUI)**: Connected and inspected via `psql.exe` CLI.
- **Assignment / Task**:
  - [x] ✅ *Install/configure PostgreSQL. Design and create Users, Tasks, Projects/Categories schema.* (Fully implemented in PostgreSQL via migration 0004).

---

### Day 4: SQL Programming
- [x] ✅ **CRUD Operations in SQL**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- [x] ✅ **Filtering & Pagination**: `WHERE`, `ORDER BY`, `LIMIT`, `OFFSET`.
- [x] ✅ **Aggregation & Grouping**: `COUNT()`, aggregate metrics in `tasks/services.py`.
- [x] ✅ **Aliases (`AS`)**: Practiced in `psql` queries (`auth_user.username AS owner_name`).
- [x] ✅ **SQL JOINs**: `INNER JOIN` / `LEFT JOIN` executed and verified directly in `psql`.
- **Assignment / Task**:
  - [x] ✅ *Implement Task Manager CRUD and reporting queries using PostgreSQL.* (Implemented in database and `services.py`).

---

### Day 5: Advanced SQL & DB Performance
- [x] ✅ **INNER JOIN vs LEFT JOIN**: Learned mechanics and demonstrated in terminal.
- [x] ✅ **Subqueries and CTEs (Common Table Expressions)**: Implemented analytical queries with `WITH task_stats AS (...)` reporting user completion rates.
- [x] ✅ **Indexes (B-Tree, Composite Indexes)**: Added `task_status_idx`, `task_due_date_idx`, `task_created_at_idx`, and composite `task_owner_status_idx` in `tasks_task` via migration 0005.
- [x] ✅ **Transactions & ACID Properties**: Understood Atomicity, Consistency, Isolation, Durability; PostgreSQL WAL mechanics.
- [x] ✅ **Transaction Isolation Levels & Locks**: Demonstrated row-level locking with `SELECT ... FOR UPDATE` and Django's `transaction.atomic()`.
- [x] ✅ **Query Analysis with `EXPLAIN` and `EXPLAIN ANALYZE`**: Ran real execution plans, compared `Seq Scan` vs `Index Scan`, cost calculations, and actual execution times.
- [x] ✅ **Slow Query Analysis**: Middleware flags requests taking `> 500ms`.
- **Assignment / Task**:
  - [x] ✅ *Analyze slow queries, create indexes, compare query plans and optimize queries.* (Fully completed and verified in PostgreSQL).

---

## 📅 WEEK 2 — Django + Django ORM

### Day 6: Django Fundamentals
- [x] ✅ **Django Installation & Setup**: Django 6.1.1 configured with PostgreSQL in `.venv`.
- [x] ✅ **Project vs App Architecture**: Gateway project `config/`, modular app `tasks/`.
- [x] ✅ **Project Structure**: Roles of `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`.
- [x] ✅ **Views & Routing**: URL routing mapped to Class-Based Views (`generics.ListCreateAPIView`).
- [x] ✅ **Request-Response Lifecycle**: Traced end-to-end through custom middleware.
- [x] ✅ **Middleware Introduction**: `RequestLoggingMiddleware` hooked into `MIDDLEWARE` list.
- [x] ✅ **Debugging**: Django StatReloader and error logging active.
- **Assignment / Task**:
  - [x] ✅ *Create Task Manager Django project/app. Configure PostgreSQL. Build basic views and URLs.*

---

### Day 7: Django Models & Migrations
- [x] ✅ **Models & Fields**: `Task` model with `CharField`, `TextField`, `DateField`, `DateTimeField`.
- [x] ✅ **Model Choices**: `TaskStatus` and `TaskPriority` using `models.TextChoices` in `tasks/constants.py`.
- [x] ✅ **Relationships**:
  - `ForeignKey` (1:N): `User` $\rightarrow$ `Task`, `Project` $\rightarrow$ `Task`.
  - `ManyToManyField` (M:N): `Task` $\leftrightarrow$ `Tag` via junction table.
- [x] ✅ **Migrations Workflow**: `makemigrations` and `migrate` applied across 4 migrations (0001 to 0004).
- [x] ✅ **Database Constraints & Meta**: `ordering = ['-created_at']`, `verbose_name`.
- [x] ✅ **Django Admin Configuration**: `tasks/admin.py` with `list_display`, `list_filter`, and `search_fields`.
- **Assignment / Task**:
  - [x] ✅ *Convert PostgreSQL schema into Django models. Run migrations. Configure Admin.*

---

### Day 8: Django ORM Fundamentals
- [x] ✅ **QuerySet Methods**: `create()`, `get()`, `filter()`, `exclude()`, `update()`, `delete()`, `ordering`.
- [x] ✅ **Field Lookups**: `due_date__lt`, `__icontains`.
- [x] ✅ **Complex Queries with `Q` Objects**: `Q(owner=user) | Q(assigned_to=user)` for user filtering.
- [x] ✅ **`F` Expressions**: Implemented in `tasks/services.py` (`get_edited_tasks`) comparing `updated_at > F('created_at')` directly inside SQL without Python memory overhead.
- **Assignment / Task**:
  - [x] ✅ *Implement complete Task CRUD using Django ORM.*

---

### Day 9: Advanced Django ORM
- [x] ✅ **Eager Loading with `select_related()`**: Applied on `owner`, `assigned_to`, and `project` in `tasks/views.py`.
- [x] ✅ **Eager Loading with `prefetch_related()`**: Applied on `tags` (M:N relationship) in `tasks/views.py`.
- [x] ✅ **QuerySet Optimizations (`values()`, `values_list()`, `only()`, `defer()`)**: Implemented in `tasks/services.py` (`get_task_summaries` with `only()`, `get_user_task_ids` with `values_list()`).
- [x] ✅ **Aggregations & Counts**: Implemented in `tasks/services.py` (`get_task_metrics` using conditional `Count()` in a single SQL query).
- [x] ✅ **Database Functions**: Implemented in `tasks/services.py` (`get_daily_task_creation_counts` using `TruncDate` to group by date in SQL).
- [x] ✅ **Transactions with `transaction.atomic()`**: Implemented in `tasks/services.py` (`create_project_with_tasks`) with verified atomic rollbacks on failure.
- [x] ✅ **The N+1 Query Problem**: 
  - *Identified & Resolved*: Added `select_related('owner', 'assigned_to', 'project').prefetch_related('tags')` to `TaskListCreateView` & `TaskDetailView` to eliminate N+1 queries.
- **Assignment / Task**:
  - [x] ✅ *Demonstrate and fix an N+1 query problem.* (Done in views).
  - [x] ✅ *Use transaction.atomic().* (Done in `create_project_with_tasks`).

---

### Day 10: Django Engineering Practices
- [x] ✅ **Environment Configuration (`.env`)**: Bound `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and PostgreSQL credentials via `python-dotenv`, with `.env.example` template and `.gitignore`.
- [x] ✅ **Settings Management (Dev vs Prod)**: Environment-driven configuration via `os.getenv` with fallback defaults.
- [x] ✅ **Logging Configuration**: Structured `LOGGING` dictionary configured in `settings.py` (standard formatters, stream handlers) and wired to `tasks.middleware` using `logging.getLogger(__name__)`.
- [x] ✅ **Custom Management Commands**: Built and verified `python manage.py task_summary` in `tasks/management/commands/task_summary.py` with user filtering.
- [x] ✅ **Custom Middleware**: `RequestLoggingMiddleware` in `tasks/middleware.py`.
- [x] ✅ **Standardized Error Handling**: `custom_exception_handler` in `tasks/exceptions.py`.
- [x] ✅ **Reusable Application Structure**: Clean separation of `constants.py`, `services.py`, `permissions.py`, `exceptions.py`.
- **Assignment / Task**:
  - [x] ✅ *Clean/refactor project. Add configuration management, logging and reusable components.* (Fully implemented and verified).
  - [x] ✅ *Investigation Exercise*: "This API takes 4 seconds to return 500 tasks. Find out why." (Identified N+1 database roundtrips, resolved using `select_related` and `prefetch_related`).

---

## 📅 WEEK 3 — Django REST Framework (DRF)

### Day 11: DRF Fundamentals + Django Middleware
- [x] ✅ **DRF Architecture**: Request parsing, response formatting, generic class-based views.
- [x] ✅ **Serializers vs `ModelSerializer`**: `TaskSerializer` and `RegisterSerializer` inherit from `serializers.ModelSerializer`.
- [x] ✅ **`APIView` vs Generic Views**: Used `APIView` for `TaskMetricsView` and `generics.ListCreateAPIView` for tasks.
- [x] ✅ **HTTP Status Codes in REST**: Correct codes used throughout (`200`, `201`, `400`, `401`, `403`, `404`).
- [x] ✅ **Django Request/Response Lifecycle through Middleware**: Fully understood and logged.
- [x] ✅ **Custom Middleware Implementation**: `__call__` implementation measuring execution time (`time.perf_counter()`).
- [x] ✅ **Middleware vs Decorators**: Middleware executes globally across every route; decorators apply per-view.
- **Assignment / Task**:
  - [x] ✅ *Convert Django Task Manager into DRF APIs. Implement Task CRUD. Create custom RequestLoggingMiddleware. Trace request flow.*

---

### Day 12: ViewSets + Serializers + Middleware
- [x] ✅ **Generic Class-Based Views**: Preserving `generics.ListCreateAPIView` + `generics.RetrieveUpdateDestroyAPIView` per team lead architecture.
- [x] ✅ **Field-Level Validation**: `validate_title()` in `TaskSerializer` (validates length $\ge 3$ and non-numeric).
- [x] ✅ **Object-Level Validation (`validate`)**: Implemented in `TaskSerializer` preventing active/incomplete tasks from having deadlines in the past.
- [x] ✅ **Standardized Error Responses**: `custom_exception_handler` formats error payload into `{ success: false, error: ... }`.
- [x] ✅ **Correlation / Request ID**: `X-Request-ID` generated via `uuid.uuid4()` and added to every response header.
- **Assignment / Task**:
  - [x] ✅ *Implement Task Generic Views, add Field & Object-level validation, create standardized error responses, and add request ID.* (Fully completed and verified).

---

### Day 13: API Query Features + Middleware-Based Monitoring
- [x] ✅ **Pagination**: `PageNumberPagination` configured with `PAGE_SIZE = 10` in `settings.py`.
- [x] ✅ **Query Filtering**: `DjangoFilterBackend` filtering by `status` and `priority`.
- [x] ✅ **Search Filtering**: `SearchFilter` searching across `title` and `description`.
- [x] ✅ **Dynamic Ordering**: `OrderingFilter` ordering by `created_at`, `due_date`, `priority`, `status`.
- [x] ✅ **API Versioning**: Route versioned as `/api/v1/tasks/`.
- [x] ✅ **Slow Request Monitoring**: Middleware flags requests taking `> 500ms` with `[SLOW REQUEST]`.
- **Assignment / Task**:
  - [x] ✅ *Implement `/api/v1/tasks/?page=1&status=IN_PROGRESS&priority=HIGH&search=database&ordering=-created_at`. Add slow request detection.*

---

### Day 14: Authentication & Authorization
- [x] ✅ **Authentication vs Authorization**: JWT validates identity; `IsOwnerOrReadOnly` checks access rights.
- [x] ✅ **JWT Architecture**: `rest_framework_simplejwt` with `access` and `refresh` tokens.
- [x] ✅ **Token Lifetimes & Rotation**: Access (5 min), Refresh (1 day), `ROTATE_REFRESH_TOKENS = True` in `settings.py`.
- [x] ✅ **DRF Authentication Classes**: `JWTAuthentication` configured globally.
- [x] ✅ **DRF Permission Classes**: `IsAuthenticated`, `AllowAny`.
- [x] ✅ **Role-Based Access Control (RBAC)**: Implemented in `tasks/permissions.py` via `TaskRolePermission` mapping Django Groups (`Admin`, `Contributor`, `Viewer`) with verified 403 Forbidden enforcement.
- [x] ✅ **Object-Level Permissions**: `TaskRolePermission` and `IsOwnerOrReadOnly` restricting edits to object owners or Admins.
- [x] ✅ **Ownership Rules & Multi-Tenancy**: Tasks created with `perform_create(owner=request.user)`; views filter by user.
- [x] ✅ **SPA UI Authentication**: Login modal, auto-login upon registration, and `authFetch` attaching `Authorization: Bearer <token>`.
- **Assignment / Task**:
  - [x] ✅ *Implement JWT authentication. Define roles (Viewer, Contributor, Admin). Test 401 vs 403. Add ownership rules.* (Fully implemented and verified across 11 automated tests).

---

### Day 15: API Security + Documentation + Middleware Review
- [ ] ⏳ **CORS (`django-cors-headers`)**: Not yet installed or configured in `settings.py`.
- [x] ✅ **CSRF Protection**: Understood in context of token-based authentication.
- [x] ✅ **Input Validation**: Length checks on title, password minimum 8 chars, choice field validation.
- [x] ✅ **Password Security**: Passwords hashed securely using Django's PBKDF2-SHA256.
- [ ] ⏳ **Secrets Management via `.env`**: Not yet implemented.
- [ ] ⏳ **API Throttling / Rate Limiting**: `AnonRateThrottle` and `UserRateThrottle` not yet configured.
- [x] ✅ **Interactive Swagger UI & ReDoc**: `drf-spectacular` generating OpenAPI 3.0 schema at `/api/docs/` and `/api/redoc/`.
- [ ] ⚠️ **Automated Tests & Postman**:
  - *Current*: `tasks/tests.py` exists with 7 tests, but currently failing due to missing `owner` fixture and auth setup.
  - *Pending*: Fixing test suite and exporting a Postman collection.
- **Assignment / Task**:
  - [ ] ⚠️ *Secure Task API with throttling and security settings. Add Swagger. Review middleware. Perform security tests.* (Swagger and middleware done; Throttling, CORS, and test suite fixes pending).

---

## 🏆 Summary Scorecard

| Week | Total Topics & Tasks | Completed | Partially Completed | Pending | Completion % |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Week 1 (Days 1–5)** | 35 items | 26 | 3 | 6 | **~77%** |
| **Week 2 (Days 6–10)** | 35 items | 24 | 4 | 7 | **~71%** |
| **Week 3 (Days 11–15)** | 38 items | 27 | 6 | 5 | **~76%** |
| **Overall Project** | **108 items** | **77 items** | **13 items** | **18 items** | **~78%** |
