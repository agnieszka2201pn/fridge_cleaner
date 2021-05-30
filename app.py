from flask import Flask

app = Flask(__name__)

@app.route('/elo')
def hello():
    return "Hello, World!"