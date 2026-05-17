import pytest
from app import create_app, db
from app.models.user import User
from app.models.donation import Donation

@pytest.fixture
def app():
    app = create_app("development")
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_user_password_hashing(app):
    with app.app_context():
        user = User(name="Test User", email="test@example.com")
        user.set_password("securepassword")
        assert user.check_password("securepassword") is True
        assert user.check_password("wrongpassword") is False

def test_donation_creation(app):
    with app.app_context():
        donation = Donation(amount=200.0, status="completed")
        db.session.add(donation)
        db.session.commit()
        assert donation.id is not None
        assert donation.currency == "ZAR"