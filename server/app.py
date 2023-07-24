#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    written_badly = ''
    for i in range(0,int(parameter)):
        written_badly = written_badly + str(i) + '\n'
    return written_badly

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    sol = ''
    if operation == '+':
        sol = int(num1) + int(num2)
    if operation == '-':
        sol = int(num1) - int(num2)
    if operation == '*':
        sol = int(num1) * int(num2)
    if operation == 'div':
        sol = int(num1) / int(num2)
    if operation == '%':
        sol = int(num1) % int(num2)
    
    return str(sol)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
