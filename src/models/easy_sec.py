from flask import request
from pymongo import MongoClient
import hashlib, random
import re

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

def hash_password(password):
    pass_len = len(password)
    if type(password) is str and (pass_len>7 and pass_len<64) and re.match(r"[a-zA-Z0-9_@#$%^&]",password):
        return hashlib.sha512(password.encode('utf_8')).hexdigest()
    else:
        return
        
def check_password(password, hash_pw):
    return (hash_password(password)==hash_pw)