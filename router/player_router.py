from flask import request, jsonify, Blueprint
from controllers.players_controller import players

player_bp = Blueprint("players", __name__)

@player_bp.route("/players", methods=["GET"])
def get_players():
    result = players.get_players()
    return jsonify(result)

@player_bp.route("/player", methods=["POST"])
def create_player():
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    goals = data["goals"]
    team = data["team"]
    result = players.create_player(name, age, goals, team)
    return jsonify(result)

@player_bp.route("/player/<id>", methods=["POST"])
def update_player(id):
    data = request.get_json()

    name = data["name"]
    age = data["age"]
    goals = data["goals"]
    team = data["team"]

    result = players.update_user(id, name, age, goals, team)
    return jsonify(result)

@player_bp.route("/player/<id>", methods=["DELETE"])
def delete_player(id):
    result = players.delete_player(id)
    return jsonify(result)