from flask_httpauth import HTTPBasicAuth
from models.user import UserModel

auth = HTTPBasicAuth()

@auth.get_password
def get_pw(username):
    user = UserModel.find_by_name(username)
    if user:
        return user.password
    return None

@auth.verify_password
def verify_pwd(username, password):
    user = UserModel.find_by_name(username)
    return user.password == password
