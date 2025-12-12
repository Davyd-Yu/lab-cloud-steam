from app.my_project.games.dao.game_dao import GameDAO

class GameService:
    def __init__(self):
        self.dao = GameDAO()

    def get_all(self):
        return [game.to_dict() for game in self.dao.get_all_games()]

    def create(self, data):
        self.dao.create_game(data['title'], data['price'])