from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.models.contact import ContactMessage
from app.models.donation import Donation

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def index():
    total_donations = db.session.query(db.func.sum(Donation.amount)).filter_by(status="completed").scalar() or 0
    return render_template("public/index.html", total_donations=total_donations)

@public_bp.route("/donate")
def donate():
    return render_template("public/donate.html")

@public_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        enquiry_type = request.form.get("enquiry_type", "General enquiry")
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("public.contact"))

        msg = ContactMessage(name=name, email=email, enquiry_type=enquiry_type, message=message)
        db.session.add(msg)
        db.session.commit()
        flash("Thank you! We will get back to you soon.", "success")
        return redirect(url_for("public.index"))

    return render_template("public/contact.html")