from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
     greeting = True
     return render_template('index.html', greeting=greeting)

@app.route('/test')
def hello_world():
    greeting = "This is a test."
    return render_template("test.html", greeting=greeting)
    

if __name__ == '__main__':
     app.run()

## Debug mode
# if __name__ == '__main__':
#     app.run(debug=True)