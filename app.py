# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def index():
    return render_template('index.html')  # return a string

@app.route('/who')
def who():
    return render_template('who.html')

@app.route('/atelier_tissage')
def ateliers():
    return render_template('ateliers.html')

@app.route('/deontologie')
def deonto():
    return render_template('deontologie.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
