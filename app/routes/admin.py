from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from app import db
from app.models.donation import Donation
from app.models.child import Child
from app.models.contact import ContactMessage

admin_bp = Blueprint("admin", __name__)

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated

@admin_bp.route("/dashboard", methods=["GET"])
@login_required
@admin_required
def dashboard():
    total_donations = db.session.query(db.func.sum(Donation.amount)).filter_by(status="completed").scalar() or 0
    child_count = Child.query.filter_by(is_active=True).count()
    unread_messages = ContactMessage.query.filter_by(is_read=False).count()
    recent_donations = Donation.query.order_by(Donation.created_at.desc()).limit(5).all()

    return render_template("admin/dashboard.html",
        total_donations=total_donations,
        child_count=child_count,
        unread_messages=unread_messages,
        recent_donations=recent_donations
    )