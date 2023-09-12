from flask import flask
app = Flask(__name__)

@app.route("/")
def Bonjour():
  return "<p>Bienvenue, Bonjour ! </p>"