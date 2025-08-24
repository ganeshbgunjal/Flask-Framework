from flask import Flask

'''
It creates an instance of the flask app. 
which will be your WSGI (web server gateway interface) application.
'''

#### WSGI application:-
app = Flask(__name__)

@app.route("/")
def welcome():
    return 'Welcome to Flask tutorial!.\n This is an amazing and best course to become Data scientist!'

@app.route("/index")
def index():
    return 'Welcome to the Index page!'

@app.route('/notification')
def notification():
    return 'You have 4 Notifications!'


if __name__ == '__main__':     # This is the entry point of any .py file.
    app.run(debug=True)                   # to run app

