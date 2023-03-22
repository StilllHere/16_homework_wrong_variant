from flask import Blueprint
import json
from create_db import get_users_all

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users/')
def user_page():
    return json.dumps(get_users_all())

