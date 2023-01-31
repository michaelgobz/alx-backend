from flask_babel import Babel
from flask import Flask, render_template

app = Flask("__name__")

babel = Babel(app)

@app.route("/):
def index():
    render_template("/templates/0-index.html")



if __name__ == "__main__":
   app.run()

