# Inventory Management System

a simple inventory management system built with Django and Django Rest Framework.

## Features
1. Inventory List & Detail Views
2. Django Admin Panel
3. REST API with Filtering
4. Unit Tests for Views & API  

---

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/Musyrif00/Inventory-Management.git
cd inventory_project 
```

### Create & Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # if on Windows: venv\Scripts\activate
```

### Install Rquired Dependencies
```sh
pip install -r requirements.txt
```
### Migrate
```sh
python manage.py migrate
```

### Create Superuser for login
```sh
python manage.py createsuperuser
```

### Run server
```sh
python manage.py runserver
```

### Access the APP
* Inventory List: http://127.0.0.1:8000/inventory/
* Admin Panel: http://127.0.0.1:8000/admin/
* API Endpoint: http://127.0.0.1:8000/api/inventory/

### Running Tests
```sh
python manage.py test inventory
```