from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import exc
import json
from run import db




class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))


db.create_all()



with open('data/user.json', 'r', encoding='utf8') as file:
    users = json.load(file)
    for user in users:
        current_user = User(**user)

        db.session.add(current_user)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Table already initialized and filled")


def get_users_all() -> list[dict]:
    """
    Возвращает всех пользователей для роута /users
    """
    users_data = []
    for user in User.query.all():
        users_data.append(user.return_data())
    return users_data


