from flask import Flask, render_template, request
from rootkit_detector import scan_file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = " "
    if request.method == "POST":
        filename = request.form["filename"]
        result = scan_file(filename)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)