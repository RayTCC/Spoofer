from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {
    "MY-FREE-KEY-001": None,
    "TEST-KEY-123456": None
}

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    key = data.get("key")
    hwid = data.get("hwid")

    if key not in licenses:
        return jsonify(success=False, message="Invalid key")

    if licenses[key] is None:
        licenses[key] = hwid
        return jsonify(success=True, message="Key validated and HWID locked")

    if licenses[key] == hwid:
        return jsonify(success=True, message="Key validated")

    return jsonify(success=False, message="HWID mismatch")

@app.route('/')
def home():
    return "License API running!"
