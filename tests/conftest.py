# # from app import app
from app import create_app
import pytest

# # @pytest.fixture
# # def test_app():
# #     """test application setup"""
# #     app.config["TESTING"] = True
# #     with app.app_context():
# #         yield app

# create_app = True

@pytest.fixture
def test_app():
    """Fixture to set up the test Flask application"""
    app = create_app("sqlite:///:memory:")  # Use an in-memory SQLite database for testing
    with app.app_context():
        yield app


