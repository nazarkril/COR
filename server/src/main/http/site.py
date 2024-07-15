from flask import Flask

hostName = "localhost"
serverPort = 8080

app = Flask(__name__)


@app.route('/')
def qq():
    return 'Hello'


@app.route('/hi')
def hi():
    return 'hi'


if __name__ == "__main__":
    app.run(host=hostName, port=serverPort)
