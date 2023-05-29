from flask import Flask, render_template
import datetime
import time

app = Flask(__name__)

year = datetime.datetime.now().year

print(year)
@app.route("/")
def homepage():
    return render_template("index.html", cuurent_year= year)

if __name__ == "__main__":
    app.run(debug=True)
