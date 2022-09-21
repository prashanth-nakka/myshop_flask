from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URL"
] = "postgresql://postgres:12345@localhost/flask_ecom"
db = SQLAlchemy(app)

from shop import routes
