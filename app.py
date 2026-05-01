from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users_collection = db["users"]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Flask + MongoDB API is running"})


@app.route("/test")
def test():
    return "PR test"


# ✅ Create new user API
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    user = {
        "name": name,
        "email": email
    }

    result = users_collection.insert_one(user)

    return jsonify({
        "message": "User created successfully",
        "user_id": str(result.inserted_id)
    }), 201


# Optional: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in users_collection.find():
        users.append({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        })

    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
