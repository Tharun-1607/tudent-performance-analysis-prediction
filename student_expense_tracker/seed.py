from app import create_app
from app.extensions import db
from app.models.transaction import Transaction

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    samples = [
        Transaction(title="College bus", amount=120, category="Travel", kind="expense"),
        Transaction(title="Lunch", amount=80, category="Food", kind="expense"),
        Transaction(title="Part-time work", amount=5000, category="Income", kind="income"),
    ]
    db.session.add_all(samples)
    db.session.commit()
    print("Database seeded.")
