from flask import request
from pymongo import MongoClient
import hashlib, random
import crypter

def authenticate_key(req):
    try:
        if req.form['token']:
            userdb = getCollectionConnection('users')
            cursor = userdb.find({'token':req.form['token']})
            return cursor[0]['_id']
        else:
            return
    except Exception as e:
        print(e)
        return
    
def easy_token():
    return (''.join([hashlib.sha224( str(random.getrandbits(256)).encode('utf_8') ).hexdigest() for _ in range(3)]))[:128]

def hash_password(pass):
    pass_len = len(pass)
    if type(password) is str and (pass_len>7 and pass_len<64) and re.match(r"[a-zA-Z0-9_@#$%^&]",password):
        # hash password and return
        return pwd_context.encrypt(pass)