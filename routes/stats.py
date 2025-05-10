from flask import Blueprint, render_template, request
import requests
import os
from dotenv import load_dotenv
from db import players_collection

load_dotenv()

API_KEY = os.getenv("HENRIK_API_KEY")
stats_bp = Blueprint("stats", __name__)

@stats_bp.route('/')
def home():
    return render_template("index.html")

@stats_bp.route('/stats', methods=['POST'])
def stats():
    name = request.form['name']
    tag = request.form['tag']
    region = "ap"

    url = f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{name}/{tag}"
    headers = {"Authorization": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        players_collection.update_one(
            {"name": name, "tag": tag},
            {"$set": data['data']},
            upsert=True
        )
        return render_template("stats.html", data=data)
    else:
        return f"Error fetching data: {response.status_code}"
