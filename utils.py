
from create_db import *

def get_users_all() -> list[dict]:
    """
    Возвращает всех пользователей для роута /users
    """
    users_data = []
    for user in User.query.all():
        users_data.append(user.return_data())
    return users_data
