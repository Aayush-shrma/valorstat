from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://aayushsh8888:9139@aayush.hqzcf.mongodb.net/valorstat?retryWrites=true&w=majority")
db = client['valorstat']
players_collection = db['players']

@app.route('/')
def home():
    if players_collection.count_documents({}) == 0:
        players_collection.insert_one({"player_name": "TestPlayer", "score": 100})

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
