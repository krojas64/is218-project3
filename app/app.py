from flask import Flask, request, render_template, flash, url_for, redirect
# from calc.calculator import Calculator

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/subsect')
def subsection():
    flash("Logged in!")
    return render_template('subsect.html')
