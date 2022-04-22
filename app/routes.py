from flask import Blueprint, jsonify


class Planet:
    def __init__(self, name, id, description, moons):
        self.name = name
        self.id = id
        self.description = description
        self.moons = moons


planets = [
    Planet("Mercury", 1,
           "Looks gray, so gray. A year is just 88 days long. Smallest planet.", 0),
    Planet("Venus", 2, "Kindof ivory? A day is longer than a year.", 0),
    Planet("Earth", 3, "Moist and oxygenated. Overrun with life.", 1)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    response = []
    for planet in planets:
        response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })
    return jsonify(response)
