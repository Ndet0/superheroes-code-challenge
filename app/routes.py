from flask import Blueprint, jsonify
from app import db
from app.models import Hero, Power, HeroPower

api = Blueprint("api", __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=("id", "name", "super_name")) for hero in heroes]), 200
