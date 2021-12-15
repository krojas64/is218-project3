from flask import Flask, request, render_template, flash, url_for, redirect
from calc.calculator import Calculator

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/subsect', methods=['GET', 'POST'])
def subsection():
    if request.method == 'POST':
        if request.form['val1'] == '' or request.form['val2'] == '':
            error = 'You must enter a value for 1 and 2 (no empty values)'
        else:
            value1 = request.form['val1']
            value2 = request.form['val2']
            operation = request.form['operation']
            numbers = (value1, value2)
            getattr(Calculator, operation)(numbers)
            result = str(Calculator.get_last_result_value())
            return render_template('result.html',value1=value1, value2=value2, operation=operation, result=result)
        return render_template('subsect.html', error=error)
    else:
        return render_template('subsect.html')
