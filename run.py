from flask import Flask, render_template
import os
import json

# name is the built in variable for name of the app
app = Flask(__name__)

# decorator to wrap function - if user returns to route directory,
# triggers index()
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # r means read only.
    # assigns contents of file to variable json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # assign new variable called company, which contains the contents of json file, to send to html template
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<character_name>")
def about_character(character_name):
    character = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == character_name:
                character = obj
                # First character is variable passed into html file, second character is second variable created in this function
    return render_template("character.html", character=character)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# __main__ is the default module
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # debug should only be true while in development. once deployed, should be set to false
        debug=True
    )