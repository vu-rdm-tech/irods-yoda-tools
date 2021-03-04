import os, webdav3, json, getpass

cDir = os.path.dirname(os.path.abspath(os.sys.argv[0]))

from webdav3.client import Client

# configure options
with open('..\\noupload\\config.json', 'r') as F:
    options = json.load(F)

# select aimms or vu configuraiton

# options = options['aimms']
options = options['vu']


test_dir = options['test_dir']
test_file = options['test_file']
options['webdav_password'] = getpass.getpass(
    '\nPlease enter webdav password for \"{}\": '.format(options['webdav_login'])
)


client = Client(options)
client.verify = False  # To not check SSL certificates (Default = True)


if os.path.exists(os.path.join(cDir, test_file)):
    os.remove(os.path.join(cDir, test_file))
    print('Download test file \"{}\" removed.'.format(test_file))

print('test_dir exists:', client.check(test_dir))
print('test_file exists:', client.check('{}/{}'.format(test_dir, test_file)))
print('unknown file exists:', client.check('{}/{}a'.format(test_dir, test_file)))

client.download_sync('{}/{}'.format(test_dir, test_file), os.path.join(cDir, test_file))
print(
    'Downloaded file \"{}\": {}'.format(
        test_file, os.path.exists(os.path.join(cDir, test_file))
    )
)

options['webdav_password'] = None
