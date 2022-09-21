from flask import request, url_for, render_template, session

from shop import app, db


@app.route("/")
def home():
    return "Home Page"


@app.route("/register")
def register():
    return render_template("admin/register.html", title="Register")
