from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/upload',  methods=['POST', 'GET'])  
def upload():
    return render_template("file_uploading_form_laid_out.html")

@app.route('/success', methods=['POST', 'GET'])  
def SaveAs():
    if request.method == "POST":
        file = request.files['file']
        file.save(file.filename)
        return render_template("success.html", name=file.filename)

if __name__ == "__main__":
    app.run(debug=True)