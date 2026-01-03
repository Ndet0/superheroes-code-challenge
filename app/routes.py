from flask import Blueprint, jsonify, request
from app import db
from app.models import Hero, Power, HeroPower


api = Blueprint("api", __name__)
