from app import db
from app.models.donation import Donation

def create_donation(amount, message="", is_anonymous=False, donor_id=None):
    donation = Donation(
        amount=amount,
        message=message,
        is_anonymous=is_anonymous,
        donor_id=donor_id,
        status="pending"
    )
    db.session.add(donation)
    db.session.commit()
    return donation

def get_total_donations():
    total = db.session.query(db.func.sum(Donation.amount)).filter_by(status="completed").scalar()
    return total or 0.0