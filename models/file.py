from db import db

class FileModel:
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256))
    folder_id = db.Column(db.Integer)
    user_id = db.Column(db_Integer)

    def __init__(self, filename, folder_id, user_id):
        self.filename = filename
        self.folder_id = folder_id
        self.user_id = user_id

    def find_by_name(self, filename):
        return self.query.filter_by(filename=filename)

    def save_to_db(self):
        db.session.ass(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
