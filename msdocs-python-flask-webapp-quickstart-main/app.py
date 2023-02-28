from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Abeer Ahmed from pune'

@app.route('/hello')
def hello():
    return 'This is the hello world page.'