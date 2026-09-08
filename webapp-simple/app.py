import os
import socket

from flask import Flask

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 5050))


@app.route("/")
def hello_world():
    return f"<p>Hello, World! (hote : {socket.gethostname()})</p>"


@app.route("/ping")
def ping():
    return {"reponse": "pong", "port": PORT}


if __name__ == "__main__":
    print(f"[webapp-simple] demarrage sur le port {PORT}", flush=True)
    app.run(host="0.0.0.0", port=PORT)
