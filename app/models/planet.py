from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_count = db.Column(db.Integer)
    moons = db.relationship("Moon", back_populates="planet")

    def to_json(self):
        planet_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moon_count": self.moon_count
        }

        if self.moons:
            planet_dict["moons"] = self.moons

        return planet_dict

    def update(self, request_body):
        self.name = request_body["name"]
        self.description = request_body["description"]
        self.moon_count = request_body["moon_count"]

        if "moon_data" in request_body:
            self.moon_data = request_body["moon_data"]

    @classmethod
    def create(cls, request_body):
        new_planet = cls(
            name=request_body['name'],
            description=request_body['description'],
            moon_count=request_body['moon_count']
        )

        return new_planet
