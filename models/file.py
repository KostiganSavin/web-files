from db import db

class FileModel(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256))
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'), unique=True, nullable=False)
    folder = db.relationship('FolderModel')


    def __init__(self, filename, folder_id):
        self.filename = filename
        self.folder_id = folder_id
        # self.user_id = user_id

    @classmethod
    def find_by_name(cls, filename):
        return cls.query.filter_by(filename=filename)

    def save_to_db(self):
        db.session.ass(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
