import csv
import io
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from app.extensions import db
from app.models.transaction import Transaction

main_bp = Blueprint("main", __name__)

@main_bp.get("/")
def index():
    transactions = Transaction.query.order_by(Transaction.created_at.desc()).all()
    income = sum(t.amount for t in transactions if t.kind == "income")
    expense = sum(t.amount for t in transactions if t.kind == "expense")
    return render_template("index.html", transactions=transactions, income=income, expense=expense)

@main_bp.post("/add")
def add():
    title = request.form.get("title", "").strip()
    amount = request.form.get("amount", type=float)
    category = request.form.get("category", "Other")
    kind = request.form.get("kind", "expense")
    note = request.form.get("note", "").strip()

    if not title or not amount or amount <= 0:
        flash("Enter a valid title and positive amount.", "danger")
        return redirect(url_for("main.index"))

    db.session.add(Transaction(
        title=title, amount=amount, category=category,
        kind=kind, note=note
    ))
    db.session.commit()
    flash("Transaction added.", "success")
    return redirect(url_for("main.index"))

@main_bp.post("/delete/<int:transaction_id>")
def delete(transaction_id):
    item = db.get_or_404(Transaction, transaction_id)
    db.session.delete(item)
    db.session.commit()
    flash("Transaction deleted.", "info")
    return redirect(url_for("main.index"))

@main_bp.get("/export")
def export():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Title", "Amount", "Category", "Type", "Note", "Created"])
    for t in Transaction.query.order_by(Transaction.created_at.desc()):
        writer.writerow([t.id, t.title, t.amount, t.category, t.kind, t.note, t.created_at])
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=transactions.csv"}
    )
