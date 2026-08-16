import pytest
from app import create_app
from app.extensions import db

@pytest.fixture()
def client(tmp_path):
    app = create_app()
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///" + str(tmp_path / "test.db")
    )
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as client:
        yield client
