from flask import Flask, request, jsonify

app = Flask(__name__)

# Example database (use PostgreSQL for production)
keys_db = {
    "ABC123": {"hwid": None},
    "DEF456": {"hwid": "ABCDEF1234"},
}

@app.route("/validate", methods=["POST"])
def validate_key():
    data = request.json
    key = data.get("key")
    hwid = data.get("hwid")

    if key not in keys_db:
        return jsonify({"status": "invalid", "message": "Invalid key"}), 400

    if keys_db[key]["hwid"] is None:
        # First time use, bind to HWID
        keys_db[key]["hwid"] = hwid
        return jsonify({"status": "success", "message": "Key bound to HWID"}), 200
    elif keys_db[key]["hwid"] == hwid:
        return jsonify({"status": "success", "message": "Access granted"}), 200
    else:
        return jsonify({"status": "error", "message": "HWID mismatch"}), 403

if __name__ == "__main__":
    app.run()
