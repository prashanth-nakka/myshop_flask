from flask import request, render_template, session, url_for, flash, redirect
from .forms import RegistrationForm
from shop import app, db


@app.route("/")
def home():
    return "Home Page"


@app.route(
    "/register",
    methods=[
        "GET",
        "POST",
    ],
)
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        flash("Thanks for Registering")
        return redirect(url_for("login"))
    else:
        pass
    return render_template("admin/register.html", title="Register", form=form)
