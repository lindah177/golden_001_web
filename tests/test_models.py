import pytest
from app import create_app, db
from app.models.user import User
from app.models.donation import Donation
from app.models.child import Child
from app.models.contact import ContactMessage

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


# USER TESTS
def test_create_user(app):
    with app.app_context():
        user = User(name="Thandi Mokoena", email="thandi@example.com")
        user.set_password("securepass")
        db.session.add(user)
        db.session.commit()
        assert user.id is not None
        assert user.email == "thandi@example.com"
        assert user.is_admin is False

def test_password_hashing(app):
    with app.app_context():
        user = User(name="Test User", email="test@example.com")
        user.set_password("mypassword123")
        assert user.check_password("mypassword123") is True
        assert user.check_password("wrongpassword") is False

def test_admin_user(app):
    with app.app_context():
        admin = User(name="Admin", email="admin@example.com", is_admin=True)
        admin.set_password("adminpass")
        db.session.add(admin)
        db.session.commit()
        assert admin.is_admin is True


# DONATION TESTS
def test_create_donation(app):
    with app.app_context():
        donation = Donation(amount=200.0, status="completed")
        db.session.add(donation)
        db.session.commit()
        assert donation.id is not None
        assert donation.currency == "ZAR"
        assert donation.amount == 200.0

def test_donation_default_status(app):
    with app.app_context():
        donation = Donation(amount=50.0)
        db.session.add(donation)
        db.session.commit()
        assert donation.status == "pending"

def test_anonymous_donation(app):
    with app.app_context():
        donation = Donation(amount=500.0, is_anonymous=True)
        db.session.add(donation)
        db.session.commit()
        assert donation.is_anonymous is True
        assert donation.donor_id is None


# CHILD TESTS
def test_create_child(app):
    with app.app_context():
        from datetime import date
        child = Child(
            first_name="Amahle",
            last_name="Dlamini",
            date_of_birth=date(2015, 3, 12)
        )
        db.session.add(child)
        db.session.commit()
        assert child.id is not None
        assert child.full_name == "Amahle Dlamini"
        assert child.is_active is True


# CONTACT TESTS
def test_create_contact_message(app):
    with app.app_context():
        msg = ContactMessage(
            name="Sipho Ndlovu",
            email="sipho@example.com",
            enquiry_type="I want to volunteer",
            message="I would love to help out on weekends."
        )
        db.session.add(msg)
        db.session.commit()
        assert msg.id is not None
        assert msg.is_read is False