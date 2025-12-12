from flask import Blueprint
from app.my_project.games.controller.game_controller import GameController

games_bp = Blueprint('games', __name__)
controller = GameController()

@games_bp.route('/games', methods=['GET'])
def get_games():
    return controller.get_all_games()

@games_bp.route('/games', methods=['POST'])
def add_game():
    return controller.create_game()