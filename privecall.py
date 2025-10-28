from flask import Flask, redirect, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/criar_sala", methods=["GET"])
def criar_sala():
    secret = "w1xr4b"  # sua chave do PriveCall
    url = f"https://privecall.com/api/automation/{secret}"
    res = requests.post(url)
    data = res.json()

    if data.get("success"):
        return redirect(data["chatUrl"])
    else:
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
