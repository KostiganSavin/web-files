from db import db

class UserModel:
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    usename = db.Column(db.String(128))
    password = db.Column(db.String(80))

    def __init__(self, .username, password):
        self.username = usernamre
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def find_by_name(self, username):
        return self.query.filter_by(username=username).first()

    def find_by_id(self, _id):
        return self.query.filter_by(id=_id).first()
