from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.transaction import Transaction

api_bp = Blueprint("api", __name__)

@api_bp.get("/transactions")
def transactions():
    return jsonify([t.to_dict() for t in Transaction.query.order_by(Transaction.id.desc()).all()])

@api_bp.post("/transactions")
def create_transaction():
    data = request.get_json(silent=True) or {}
    required = ["title", "amount", "category", "kind"]
    if any(key not in data for key in required):
        return jsonify({"error": "Missing required fields"}), 400

    item = Transaction(
        title=data["title"],
        amount=float(data["amount"]),
        category=data["category"],
        kind=data["kind"],
        note=data.get("note", "")
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201
