from db import db

class FolderModel(db.Model):
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    foldername = db.Column(db.String(256))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship('UserModel')
    files = db.relationship('FileModel')

    def __init__(self, foldername, owner_id):
        self.foldername = foldername
        self.owner_id = owner_id

    @classmethod
    def find_by_name_and_owner(cls, foldername, owner):
        return cls.query.filter_by(foldername=foldername).filter_by(owner_id=owner.id).first()

    def save_to_db(self):
        print('save')
        print(self)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
