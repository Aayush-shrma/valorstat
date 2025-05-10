from flask import Flask
from routes.stats import stats_bp
from routes.leaderboard import leaderboard_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(stats_bp)
app.register_blueprint(leaderboard_bp)

if __name__ == '__main__':
    app.run(debug=True)
