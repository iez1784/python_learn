
# generate rramdom uuid
import uuid
from validate_email import validate_email


def generate_uuid():
    return str(uuid.uuid4())



if __name__ == '__main__':
    print generate_uuid()
    is_valid = validate_email("edison.w.zhang@newegg.com", check_mx=True)
    print is_valid
