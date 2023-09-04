"""Flask app for Cupcakes"""
import os

from flask import Flask, redirect, render_template,flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"


# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.get("/api/cupcakes")
def show_cupcakes():
    """show data about all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:id>")
def show_cupcake(cupcake_id):
    """show data about single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """create cupcake with client's properties"""

    id = request.json["id"]
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"]

    new_cupcake = Cupcake(id=id, flavor=flavor, size=size,
                          rating=rating, image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return jsonify(cupcake=serialized)

