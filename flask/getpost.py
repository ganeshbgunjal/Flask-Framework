from flask import Flask, render_template, request

'''
It creates an instance of the flask app. 
which will be your WSGI (web server gateway interface) application.
'''

#### WSGI application:-
app = Flask(__name__)

@app.route("/")
def welcome():
    return '''<html><H1>Welcome to this Data Scientist course!</H1></html>\
            <html><H2>Become a Pro Data Scientist!</H2></html>'''

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':     # This is the entry point of any .py file.
    app.run(debug=True)                   # to run app

