from flask import Flask, render_template

app  = Flask(__name__)

@app.route('/')
def index():
    name = "Vishwajeet"
    l1 = list(name)
    d1 = {"name":"Vishwajeet"}

    l2 = ["ML","AI","DL","DS"]

    return render_template("index.html", name=name, l1=l1, d1=d1, l2=l2)

@app.route('/friend')
def friend():
    name = "Vivek"
    return render_template('friend.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)