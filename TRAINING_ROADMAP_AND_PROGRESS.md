# 🚀 Python Full Stack Development — Training Roadmap & Progress Tracker

> **Candidate:** Rushikesh Randive  
> **Repository:** [python-full-stack-development](https://github.com/rushikeshxdev/python-full-stack-development)  
> **Primary Application:** [`task_manager`](file:///d:/python-full-stack-development/task_manager)  
> **Last Synchronized:** October 08, 2026  

---

## 📊 Executive Progress Dashboard

| Training Phase | Status | Completed Highlights | Active / Upcoming Tasks |
| :--- | :---: | :--- | :--- |
| **Week 1: Python Fundamentals & OOP** | **100% Complete** | Virtual environment, Memory model, OOP, Custom Exceptions, JSON CLI persistence engine | Fully mastered & verified |
| **Week 2: Backend, HTTP, REST & SQL** | **90% Complete** | HTTP lifecycle, REST contract, PostgreSQL 17 setup, raw SQL (`INSERT`, `INNER/LEFT JOIN`, `GROUP BY`) | Advanced SQL profiling (`EXPLAIN`), B-Tree Indexes |
| **Week 3: Django & Django ORM** | **85% Complete** | Modular Monolith, Models & text choices, PostgreSQL migration, generic views, service layer | `select_related` N+1 benchmark, `Q`/`F` expressions, `.env` config |
| **Week 4: DRF, Architecture & Production** | **60% In Progress** | Custom Latency Middleware, `X-Request-ID`, Serializer validation, Standardized Error Handler, 7 automated tests | **Day 14 (JWT Auth & RBAC)**, Day 15 (Throttling & Security hardening) |

---

## 📅 Detailed Week-by-Week Syllabus & Best Practices

---

### 🟢 Week 1: Python Fundamentals & OOP
*Build a strong, defensive Python foundation required for backend systems.*

- [x] **Python Setup & Virtual Environments (`.venv`)**: Isolated execution sandbox; path isolation.
- [x] **Variables, Data Types & Memory Model**: Object references, `id()`, `is` vs `==`, mutability vs immutability.
- [x] **Control Flow & Truthiness**: Falsy values (`None`, `""`, `[]`), loops, `enumerate()`, `break` vs `continue`.
- [x] **Functions & Scope**: `LEGB` scope resolution, `return` vs `print()`, `*args` (tuples), and `**kwargs` (dictionaries).
- [x] **Collections & Time Complexity**: Lists, Tuples, Sets, Dictionaries; algorithmic performance ($O(1)$ hashing vs $O(N)$ linear scans).
- [x] **Comprehensions**: List & Dict comprehensions for inline filtering and mapping.
- [x] **Object-Oriented Programming (OOP)**: `class`, constructor `__init__`, `self` attribute binding, instance methods.
- [x] **Defensive Validation & Exception Handling**: Raising `ValueError`, custom exceptions inheriting from `Exception` (`class TaskNotFoundError(Exception): pass`), `try...except` blocks.
- [x] **File I/O & JSON Persistence**: Context manager `with open(...)`, serialization (`json.dump()`), deserialization (`json.load()`).
- [x] **Modules & Packages**: Decoupling code into distinct files (`task.py`, `storage.py`, `task_manager.py`, `main.py`).
- [x] **Mini-Projects Completed**: Todo list CLI, Student CRUD engine, JSON file Task Manager.

---

### 🟡 Week 2: Backend, HTTP, REST & Database Fundamentals
*Master client-server communication, API architecture, and relational database systems.*

#### Day 1 — Backend & HTTP Fundamentals
- [x] **Client-Server Architecture**: Frontend/backend/database interaction and request-response lifecycle.
- [x] **HTTP/HTTPS & Protocols**: DNS basics, HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- [x] **Status Code Semantics**: `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `404 Not Found`.
- [x] **Headers & Parameters**: `Content-Type: application/json`, query parameters, path variables, request body.
- [x] **Tracing**: Analyzed requests using browser DevTools & cURL, tracing client $\rightarrow$ backend $\rightarrow$ response.
- ⭐ **Senior Best Practice**: Enforced explicit idempotency awareness (`POST` non-idempotent vs `PUT`/`PATCH`/`DELETE` idempotent).

#### Day 2 — REST API Design
- [x] **REST Principles**: Resources/endpoints using plural nouns (`/tasks`, `/tasks/{id}`).
- [x] **API Contract**: Standardized pagination contract (`count`, `next`, `results`).
- [x] **API Documentation**: Interactive OpenAPI 3.0 & Swagger UI via `drf-spectacular` at `/api/docs/`.
- ⭐ **Senior Best Practice**: Strict HTTP method dispatching rejecting unauthorized actions with `405 Method Not Allowed`.

#### Day 3 — PostgreSQL Fundamentals
- [x] **RDBMS Core**: Relational architecture, table schemas, data types (`BIGINT`, `VARCHAR`, `TIMESTAMP WITH TIME ZONE`).
- [x] **Keys & Constraints**: Primary Keys (`PK`), Foreign Keys (`FK`), `NOT NULL`, `DEFAULT`.
- [x] **Relational Cardinality**: `1:1` (User Profile), `1:N` (Projects $\rightarrow$ Tasks), `M:N` (Tasks $\leftrightarrow$ Tags).
- [x] **PostgreSQL Setup**: Installed PostgreSQL 17 on Windows, configured service `postgresql-x64-17` on port 5432, created `task_manager_db` via `psql`.
- ⭐ **Senior Best Practice**: UTF-8 encoding verification and setting database user permissions.

#### Day 4 — SQL Programming
- [x] **DML Operations**: `SELECT`, `INSERT`, `UPDATE`, `DELETE` in raw PostgreSQL terminal.
- [x] **Filtering & Sorting**: `WHERE`, `ORDER BY`, `LIMIT`, `OFFSET`.
- [x] **Relational Queries**: `INNER JOIN` (matching rows) and `LEFT JOIN` (all left table rows regardless of matches).
- [x] **Aggregations & Grouping**: `COUNT(tasks.id)`, `GROUP BY projects.name`.
- ⭐ **Senior Best Practice**: Querying `information_schema.tables` and inspecting PostgreSQL data types with `\d`.

#### Day 5 — Advanced SQL & DB Performance
- [ ] **Transactions & ACID**: `BEGIN`, `COMMIT`, `ROLLBACK` for multi-step data safety.
- [ ] **Indexes**: B-Tree indexes (`CREATE INDEX ... ON ...`) on high-cardinality search fields.
- [ ] **Query Execution Plans**: Using `EXPLAIN` and `EXPLAIN ANALYZE` to diagnose Sequential Scans vs Index Scans.
- [ ] **Slow Query Analysis**: Identifying table lock bottlenecks and sorting costs in SQL.
- ⭐ **Senior Best Practice**: Partial indexes (`WHERE status != 'DONE'`) to save index storage in high-volume tables.

---

### 🔵 Week 3: Django + Django ORM
*Translate database concepts into high-performance Python ORM abstractions.*

#### Day 6 — Django Fundamentals
- [x] **Architecture**: Project vs App split (`config/` gateway vs `tasks/` domain).
- [x] **Settings & Routing**: Central configuration in `settings.py`, root URL routing in `urls.py`.
- [x] **Execution Interfaces**: WSGI (`wsgi.py`) vs ASGI (`asgi.py`) execution models.
- ⭐ **Senior Best Practice**: Modular Monolith directory conventions with snake_case naming.

#### Day 7 — Django Models & Migrations
- [x] **Model Design**: `Task` model with `CharField`, `TextField`, `DateField`, `DateTimeField`.
- [x] **Master Data Choices**: Subclassed `models.TextChoices` (`TaskStatus`, `TaskPriority`) in `constants.py`.
- [x] **PostgreSQL Migration**: Swapped SQLite for PostgreSQL in `settings.py`, generated and executed migrations.
- [x] **Django Admin**: Configured admin dashboard, created superuser account `rushi`.
- ⭐ **Senior Best Practice**: Clean migration squashing and zero dead SQLite artifacts.

#### Day 8 — Django ORM Fundamentals
- [x] **CRUD via ORM**: `objects.create()`, `objects.get()`, `objects.filter()`, `objects.all()`.
- [ ] **Advanced Lookups**: `__icontains`, `__in`, `__date`, `__gte`, `__lte`.
- [ ] **Complex Logic**: `Q` objects (`Q(status='TODO') | Q(priority='HIGH')`).
- [ ] **Race Condition Prevention**: `F` expressions for atomic database increments.
- ⭐ **Senior Best Practice**: Separation of concerns using a dedicated `services.py` layer.

#### Day 9 — Advanced Django ORM & Performance
- [ ] **The N+1 Query Problem**: Reproducing the classic loop query bottleneck ($1 + N$ queries).
- [ ] **The N+1 Fix**: Using `select_related()` (SQL `JOIN` for 1:N) and `prefetch_related()` (for M:N).
- [ ] **Efficient Projections**: `values()` and `values_list()` for low-overhead read queries.
- [ ] **Database Aggregations**: `.annotate(task_count=Count('tasks'))`.
- [ ] **Atomic Transactions**: Wrapping critical operations in `with transaction.atomic():`.
- ⭐ **Senior Best Practice**: Automated unit tests checking query count limits (`assertNumQueries`).

#### Day 10 — Django Engineering Practices & Performance Case Study
- [ ] **Environment Configuration**: Moving credentials to `.env` using `python-dotenv`.
- [ ] **Custom Management Command**: Building CLI tool `python manage.py export_tasks_json`.
- [ ] **Senior Case Study**: *"This API takes 4 seconds to return 500 tasks. Find out why: API $\rightarrow$ Django $\rightarrow$ ORM $\rightarrow$ SQL $\rightarrow$ PostgreSQL $\rightarrow$ Query Plan."*
- ⭐ **Senior Best Practice**: Production healthcheck endpoint (`/healthz`) pinging DB status.

---

### 🟣 Week 4: Django REST Framework, Architecture & Production Engineering
*Build secure, observable, enterprise-grade REST APIs.*

#### Day 11 — DRF Fundamentals + Django Middleware
- [x] **DRF Core**: Serializers, `ModelSerializer`, generic views, and HTTP status codes.
- [x] **Custom RequestLoggingMiddleware**:
  - Intercepts requests to log method, path, response status, and duration in ms.
  - Lifecycle: `start_time = time.perf_counter()`, executes view, calculates duration on return.
- [x] **Slow Query Threshold**: Flagging requests exceeding $500\text{ms}$ (`[SLOW REQUEST]`).
- ⭐ **Senior Best Practice**: End-to-end request tracing: Client $\rightarrow$ Middleware $\rightarrow$ URL $\rightarrow$ View $\rightarrow$ Serializer $\rightarrow$ ORM $\rightarrow$ Response $\rightarrow$ Middleware $\rightarrow$ Client.

#### Day 12 — ViewSets + Serializers + Middleware
- [x] **API Patterns**: Standardized generic views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`).
- [x] **Serializer Validation**:
  - Field-level validation: `validate_title(self, value)` checking min length $\ge 3$ and non-numeric rules.
  - Read-only protection: `read_only_fields = ['id', 'created_at', 'updated_at']`.
- [x] **Standardized Error Envelope** ([`tasks/exceptions.py`](file:///d:/python-full-stack-development/task_manager/tasks/exceptions.py)):
  - Custom exception handler intercepting `ValidationError`, `Http404`, returning `{success: false, error: {...}, request_id: "..."}`.
- [x] **Correlation ID Middleware**:
  - Injects `X-Request-ID` into every incoming request and outgoing response header.
- ⭐ **Senior Best Practice**: Correlation ID propagated into error payloads for 30-second Sentry/APM debugging.

#### Day 13 — API Query Features + Monitoring
- [x] **Filtering, Search & Ordering**:
  - `DjangoFilterBackend` for status and priority.
  - `SearchFilter` across title and description.
  - `OrderingFilter` for `created_at`, `due_date`, `priority`, `status`.
- [x] **API Versioning**: Route versioning `/api/v1/tasks/`.
- [x] **Pagination Contract**: `PageNumberPagination` with page size 10.
- ⭐ **Senior Best Practice**: Integration test suite in [`tasks/tests.py`](file:///d:/python-full-stack-development/task_manager/tasks/tests.py) validating all features in $<0.05\text{s}$.

#### Day 14 — Authentication & Authorization (CURRENT ACTIVE MILESTONE)
- [x] `djangorestframework-simplejwt` installed in environment.
- [ ] **JWT Configuration**: Register `JWTAuthentication` and token settings in `settings.py`.
- [ ] **Auth Endpoints**:
  - `POST /api/v1/auth/token/` (Login $\rightarrow$ returns `access` and `refresh` tokens).
  - `POST /api/v1/auth/token/refresh/` (New access token via refresh token).
- [ ] **Task Ownership**:
  - Add `created_by` / `owner` (`ForeignKey(User, ...)`).
  - Add `assigned_to` (`ForeignKey(User, null=True, ...)`).
  - Auto-assign `request.user` on task creation (`perform_create`).
- [ ] **Role-Based Access Control (RBAC)**:
  - `Viewer` $\rightarrow$ Read-only access (`GET`).
  - `Contributor` $\rightarrow$ Create and update own tasks.
  - `Admin` $\rightarrow$ Full management access across all resources.
- [ ] **Object-Level Permissions**: Custom `IsOwnerOrReadOnly` / `IsOwnerOrAdmin` permission class.
- [ ] **Security Verification**: Testing `401 Unauthorized` vs `403 Forbidden` response boundaries.
- ⭐ **Senior Best Practice**: Embedding custom claims (`role`, `email`) in JWT payload to prevent DB queries on every authenticated request.

#### Day 15 — API Security + Documentation + Middleware Review
- [ ] **CORS Configuration**: Install and configure `django-cors-headers` for frontend origins.
- [ ] **API Throttling & Rate Limiting**:
  - `AnonRateThrottle` (10 req/min for unauthenticated requests).
  - `UserRateThrottle` (60 req/min for authenticated requests).
- [ ] **Security HTTP Status Verification**: Verifying `400`, `401`, `403`, `404`, `405`, and `429 Too Many Requests`.
- [ ] **Swagger & Postman**: Export finalized OpenAPI 3.0 schema and Postman test collection.
- ⭐ **Senior Best Practice**: Automated security tests asserting throttling kicks in after burst limit.
