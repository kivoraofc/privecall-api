from flask import Flask, redirect, jsonify
import requests, os

app = Flask(__name__)

# ==================== ROTAS - ISABELA ====================

@app.route("/isabela/verificacao", methods=["GET"])
def isabela_verificacao():
    return chamar_automation("e1snqw")

@app.route("/isabela/brinquedo1", methods=["GET"])
def isabela_brinquedo1():
    return chamar_automation("jtvn2e")

@app.route("/isabela/brinquedo2", methods=["GET"])
def isabela_brinquedo2():
    return chamar_automation("ns4ejo")


def chamar_automation(secret):
    """Função genérica que chama a API do PriveCall com segurança"""
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url, timeout=10)
        data = res.json()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if data.get("success") and data.get("chatUrl"):
        return redirect(data["chatUrl"])
    else:
        return jsonify({"error": "Resposta inesperada do servidor", "data": data}), 400


# ==================== CONFIG SERVIDOR ====================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
