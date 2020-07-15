from flask import Flask, redirect, request, abort, render_template, session
from flask_cors import CORS
from flask_socketio import SocketIO
import json
import os


app = Flask(__name__, template_folder="templates/")
CORS(app)
socketio = SocketIO(app)

app.secret_key = "gator-semantic-annotator"


### / - routes for the editor and browser ui, GET only


@app.route("/", methods=["GET"])
def cnsa():
    return render_template("editor.html")


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5050

    import sys

    for arg in sys.argv:
        if "=" in arg:
            k = arg.split("=")[0]
            v = arg.split("=")[1]

            if k == "host":
                host = v
            if k == "port":
                port = int(v)

    socketio.run(app, host=host, port=port, debug=False)
