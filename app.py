
from flask import Flask, request

app = Flask(__name__)


# Addition API
@app.route('/add')
def add():

    a = request.args.get('a')
    b = request.args.get('b')

    if a is None or b is None:
        return {"error": "Both numbers are required"}, 400

    try:
        a = float(a)
        b = float(b)

    except ValueError:
        return {"error": "Please enter valid numbers"}, 400

    result = a + b

    return {"result": result}


# Subtraction API
@app.route('/subtract')
def subtract():

    a = request.args.get('a')
    b = request.args.get('b')

    if a is None or b is None:
        return {"error": "Both numbers are required"}, 400

    try:
        a = float(a)
        b = float(b)

    except ValueError:
        return {"error": "Please enter valid numbers"}, 400

    result = a - b

    return {"result": result}


# Multiplication API
@app.route('/multiply')
def multiply():

    a = request.args.get('a')
    b = request.args.get('b')

    if a is None or b is None:
        return {"error": "Both numbers are required"}, 400

    try:
        a = float(a)
        b = float(b)

    except ValueError:
        return {"error": "Please enter valid numbers"}, 400

    result = a * b

    return {"result": result}


# Division API
@app.route('/divide')
def divide():

    a = request.args.get('a')
    b = request.args.get('b')

    if a is None or b is None:
        return {"error": "Both numbers are required"}, 400

    try:
        a = float(a)
        b = float(b)

    except ValueError:
        return {"error": "Please enter valid numbers"}, 400

    if b == 0:
        return {"error": "Cannot divide by zero"}, 400

    result = a / b

    return {"result": result}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

