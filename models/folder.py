from db import db

class FolderModel:
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    foldername = db.Column(db.String(256))
    user_id = db.Column(db.Integer)
    # db.relationship

    def __init__(self, foldername, user_id):
        self.foldername = foldername
        self.user_id = user_id

    def find_by_name(self, foldername):
        return self.query.filter_by(foldername=foldername)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
