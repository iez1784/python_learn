
import uuid
import time
from validate_email import validate_email
import os
import stat
import shutil


# delete folder
def rmtree(path):
    if os.path.exists(path):
        shutil.rmtree(path, onerror=del_rw)


# set right and  remove folder
def del_rw(action, name, exc):
    os.chown(name, stat.S_IWRITE)
    os.remove(name)


# generate rramdom uuid
def generate_uuid():
    return str(uuid.uuid4())

# time
def timestamp():
    return str(time.time())

if __name__ == '__main__':
    print generate_uuid()
    is_valid = validate_email("edison.w.zhang@newegg.com", check_mx=True)
    print is_valid
