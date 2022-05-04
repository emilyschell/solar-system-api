from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moons": self.moons
        }

    def update(self, request_body):
        self.name = request_body["name"]
        self.description = request_body["description"]
        self.moons = request_body["moons"]

    @classmethod
    def create(cls, request_body):
        new_planet = cls(
            name=request_body['name'],
            description=request_body['description'],
            moons=request_body['moons']
        )

        return new_planet
