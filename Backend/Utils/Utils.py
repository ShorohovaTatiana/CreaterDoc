from flask import Blueprint
from Backend.entities.User import User
import hashlib

util_app = Blueprint('util_app', __name__)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, User):
        return obj.__dict__

    raise TypeError("Type %s not serializable" % type(obj))


def get_hash(str):
    hash_object = hashlib.md5(str.encode('utf-8'))
    return hash_object.hexdigest()





