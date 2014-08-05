# Force everything over HTTP if you're too cheap to get an SSL certificate.
# Also changes the puu.sh check to pass so you can use different domains.
# OSX only. If you have a developer account, you should resign the resulting executable.

from os.path import join
PUUSH_PATH = '/Applications/puush.app'

# HTTP patch
BINARY_TO_FIND = '\x68\x74\x74\x70\x73\x3A\x2F\x2F\x70\x75\x75\x73\x68\x2E\x6D\x65\x2F\x25\x40\x00' # https://puush.me/api
PATCH_CONTENTS = '\x68\x74\x74\x70\x3A\x2F\x2F\x70\x75\x75\x73\x68\x2E\x6D\x65\x2F\x25\x40\x2F\x00' # http://puush.me/api/


# puu.sh check

PUUSH_FIND = '\x48\x8D\x15\xF0\x06\x02\x00\x48\x89\xC7\xFF\x15\x3F\x2F\x01\x00\xB8\xFE\xFF\xFF\xFF\x45\x31\xFF'
PUUSH_PATCH = '\x0F\x1F\x00'

f = open(join(PUUSH_PATH,'Contents','MacOS','puush'),'r+w+b')
contents = f.read()

idx = contents.find(BINARY_TO_FIND)
idx_2 = contents.find(PUUSH_FIND)

if idx > 0:
    f.seek(idx)
    f.write(PATCH_CONTENTS)

if idx_2 > 0:
	f.seek(idx_2 + 24)
	f.write(PUUSH_PATCH)

f.close()
