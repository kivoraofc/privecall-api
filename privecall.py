from flask import Flask, redirect, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/criar_sala", methods=["GET"])
def criar_sala():
    # Seu link secreto (não mostre pra ninguém)
    secret = "w1xr4b"
    url = f"https://privecall.com/api/automation/{secret}"

    # Faz o POST pra PriveCall criar a sala
    response = requests.post(url)
    data = response.json()

    # Se der certo, redireciona o cliente direto pra sala
    if data.get("success"):
        return redirect(data["chatUrl"])
    else:
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
