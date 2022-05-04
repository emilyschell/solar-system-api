from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app import db
from .helpers import validate


# class Planet:
#     def __init__(self, name, id, description, moons):
#         self.name = name
#         self.id = id
#         self.description = description
#         self.moons = moons

#     def to_json(self):
#         return {
#                 "id": self.id,
#                 "name": self.name,
#                 "description": self.description,
#                 "moons": self.moons
#             }

# planets = [
#     Planet("Mercury", 1,
#            "Looks gray, so gray. A year is just 88 days long. Smallest planet.", 0),
#     Planet("Venus", 2, "Kindof ivory? A day is longer than a year.", 0),
#     Planet("Earth", 3, "Moist and oxygenated. Overrun with life.", 1)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# POST ROUTES


@planets_bp.route("",  methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.create(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been succesfully created!", 201)

# GET ROUTES


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    moons_query = request.args.get("moons")
    description_query = request.args.get("description")

    if moons_query:
        planets = Planet.query.filter_by(moons=moons_query)
    elif description_query:
        planets = Planet.query.filter_by(description=description_query)
    else:
        planets = Planet.query.all()

    response = [planet.to_json() for planet in planets]

    return jsonify(response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate(planet_id)
    response = planet.to_json()
    return jsonify(response), 200

# PUT ROUTES


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet = validate(planet_id)
    request_body = request.get_json()

    planet.update(request_body)

    db.session.commit()

    return make_response({"message": f"planet {planet_id} succesfully updated"}, 200)

# DELETE ROUTES


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response({"message": f"planet {planet_id} succesfully deleted"}, 200)
