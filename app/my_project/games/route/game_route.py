from flask import Blueprint
from app.my_project.games.controller.game_controller import GameController

games_bp = Blueprint('games', __name__)
controller = GameController()

@games_bp.route('/games', methods=['GET'])
def get_games():
    """
    Отримати список ігор
    ---
    tags:
      - Games
    responses:
      200:
        description: Повертає JSON зі списком ігор
    """
    return controller.get_all_games()

@games_bp.route('/games', methods=['POST'])
def add_game():
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
    return controller.create_game()

@games_bp.route('/games/<int:game_id>/details', methods=['GET'])
def get_details(game_id):
    """
    Отримати деталі гри та категорії
    ---
    tags:
      - Games
    parameters:
      - name: game_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Детальна інформація про гру
      404:
        description: Гру не знайдено
    """
    return controller.get_game_details(game_id)