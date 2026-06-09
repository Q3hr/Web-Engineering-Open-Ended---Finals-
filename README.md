# 🎓 Digital Certificate Generator System

A Django-based web application developed for the **Web Engineering Lab (CYS-463L)**. This project allows users to create, manage, search, edit, delete, and generate digital certificates through a responsive web interface.

---

## 📌 Project Overview

The Digital Certificate Generator System is designed to simplify the management and generation of student certificates. The application follows Django's MVC (Model-View-Template) architecture and implements complete CRUD functionality with a user-friendly Bootstrap interface.

---

## ✨ Features

### Certificate Management

* Add Certificate Records
* View All Certificates
* Edit Certificate Details
* Delete Certificates
* Search Certificates by Student Name

### Certificate Generation

* Generate Professional Certificate View
* Print Certificate Option
* Authorized Signature Section
* Responsive Certificate Layout

### Technical Features

* Django Models
* Django Forms
* Django Templates
* Bootstrap 5 Responsive UI
* JavaScript Form Validation
* SQLite Database
* Full CRUD Operations

---

## 🛠 Technologies Used

* Python 3
* Django
* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* SQLite3
* Git & GitHub

---

## 📂 Project Structure

```text
DigitalCertificateGenerator/
│
├── DigitalCertificateGenerator/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── certificates/
│   ├── migrations/
│   ├── templates/
│   │   └── certificates/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── add_certificate.html
│   │       ├── certificate_list.html
│   │       ├── edit_certificate.html
│   │       ├── delete_certificate.html
│   │       └── certificate_view.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Q3hr/Web-Engineering-Open-Ended---Finals-.git
```

### Move into Project Directory

```bash
cd Web-Engineering-Open-Ended---Finals-
```

### Create Virtual Environment

```bash
python -m venv myworld
```

### Activate Virtual Environment

#### Windows

```bash
myworld\Scripts\activate
```

#### Linux/Mac

```bash
source myworld/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## 🚀 Application Pages

### Home Page

Provides navigation to all system functionalities.

### Add Certificate

Allows users to add a new certificate record.

### View Certificates

Displays all certificates in a responsive table.

### Search Certificates

Search certificates using student names.

### Edit Certificate

Update existing certificate information.

### Delete Certificate

Remove certificate records safely.

### Certificate View

Generate and print professional certificate layouts.

---

## 🗄 Database Model

### Certificate

| Field        | Type      |
| ------------ | --------- |
| student_name | CharField |
| course       | CharField |
| issue_date   | DateField |

---

## 🔒 Security Features

* CSRF Protection
* Django Form Validation
* JavaScript Client-Side Validation
* Secure ORM Queries

---

## 📷 Sample Functionalities

* Add New Certificate
* Search Certificate
* Generate Certificate
* Edit Certificate
* Delete Certificate
* Print Certificate

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Django Framework
* Database Design
* CRUD Operations
* Template Inheritance
* Bootstrap Integration
* Form Handling
* Git & GitHub Version Control
* Web Application Development

---

## 👨‍💻 Author

**Ibrar Ul Hassan Shami**

BS Cyber Security
University of Wah

GitHub: https://github.com/Q3hr

---

## 🙏 Acknowledgement

Special thanks to my respected instructor and supervisor Sir Qadeer Yaseen for their guidance, support, and valuable feedback throughout the development of this project.

---

## 📜 License

This project is developed for educational and academic purposes.
