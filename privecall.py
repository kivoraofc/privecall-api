from flask import Flask, redirect, jsonify
import requests, os

app = Flask(__name__)

# ==========================================================
# 🚀 ROTAS - ISABELA
# ==========================================================

# 🟣 Verificação
@app.route("/isabela/verificacao", methods=["GET"])
def isabela_verificacao():
    secret = "e1snqw"
    url = f"https://privecall.com/api/automation/{secret}"
    res = requests.post(url)
    data = res.json()
    if data.get("success"):
        return redirect(data["chatUrl"])
    return jsonify(data)

# 🩷 Brinquedo 1
@app.route("/isabela/brinquedo1", methods=["GET"])
def isabela_brinquedo1():
    secret = "jtvn2e"
    url = f"https://privecall.com/api/automation/{secret}"
    res = requests.post(url)
    data = res.json()
    if data.get("success"):
        return redirect(data["chatUrl"])
    return jsonify(data)

# 💛 Brinquedo 2
@app.route("/isabela/brinquedo2", methods=["GET"])
def isabela_brinquedo2():
    secret = "ns4ejo"
    url = f"https://privecall.com/api/automation/{secret}"
    res = requests.post(url)
    data = res.json()
    if data.get("success"):
        return redirect(data["chatUrl"])
    return jsonify(data)

# ==========================================================
# 🔧 CONFIGURAÇÃO SERVIDOR (Railway usa a variável PORT)
# ==========================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
