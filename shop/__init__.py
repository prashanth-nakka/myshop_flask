from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URL"
] = "postgresql://postgres:12345@localhost/flask_ecom"
app.config["SECRET_KEY"] = "gdhgfrwfuegu1374ds"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from shop.admin import routes
