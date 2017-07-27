from db import db

class FileModel(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256))
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=False)
    folder = db.relationship('FolderModel')

    def __init__(self, filename, folder_id):
        self.filename = filename
        self.folder_id = folder_id

    def __str__(self):
        return self.filename

    @classmethod
    def find_by_name_and_foldername(cls, filename, folder):
        print('class F', folder.id)
        print('class file', filename)
        return cls.query.filter_by(filename=filename).filter_by(folder_id=folder.id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
