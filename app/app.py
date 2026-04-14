from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "web-api running in PRODUCTION"

# IMPORTANT: no app.run() here
