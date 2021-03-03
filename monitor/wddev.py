import os, webdav3

cDir = os.getcwd()
from webdav3.client import Client

test_dir = None
test_file = None
test_host = None

options = {
    'webdav_hostname': test_host,
    'webdav_login': os.environ['ws_user'],
    'webdav_password': os.environ['ws_pwd'],
}


client = Client(options)
# client.verify = False  # To not check SSL certificates (Default = True)


if __name__ == '__main__':
    if os.path.exists(os.path.join(cDir, test_file)):
        os.remove(os.path.join(cDir, test_file))
        print('Download test file \"{}\" removed.'.format(test_file))

    print('test_dir exists:', client.check(test_dir))
    print('test_file exists:', client.check('{}/{}'.format(test_dir, test_file)))
    print('unknown file exists:', client.check('{}/{}a'.format(test_dir, test_file)))

    client.download_sync(
        '{}/{}'.format(test_dir, test_file), os.path.join(cDir, test_file)
    )
    print(
        'Downloaded file \"{}\": {}'.format(
            test_file, os.path.exists(os.path.join(cDir, test_file))
        )
    )
