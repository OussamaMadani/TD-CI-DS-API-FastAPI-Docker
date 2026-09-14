def test_application_imports():
    from app.main import app

    assert app.title == "FastAPI"
