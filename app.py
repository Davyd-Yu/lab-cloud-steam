from flask import Flask
from flasgger import Swagger
from app.my_project.games.route.game_route import games_bp

app = Flask(__name__)

# Підключаємо Swagger (авто-документацію)
swagger = Swagger(app)

# Реєструємо наші маршрути
app.register_blueprint(games_bp)

@app.route('/')
def home():
    return """
    <h1>Steam Project Live!</h1>
    <p>Go to <a href="/apidocs">/apidocs</a> to test the API.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)