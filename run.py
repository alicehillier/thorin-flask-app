from flask import Flask, render_template
import os

# name is the built in variable for name of the app
app = Flask(__name__)

# decorator to wrap function - if user returns to route directory,
# triggers index()
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# __main__ is the default module
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # debug should only be true while in development. once deployed, should be set to false
        debug=True
    )