from flask import Flask, redirect, jsonify
import requests, os, json

app = Flask(__name__)

# ====================================================
# NOVAS ROTAS
# ====================================================

# 🟣 Modelo 1
@app.route("/modelo1", methods=["GET"])
def modelo1():
    secret = "336xth"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        data = res.json()

        # Garante que o conteúdo é JSON mesmo se vier como string
        if isinstance(data, str):
            data = json.loads(data)

        # Redireciona se o retorno for válido
        if data.get("success") and "chatUrl" in data:
            return redirect(data["chatUrl"])

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🟣 Modelo 2
@app.route("/modelo2", methods=["GET"])
def modelo2():
    secret = "8fdq29"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        data = res.json()
        if isinstance(data, str):
            data = json.loads(data)
        if data.get("success") and "chatUrl" in data:
            return redirect(data["chatUrl"])
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🟣 Modelo 3
@app.route("/modelo3", methods=["GET"])
def modelo3():
    secret = "fix5hn"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        data = res.json()
        if isinstance(data, str):
            data = json.loads(data)
        if data.get("success") and "chatUrl" in data:
            return redirect(data["chatUrl"])
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ====================================================
# SERVIDOR
# ====================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
