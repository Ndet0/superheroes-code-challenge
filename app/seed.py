from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
    ]

    powers = [
        Power(
            name="super strength",
            description="gives the wielder super-human strength"
        ),
        Power(
            name="flight",
            description="gives the wielder the ability to fly"
        ),
        Power(
            name="elasticity",
            description="can stretch the body to extreme lengths"
        ),
    ]

    db.session.add_all(heroes + powers)
    db.session.commit()

    hero_powers = [
        HeroPower(hero_id=1, power_id=2, strength="Strong"),
        HeroPower(hero_id=3, power_id=1, strength="Average"),
    ]

    db.session.add_all(hero_powers)
    db.session.commit()

    print("✅ Done seeding!")
