#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)

userdatabase = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(userdatabase.keys()))

@app.route("/users/<username>")
def user_data(username):
    name_lower = username.lower()
    if name_lower in userdatabase:
        return jsonify(userdatabase[name_lower])
    else:
        return jsonify({"error" : "User not found"}), 404

@app.route("/status")
def status():
    return "OK"

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json(silent=True)
    if new_user is None:
        return ({"error" : "Invalid JSON"}), 400
    if "username" not in new_user:
        return ({"error" : "Username is required"}), 400
    username = new_user["username"]
    username_lower = username.lower()
    if username_lower in userdatabase:
        return ({"error" : "Username already exists"}), 409
    userdatabase[username_lower] = new_user
    return jsonify({
        "message" : "User added",
        "user" : new_user
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
