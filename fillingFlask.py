from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to Software Dev!"

@app.route('/hi')
def hi():
    return "Hello World"

@app.route('/bye')
def bye():
    return "Bye"

if __name__ == '__main__':
    app.run()
