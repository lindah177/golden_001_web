from flask import Blueprint, request, jsonify
from app import csrf
from app.services.donation_service import create_donation

donations_bp = Blueprint("donations", __name__)

@donations_bp.route("/create", methods=["POST"])
@csrf.exempt  # Exempt this route from CSRF protection for API usage
def donate():
    data = request.get_json()
    amount = data.get("amount")

    if not amount or float(amount) <= 0:
        return jsonify({"success": False, "error": "Invalid amount"}), 400

    donation = create_donation(amount=float(amount), message=data.get("message", ""))

    return jsonify({
        "success": True,
        "donation_id": donation.id,
        "message": f"Thank you for your R{float(amount):.2f} donation!"
    }), 201