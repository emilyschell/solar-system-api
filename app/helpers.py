from flask import abort, make_response
from app.models.planet import Planet


def validate(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        return abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet
