from flask import request, render_template, session, url_for, flash, redirect
from .forms import RegistrationForm
from .models import User
from shop import app, db, bcrypt


@app.route("/")
def home():
    return render_template("admin/index.html", title="Admin Page")


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
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=hash_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {form.username.data}, Thanks for Registering", "success")
        return redirect(url_for("home"))
    else:
        pass
    return render_template("admin/register.html", title="Register", form=form)
