from flask import request, jsonify
from app.my_project.games.service.game_service import GameService

service = GameService()

class GameController:
    def get_all_games(self):
        """
        Отримати список ігор
        ---
        tags:
          - Games
        responses:
          200:
            description: Повертає JSON зі списком ігор
        """
        return jsonify(service.get_all())

    def create_game(self):
        """
        Додати нову гру
        ---
        tags:
          - Games
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - title
                - price
              properties:
                title:
                  type: string
                  example: "Half-Life 3"
                price:
                  type: number
                  example: 59.99
        responses:
          201:
            description: Гру успішно створено
        """
        service.create(request.json)
        return jsonify({"message": "Game created"}), 201