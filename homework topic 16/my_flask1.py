from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/life')
def life():
    return render_template('life.html')

@app.route('/apple')
def apple():
    return render_template('fqfqw.html')




app.run(port=8080)

