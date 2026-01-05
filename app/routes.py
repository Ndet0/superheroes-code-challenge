from flask import Blueprint, jsonify, request
from app import db
from app.models import Hero, Power, HeroPower

api = Blueprint("api", __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        hero.to_dict(only=("id", "name", "super_name"))
        for hero in heroes
    ]), 200



@api.route("/heroes/<int:id>", methods=["GET"])
def get_hero_by_id(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify(
        hero.to_dict(
            only=("id", "name", "super_name", "hero_powers"),
            rules=("-hero_powers.hero",)
        )
    ), 200


@api.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200


@api.route("/powers/<int:id>", methods=["GET"])
def get_power_by_id(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.to_dict()), 200



@api.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()

    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({
            "errors": ["validation errors"]
        }), 400

    power.description = description
    db.session.commit()

    return jsonify(power.to_dict()), 200



@api.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()

    try:
        hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )

        db.session.add(hero_power)
        db.session.commit()

        hero = Hero.query.get(data["hero_id"])

        return jsonify(
            hero.to_dict(
                only=("id", "name", "super_name", "hero_powers"),
                rules=("-hero_powers.hero",)
            )
        ), 201

    except Exception:
        return jsonify({
            "errors": ["validation errors"]
        }), 400
