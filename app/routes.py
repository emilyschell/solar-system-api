from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, name, id, description, moons):
        self.name = name
        self.id = id
        self.description = description
        self.moons = moons

    def to_json(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "moons": self.moons
            }

planets = [
    Planet("Mercury", 1,
           "Looks gray, so gray. A year is just 88 days long. Smallest planet.", 0),
    Planet("Venus", 2, "Kindof ivory? A day is longer than a year.", 0),
    Planet("Earth", 3, "Moist and oxygenated. Overrun with life.", 1)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message" :f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    return abort(make_response({"message" :f"planet {planet_id} not found"}, 404))


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    response = []
    for planet in planets:
        response.append(planet.to_json())
    return jsonify(response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate(planet_id)
    return jsonify(planet.to_json(),200)

