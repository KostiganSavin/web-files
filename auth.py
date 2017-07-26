from flask.ext.httpauth import HTTPBasicAuth

users = {
    'john': 'hello',
    'susan': 'bye'
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@auth.verify_password
def verify_pwd(username, password):
    return users.get(username) == password
