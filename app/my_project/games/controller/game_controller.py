from flask import request, jsonify
from app.my_project.games.service.game_service import GameService

service = GameService()

class GameController:
    def get_all_games(self):
        return jsonify(service.get_all())

    def create_game(self):
        service.create(request.json)
        return jsonify({"message": "Game created"}), 201

    def get_game_details(self, game_id):
        game = service.get_details(game_id)
        if game:
            return jsonify(game)
        return jsonify({"error": "Not found"}), 404