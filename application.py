from flask import Flask

application = Flask(__name)

@application.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')