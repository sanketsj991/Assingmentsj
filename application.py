"""
Your module docstring goes here (replace this line).
"""

from flask import Flask

application = Flask(__name)

@application.route('/')
def hello() -> str:
    """
    This is the docstring for the hello function.
    It returns a greeting message.
    """
    return "Hello, World!"

if __name__ == '__main__':
    application.run(
        debug=True,
        host='0.0.0.0'
    )
