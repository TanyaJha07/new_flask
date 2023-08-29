from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.route("/hello/<twinkle>")
def hello_world3(twinkle):
    return f"<p>Hello,{twinkle}!</p>"


if __name__ == '__main__':
    app.run(debug=True)