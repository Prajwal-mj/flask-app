#!/Library/Developer/CommandLineTools/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()