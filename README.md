 # ☀️ Golden Ark Care Centre

A full-stack web application built for **Golden Ark Care Centre**, a South African non-profit organisation (NPO) dedicated to nurturing and empowering vulnerable children.

The platform allows the public to learn about the organisation, make donations, and get in touch — while giving staff a secure admin dashboard to manage records.

---

##  Live Features

- Public-facing website with home, donate, and contact pages
- Interactive donation form with preset amounts (R50, R200, R500, R1000)
- Contact form that saves messages to the database
- Secure admin login with role-based access control
- Admin dashboard showing donation totals, children in care, and unread messages
- CSRF protection on all forms
- Email confirmation service for donations
- Mobile-responsive design using Bootstrap 5

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | Flask |
| Database | SQLite + SQLAlchemy ORM |
| Migrations | Flask-Migrate (Alembic) |
| Authentication | Flask-Login |
| Forms & Security | Flask-WTF (CSRF protection) |
| Email | Flask-Mail |
| Frontend | Bootstrap 5, HTML5, JavaScript |
| Testing | pytest |
| Security Scanning | Bandit |
| Version Control | Git + GitHub |

---

##  Project Structure

golden_001_web/
├── app/

│ ├── init.py # App factory — creates and configures Flask app

│ ├── models/

│ │ ├── user.py # User model with password hashing

│ │ ├── donation.py # Donation records

│ │ ├── child.py # Children in care

│ │ └── contact.py # Contact form messages

│ ├── routes/

│ │ ├── public.py # Home, donate, contact pages

│ │ ├── auth.py # Login and logout

│ │ ├── admin.py # Protected admin dashboard

│ │ └── donations.py # JSON API for processing donations

│ ├── services/

│ │ ├── donation_service.py # Donation business logic

│ │ └── email_service.py # Email notifications

│ ├── static/

│ │ ├── css/main.css # Custom styles (Bootstrap overrides)

│ │ └── js/

│ │ ├── main.js # Global JS (alerts, smooth scroll)

│ │ └── donate.js # Donation form interactivity

│ └── templates/

│ ├── base.html # Master layout (navbar, footer)

│ ├── auth/login.html

│ ├── admin/dashboard.html

│ └── public/

│ ├── index.html

│ ├── donate.html

│ └── contact.html

├── migrations/ # Flask-Migrate database migration files

├── tests/

│ ├── test_models.py # Unit tests for database models

│ ├── test_routes.py # Route and response tests

│ └── test_donations.py # Donation flow tests

├── config.py # App configuration (dev and production)

├── app.py # Entry point

├── requirements.txt # Python dependencies

├── .env.example # Environment variable template

└── .gitignore

---

##  Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/lindah177/golden_001_web.git
cd golden_001_web
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```

Open `.env` and fill in your values:

SECRET_KEY=your-strong-secret-key

DATABASE_URL=sqlite:///sunshine.db

MAIL_USERNAME=your-email@gmail.com

MAIL_PASSWORD=your-app-password

To generate a strong secret key:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Set up the database
```bash
export FLASK_APP=app.py
flask db upgrade
```

### 6. Run the app
```bash
python3 app.py
```

Visit `http://127.0.0.1:5000`

---

##  Running Tests

```bash
pytest
```

To see detailed output:
```bash
pytest -v
```

---

##  Security Scanning

```bash
bandit -r app/
```

---

##  Database Migrations

After changing any model, run:

```bash
flask db migrate -m "Describe what you changed"
flask db upgrade
```

---

##  Deployment Notes

For production deployment:

- Set `FLASK_ENV=production` in your environment
- Replace SQLite with PostgreSQL by updating `DATABASE_URL`
- Use **Gunicorn** as the WSGI server:
```bash
  pip install gunicorn
  gunicorn -w 4 app:app
```
- Set a strong `SECRET_KEY` — never use the default
- Enable HTTPS

---

##  Author

**Lindah**
Software Engineering Graduate — WeThinkCode_
Pivoting into cybersecurity while building full-stack experience.

- GitHub: [@lindah177](https://github.com/lindah177)

---

##  Licence

This project was built for educational and portfolio purposes.
Sunshine Children's Care Centre is a fictionalised organisation used for this project.