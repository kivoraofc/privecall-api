from flask import Flask, jsonify, redirect
import requests, os, json

app = Flask(__name__)

# =========================
#   ROTAS - ISABELA
# =========================

# 🔹 Verificação
@app.route("/isabela/verificacao", methods=["GET"])
def isabela_verificacao():
    secret = "e1snqw"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        data = res.json()

        # caso venha como string JSON dentro de outro JSON
        if isinstance(data, str):
            data = json.loads(data)

        # redireciona pro link do chat se for sucesso
        if data.get("success") and "chatUrl" in data:
            return redirect(data["chatUrl"])

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🔹 Brinquedo 1
@app.route("/isabela/brinquedo1", methods=["GET"])
def isabela_brinquedo1():
    secret = "jtvn2e"
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


# 🔹 Brinquedo 2
@app.route("/isabela/brinquedo2", methods=["GET"])
def isabela_brinquedo2():
    secret = "ns4ejo"
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


# =========================
#   CONFIG SERVIDOR
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
