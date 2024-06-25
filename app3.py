from flask import Flask 

app = Flask(__name__)


@app.route('/') 
def name():
    return "your surname"

@app.route('/name') 
def name():
    return "your name"

@app.route('/contact')
def contact():
    return "your contact is"

@app.route('/address')
def address():
    return "your address"

if __name__ == '__main__':
    app.run(debug=True)