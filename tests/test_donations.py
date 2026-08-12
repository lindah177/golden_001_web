import pytest
import json
from app import create_app, db
from app.models.donation import Donation

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


def test_donation_api_valid_amount(client):
    response = client.post("/donations/create",
        data=json.dumps({"amount": 200, "is_anonymous": True}),
        content_type="application/json"
    )
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data["success"] is True
    assert "200" in data["message"]

def test_donation_api_invalid_amount(client):
    response = client.post("/donations/create",
        data=json.dumps({"amount": -50}),
        content_type="application/json"
    )
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["success"] is False

def test_donation_api_zero_amount(client):
    response = client.post("/donations/create",
        data=json.dumps({"amount": 0}),
        content_type="application/json"
    )
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["success"] is False

def test_donation_saved_to_database(app, client):
    with app.app_context():
        client.post("/donations/create",
            data=json.dumps({"amount": 500, "is_anonymous": True}),
            content_type="application/json"
        )
        donation = Donation.query.first()
        assert donation is not None
        assert donation.amount == 500.0
        assert donation.status == "pending"

def test_donation_service_directly(app):
    with app.app_context():
        from app.services.donation_service import create_donation, get_total_donations
        create_donation(amount=100.0)
        create_donation(amount=200.0)
        donations = Donation.query.all()
        assert len(donations) == 2