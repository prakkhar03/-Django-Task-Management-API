# Django Task Management API

A simple **Task Management API** built using **Django REST Framework (DRF)**. This API allows users to **create, read, update, and delete (CRUD)** tasks while implementing authentication using **JWT tokens**.

---

## 🚀 Features

✅ User authentication using JWT tokens
✅ Task CRUD operations
✅ Task ownership restriction
✅ Pagination & ordering
✅ Unit tests for API endpoints

---

## 📛 Installation

### 1️⃣ Clone the repository:
```sh
 git clone https://github.com/yourusername/task_project.git
 cd task_project
```

### 2️⃣ Create and activate a virtual environment:
```sh
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

### 4️⃣ Run migrations:
```sh
python manage.py migrate
```

### 5️⃣ Create a superuser:
```sh
python manage.py createsuperuser
```

### 6️⃣ Start the development server:
```sh
python manage.py runserver
```

---

## 🔑 Authentication

This API uses **JWT authentication**.

### Obtain Access Token:
```http
POST /api/token/
```
#### Request Body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
#### Response:
```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```
### Use Access Token for Authorization:
Include it in the `Authorization` header:
```http
Authorization: Bearer your_access_token
```
---

## 📌 API Endpoints

| Method | Endpoint            | Description                     |
|--------|---------------------|---------------------------------|
| POST   | `/api/token/`       | Get JWT tokens                 |
| POST   | `/api/token/refresh/` | Refresh access token          |
| GET    | `/api/tasks/`       | List all tasks (Auth required) |
| POST   | `/api/tasks/`       | Create a new task              |
| GET    | `/api/tasks/{id}/`  | Retrieve a specific task       |
| PUT    | `/api/tasks/{id}/`  | Update a task                  |
| DELETE | `/api/tasks/{id}/`  | Delete a task                  |

---

## 🧦 Running Tests

To ensure everything works correctly, run the tests:
```sh
python manage.py test tasks
```

---

## 🛠 Technologies Used

- **Django** & **Django REST Framework**
- **SQLite** (default database, can be switched to PostgreSQL/MySQL)
- **JWT authentication** with `djangorestframework-simplejwt`
- **Thunder Client/Postman** for API testing



