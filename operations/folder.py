from flask_jsonrpc import JSONRPC

@jsonrpc.method('App.create_folder(String)-> String')
def create_folder(foldername):
    return 'We create folder {0}'.format(foldername)

@jsonrpc.method('App.delete_folder(String)-> String')
def delete_folder(foldername):
    return 'We delete folder {0}'.format(foldername)
