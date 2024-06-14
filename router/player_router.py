from flask import request, jsonify, Blueprint
from controllers.players_controller import players

player_bp = Blueprint("players", __name__)

@player_bp.route("/players", methods=["GET"])
def get_players():
    result = players.get_players()
    return jsonify(result)

@player_bp.route("/player/<id>", methods=["GET"])
def get_player_by_id(id):
    players_instance = players()  
    result = players_instance.get_player_by_id(id)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Player not found"}), 404

@player_bp.route("/player", methods=["POST"])
def create_player():
    data = request.get_json()
    name = data["name"]
    role = data["role"]
    team = data["team"]
    appearances = data["appearances"]
    goals = data["goals"]
    yellow_cards = data["yellow_cards"]
    red_cards = data["red_cards"]
    mvps = data["red_cards"]
    goals_con = data["goals_con"]
    ratio = data["ratio"]
    result = players.create_player(name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio)
    return jsonify(result)

@player_bp.route("/player/<id>", methods=["PATCH"])
def update_player(id):
    data = request.get_json()
    name = data["name"]
    role = data["role"]
    team = data["team"]
    appearances = data["appearances"]
    goals = data["goals"]
    yellow_cards = data["yellow_cards"]
    red_cards = data["red_cards"]
    mvps = data["red_cards"]
    goals_con = data["goals_con"]
    ratio = data["ratio"]
    result = players.update_player(id, name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio)
    return jsonify(result)

@player_bp.route("/player/<id>", methods=["DELETE"])
def delete_player(id):
    result = players.delete_player(id)
    return jsonify(result)
