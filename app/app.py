from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return "web-api v1.0.1 running"
# IMPORTANT: no app.run() here
