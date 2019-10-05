from flask import Flask
from flask_cors import CORS
from flask import request
import logging
app = Flask(__name__)
CORS(app)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/summarize", methods =["GET"])
def summarize_text():
    text = request.args.get("text")
    return text
if __name__ == '__main__':
    app.run(host='0.0.0.0')