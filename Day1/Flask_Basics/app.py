from flask import Flask

app  = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to ML Application Training Dya-1<h1>"


@app.route('/info')
def info():
    return "<h1>Welcome to Info Page.</h1>"

@app.route('/name/<name>')
def name(name):
    return "<h1>This page is designed for {}.</h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True)