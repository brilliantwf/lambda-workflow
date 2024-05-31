from flask import (Flask, jsonify)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return '<h1><center>This Sample Flask Application</center></h1>'
