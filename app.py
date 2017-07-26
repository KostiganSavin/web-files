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
    print(folder)
    print(folder.foldername)
    print(folder.owner_id)
    folder.delete_from_db()
    return 'We delete folder {0}'.format(foldername)

@jsonrpc.method('App.add_file_to_folder(String, String)-> String')
def add_file_to_folder(filename, foldername):
    return 'We create file {1} in folder {0}'.format(foldername, filename)

@jsonrpc.method('App.delete_file_from_folder(String, String)-> String')
def delete_file_from_folder(filename, foldername):
    return 'We delete file {1} from folder {0}'.format(foldername, filename)

@jsonrpc.method('App.copy_file(String, String, String, Boolean)-> String')
def copy_file(filename, source_folder, dest_folder, move):
    if move == True:
        return 'We moved file {0} from folder {1} to folder {2}'.format(filename, source_folder, dest_folder)
    return 'We copy file {0} from folder {1} to folder {2}'.format(filename, source_folder, dest_folder)

def file_download(filename):
    pass

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
