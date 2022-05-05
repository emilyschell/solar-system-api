import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    planet_ny = Planet(name="New York",
                       description="ny 4evr",
                       moons=2)
    planet_rocky = Planet(name="Rocky McPlanet",
                          description="i luv 2 climb rocks",
                          moons=0)

    db.session.add_all([planet_ny, planet_rocky])
    db.session.commit()
