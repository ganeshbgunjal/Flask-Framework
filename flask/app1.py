from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_welcome():
    return 'Welcome to Data Science this course!'

@app.route('/message')
def print_message():
    return 'You have 5 messages in your inbox!'


if __name__ == '__main__':
    app.run(debug = True)