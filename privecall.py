from flask import Flask, redirect, jsonify
import requests, os, json

app = Flask(__name__)

# ====================================================
# ROTAS - ISABELA
# ====================================================

# 🟣 ISABELA - Verificação
@app.route("/isabela/CALL1", methods=["GET"])
def isabela_verificacao():
    secret = "336xth"
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


# 🟣 ISABELA - Brinquedo 1
@app.route("/isabela/CALL2", methods=["GET"])
def isabela_brinquedo1():
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


# 🟣 ISABELA - Brinquedo 2
@app.route("/isabela/CALL3", methods=["GET"])
def isabela_brinquedo2():
    secret = "htn4eg"
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
# ROTAS - LORENA
# ====================================================

# 🟣 LORENA - 7 Min
@app.route("/lorena/CALL1", methods=["GET"])
def lorena_call1():
    secret = "ckczty"
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


# 🟣 LORENA - Strip
@app.route("/lorena/CALL2", methods=["GET"])
def lorena_call2():
    secret = "00vq1e"
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


# 🟣 LORENA - 15 Min
@app.route("/lorena/CALL3", methods=["GET"])
def lorena_call3():
    secret = "ugsxxd"
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


# 🟣 LORENA - Amigo
@app.route("/lorena/CALL4", methods=["GET"])
def lorena_call4():
    secret = "ppfeev"
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
