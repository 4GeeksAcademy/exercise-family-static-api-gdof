import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.route('/members', methods=['GET'])
def get_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if not member:
            return jsonify({"error": "Member not found"}), 404
        return jsonify(member), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/members', methods=['POST'])
def add_member():
    try:
        data = request.get_json(force=True)
        required_fields = {"first_name", "age", "lucky_numbers"}
        if not data or not required_fields.issubset(data.keys()):
            return jsonify({"error": f"Missing fields, required: {required_fields}"}), 400

      
        if "id" not in data or data["id"] is None:
            data["id"] = jackson_family._generate_id()

       
        member = {
            "id": data["id"],
            "first_name": data["first_name"],
            "age": data["age"],
            "lucky_numbers": data["lucky_numbers"]
        }
        jackson_family.add_member(member)
        return jsonify(member), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        success = jackson_family.delete_member(member_id)
        if not success:
            return jsonify({"error": "Member not found"}), 404
        return jsonify({"done": True}), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)