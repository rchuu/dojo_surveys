from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.survey import Survey


@app.route('/')  # landing page, default
def index():
    return render_template('index.html')  # display the html


@app.route('/create', methods=['POST'])  # hidden route -
def create():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/result')
    return redirect('/')


@app.route('/result')  # result page
def result():
    return render_template('result.html', survey=Survey.get_survey())
