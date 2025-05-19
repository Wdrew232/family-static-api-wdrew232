from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Family already initialized with 3 members from the class
jackson_family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify({
            "name": member.get("first_name"),  # ✅ must be "name", not "first_name"
            "id": member.get("id"),
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers")
        }), 200
    return jsonify({"error": "Member not found"}), 404


@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Invalid input"}), 400
    jackson_family.add_member(data)
    return jsonify({
        "message": "Member added successfully",
        "member": data
    }), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
