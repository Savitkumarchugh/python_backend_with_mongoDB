from flask import Flask, request, jsonify
from connection import GymDB

app = Flask(__name__)
db = GymDB()


# -------------------------------
# HEALTH CHECK
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Gym API is running 🚀"})


# -------------------------------
# CREATE USER
# -------------------------------
@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.json

        required_fields = ["UserId", "Name", "Package_Period", "Start_Date", "Amount_Paid", "Phone_Number"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        db.create_user(data)
        return jsonify({"message": "✅ User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# GET ALL USERS
# -------------------------------
@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        users = db.get_all_users()
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# GET SINGLE USER
# -------------------------------
@app.route("/users/<name>", methods=["GET"])
def get_user(name):
    try:
        user = db.get_user_by_name(name)

        if isinstance(user, str):
            return jsonify({"error": user}), 404

        return jsonify(user), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# UPDATE USER
# -------------------------------
@app.route("/users/<name>", methods=["PUT"])
def update_user(name):
    try:
        data = request.json

        db.update_user(name, data)
        return jsonify({"message": "✅ User updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# DELETE USER
# -------------------------------
@app.route("/users/<name>", methods=["DELETE"])
def delete_user(name):
    try:
        db.delete_user(name)
        return jsonify({"message": "✅ User deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
