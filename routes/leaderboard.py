from flask import Blueprint, render_template
from db import players_collection

leaderboard_bp = Blueprint("leaderboard", __name__, url_prefix="/leaderboard")

@leaderboard_bp.route('/')
def leaderboard():
    leaderboard_data = players_collection.find().sort("elo", -1)  # Sort by Elo (optional)
    return render_template("home.html", leaderboard=leaderboard_data)
