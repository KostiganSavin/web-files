from flask import Flask
from flask_jsonrpc import JSONRPC


app = Flask(__name__)
auth = HTTPBasicAuth()
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)


@jsonrpc.method('App.index')
# @auth.login_required
def index():
    return 'Welcome to Flask JSON-RPC'

def create_folder(foldername):
    pass

def delete_folder(foldername):
    pass

def add_file_to_folder(filename, foldername):
    pass

def delete_file_from_folder(filename, foldername):
    pass

def copy_file(filename, source_folder, dest_folder):
    pass

def file_download(filename)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
