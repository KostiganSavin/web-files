import os
from flask import Flask
from flask_jsonrpc import JSONRPC
from auth import auth
from models.user import UserModel
from models.folder import FolderModel
from models.file import FileModel

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.secret_key = 'kostigan'
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


@jsonrpc.method('App.index')
@auth.login_required
def index():
    return 'Welcome to Flask JSON-RPC'


@jsonrpc.method('App.register(String, String) -> String')
def register(username, password):
    if UserModel.find_by_name(username):
        return "User '{}' already exists".format(username)
    user = UserModel(username, password)
    user.save_to_db()
    return 'User registred'


@jsonrpc.method('App.create_folder(String)-> String')
@auth.login_required
def create_folder(foldername):
    owner = UserModel.find_by_name(auth.username())
    folder = FolderModel.find_by_name_and_owner(foldername, owner)
    if folder:
        return 'We already have folder with name "{}"'.format(foldername)
    new_folder = FolderModel(foldername, owner.id)
    new_folder.save_to_db()
    return 'We created folder {0}'.format(foldername)


@jsonrpc.method('App.delete_folder(String)-> String')
@auth.login_required
def delete_folder(foldername):
    owner = UserModel.find_by_name(auth.username())
    folder = FolderModel.find_by_name_and_owner(foldername, owner)
    folder.delete_from_db()
    return 'We delete folder {0}'.format(foldername)


@jsonrpc.method('App.add_file_to_folder(String, String)-> String')
@auth.login_required
def add_file_to_folder(filename, foldername):
    owner = UserModel.find_by_name(auth.username())
    file_ = FileModel.find_by_name_and_foldername(filename, foldername)
    if file_:
        return 'We already have file with name "{}" in folder "{}"'.format(filename, foldername)
    folder = FolderModel.find_by_name_and_owner(foldername, owner)
    if folder:
        file_ = FileModel(filename, folder.id)
        file_.save_to_db()
    else:
        new_folder = FolderModel(foldername, owner.id)
        new_folder.save_to_db()
        file_ = FileModel(filename, new_folder.id)
        file_.save_to_db()
    return 'We create file {0} in folder {1}'.format(filename, foldername)


@jsonrpc.method('App.delete_file_from_folder(String, String)-> String')
@auth.login_required
def delete_file_from_folder(filename, foldername):
    owner = UserModel.find_by_name(auth.username())
    folder = FolderModel.find_by_name_and_owner(foldername, owner)
    file_ = FileModel.find_by_name_and_foldername(filename, folder.foldername)
    file_.delete_from_db()
    return 'We delete file {0} from folder {1}'.format( filename, foldername)


@jsonrpc.method('App.move_file(String, String, String)-> String')
@auth.login_required
def move_file(filename, source_folder, dest_folder):
    owner = UserModel.find_by_name(auth.username())
    folder_from = FolderModel.find_by_name_and_owner(source_folder, owner)
    folder_to = FolderModel.find_by_name_and_owner(dest_folder, owner)
    if not folder_from:
        return "There is not folder with name '{}'".format(source_folder)
    file_ = FileModel.find_by_name_and_foldername(filename, folder_from)
    if not file_:
        return "There is no file '{}' in folder '{}'".format(filename, source_folder)
    if folder_to:
        file_.folder_id = folder_to.id
        file_.save_to_db()
    else:
        new_folder = FolderModel(dest_folder, owner.id)
        new_folder.save_to_db()
        file_.folder_id = new_folder.id
        file_.save_to_db()
    return 'We moved file {0} from folder {1} to folder {2}'.format(filename, source_folder, dest_folder)


def file_download(filename):
    pass


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
