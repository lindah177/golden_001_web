from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    # Check if admin already exists
    existing = User.query.filter_by(email="admin@goldenarkcare.org.za").first()

    if existing:
        print("Admin user already exists.")
    else:
        admin = User(
            name="Admin",
            email="admin@goldenarkcare.org.za",
            is_admin=True
        )
        admin.set_password("Admin@1234")
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
        print("Email:    admin@goldenarkcare.org.za")
        print("Password: Admin@1234")