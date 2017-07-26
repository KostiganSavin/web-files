from flask_httpauth import HTTPBasicAuth
from models.user import UserModel

auth = HTTPBasicAuth()

# users = {
#     'kast': 'hello',
#     'susan': 'bye'
# }
#
# @auth.get_password
# def get_pw(username):
#     if username in users:
#         return users.get(username)
#     return None
#
# @auth.verify_password
# def verify_pwd(username, password):
#     return users.get(username) == password

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
