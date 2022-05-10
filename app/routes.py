from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app.models.moon import Moon
from app import db
from .helpers import validate

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

# POST ROUTES


@planets_bp.route("",  methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.create(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} has been successfully created!"), 201)


@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate(planet_id)
    request_body = request.get_json()

    new_moon = Moon.create(request_body, planet)
    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"New moon {new_moon.id} successfully created for planet {planet.name}"), 200)

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


@moons_bp.route("", methods=["GET"])
def read_all_moons():

    moons = Moon.query.all()

    response = [moon.to_dict() for moon in moons]

    return jsonify(response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate(planet_id)
    response = planet.to_json()
    return jsonify(response), 200


@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def read_moon_by_planet(planet_id):
    planet = validate(planet_id)
    moons_response = [moon.to_dict() for moon in planet.moons]
    return jsonify(moons_response), 200

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
