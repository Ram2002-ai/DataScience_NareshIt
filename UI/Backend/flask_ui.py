from flask import Flask
from flask import request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

app.run(host='127.0.0.1')