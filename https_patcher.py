# Force everything over HTTP if you're too cheap to get an SSL certificate.
# OSX only. If you have a developer account, you should resign the resulting executable.

from os.path import join
PUUSH_PATH = '/Applications/puush.app'
BINARY_TO_FIND = '\x68\x74\x74\x70\x73\x3A\x2F\x2F\x70\x75\x75\x73\x68\x2E\x6D\x65\x2F\x25\x40\x00' # https://puush.me/api
PATCH_CONTENTS = '\x68\x74\x74\x70\x3A\x2F\x2F\x70\x75\x75\x73\x68\x2E\x6D\x65\x2F\x25\x40\x2F\x00' # http://puush.me/api/

f = open(join(PUUSH_PATH,'Contents','MacOS','puush'),'r+w+b')
contents = f.read()

idx = contents.find(BINARY_TO_FIND)

if idx != 0:
    f.seek(idx)
    f.write(PATCH_CONTENTS)

f.close()
