from app.my_project.utils.db import get_db_connection
from app.my_project.games.domain.game import Game

class GameDAO:
    def get_all_games(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM games")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Game(row['id'], row['title'], row['price']) for row in rows]

    def create_game(self, title, price):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO games (title, price) VALUES (%s, %s)", (title, price))
        conn.commit()
        cursor.close()
        conn.close()