from flask import Flask, jsonify
import requests, os

app = Flask(__name__)

# ====== ROTAS - ISABELA ======

@app.route("/isabela/verificacao", methods=["GET"])
def isabela_verificacao():
    secret = "e1snqw"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        print("VERIFICACAO -> STATUS:", res.status_code)
        print("BODY:", res.text)
        return jsonify({"status_code": res.status_code, "body": res.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/isabela/brinquedo1", methods=["GET"])
def isabela_brinquedo1():
    secret = "jtvn2e"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        print("BRINQUEDO1 -> STATUS:", res.status_code)
        print("BODY:", res.text)
        return jsonify({"status_code": res.status_code, "body": res.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/isabela/brinquedo2", methods=["GET"])
def isabela_brinquedo2():
    secret = "ns4ejo"
    url = f"https://privecall.com/api/automation/{secret}"
    try:
        res = requests.post(url)
        print("BRINQUEDO2 -> STATUS:", res.status_code)
        print("BODY:", res.text)
        return jsonify({"status_code": res.status_code, "body": res.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
