from flask import Flask, Blueprint
from config.db import generate_tables
from router.player_router import player_bp

app = Flask(__name__)

app.register_blueprint(player_bp)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    generate_tables()
    app.run(debug=True)