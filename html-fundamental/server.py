from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/contact")
def get_contact():
    print(url_for('get_contact'))
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)
