"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """creates instances of cupcakes"""
    __tablename__ = "cupcakes"

    def to_dict(self):
        """serialize to dict"""

        return {"id": self.id,
                "flavor": self.flavor,
                "size": self.size,
                "rating": self.rating,
                "image_url": self.image_url }

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    flavor = db.Column(
        db.String(50),
        nullable = False
    )

    size = db.Column(
        db.String(15),
        nullable = False
    )

    rating = db.Column(
        db.Integer,
        nullable = False
    )

    image_url = db.Column(
        db.Text,
        nullable = False,
        default = "https://tinyurl.com/demo-cupcake"
    )