from flask_mail import Message
from app import mail

def send_donation_confirmation(donor_email, donor_name, amount):
    msg = Message(
        subject="Thank you for your donation – Golden Ark Care Centre",
        recipients=[donor_email],
        body=f"""Dear {donor_name},

Thank you for your generous donation of R{amount:.2f}.
Your contribution goes directly to supporting the children in our care.

With gratitude,
Golden Ark Care Centre
"""
    )
    mail.send(msg)