from flask import Flask, request, render_template, flash

# from calc.calculator import Calculator

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    flash("This is a test message")
    return render_template("index.html")


@app.route('/subsect')
def subsection():
    flash("Another flash message!")
    return render_template("subsect.html")
