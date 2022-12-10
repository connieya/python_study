from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def buy():
    return 'Oh~~ Yeah!!!!'

if __name__ == "__main__":
    app.run(debug=True)