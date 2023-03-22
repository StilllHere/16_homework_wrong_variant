from flask import Flask
from users.views import users_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_hw16_db.db"

db = SQLAlchemy()

app.register_blueprint(users_blueprint)


if __name__ == "__main__":
    app.run()