from flask import Flask, jsonify, session # type: ignore
from models import User

app = Flask(__name__) # type: ignore

@app.route("/users", methods = ["GET"])
def get_users():
    users = session.query(User).all() # type: ignore
    return jsonify([user.name for user in users])