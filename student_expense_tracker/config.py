import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///expense_tracker.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
