from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    name = request.args.get('name', 'nobody')

    if name:
        greet = request.args.get('greet', 'Hello')
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()