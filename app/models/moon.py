from app import db


class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Integer)
    description = db.Column(db.String)
    has_craters = db.Column(db.Boolean)
    planet_id = db.Column(
        db.Integer, db.ForeignKey('planet.id'), nullable=True)
    planet = db.relationship("Planet", back_populates="moons")

    def to_dict(self):
        return {
            "id": self.id,
            "size": self.size,
            "description": self.description,
            "has craters": self.has_craters,
            "planet_id": self.planet_id
        }

    @classmethod
    def create(cls, request_body, planet):
        new_moon = cls(
            description=request_body['description'],
            size=request_body['size'],
            has_craters=request_body['has_craters'],
            planet=planet
        )

        return new_moon
