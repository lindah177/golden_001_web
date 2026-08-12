import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


# PUBLIC ROUTES
def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200

def test_donate_page_loads(client):
    response = client.get("/donate")
    assert response.status_code == 200

def test_contact_page_loads(client):
    response = client.get("/contact")
    assert response.status_code == 200

def test_login_page_loads(client):
    response = client.get("/auth/login")
    assert response.status_code == 200


# CONTACT FORM SUBMISSION
def test_contact_form_submission(client):
    response = client.post("/contact", data={
        "name": "Lerato Khumalo",
        "email": "lerato@example.com",
        "enquiry_type": "I want to volunteer",
        "message": "I want to help with tutoring."
    }, follow_redirects=True)
    assert response.status_code == 200

def test_contact_form_missing_fields(client):
    response = client.post("/contact", data={
        "name": "",
        "email": "",
        "message": ""
    }, follow_redirects=True)
    assert response.status_code == 200


# ADMIN PROTECTION
def test_admin_dashboard_requires_login(client):
    response = client.get("/admin/dashboard", follow_redirects=True)
    # Should redirect to login page
    assert response.status_code == 200
    assert b"Login" in response.data

def test_login_with_wrong_credentials(client):
    response = client.post("/auth/login", data={
        "email": "wrong@example.com",
        "password": "wrongpassword"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid" in response.data


# ADMIN LOGIN
def test_admin_login_success(app, client):
    with app.app_context():
        admin = User(name="Admin", email="admin@test.com", is_admin=True)
        admin.set_password("adminpass123")
        db.session.add(admin)
        db.session.commit()

    response = client.post("/auth/login", data={
        "email": "admin@test.com",
        "password": "adminpass123"
    }, follow_redirects=True)
    assert response.status_code == 200