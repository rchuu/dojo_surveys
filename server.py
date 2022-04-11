# added render_template!
from flask import Flask, render_template, session, request, redirect

from env import KEY

app = Flask(__name__)

app.secret_key = KEY  # app.secret_key ="my secret key"


@app.route('/')  # landing page, default
def index():
    return render_template('index.html')  # display the html


@app.route('/process', methods=['POST'])  # hidden route -
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route('/result')  # result page
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
