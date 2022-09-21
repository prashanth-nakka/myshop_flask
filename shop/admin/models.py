from shop import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile_pic = db.Column(
        db.String(180), unique=False, nullable=False, default="profile.jpg"
    )

    def __repr__(self) -> str:
        return f"User >>> {self.username}"

db.create_all()