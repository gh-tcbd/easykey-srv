from flask import Flask
from flask import request
from pymongo import MongoClient
from models import user
from models import household
from models import device
from models import easy_sec
from db import mdb
import json
import hashlib


app = Flask(__name__)

# ROOT TEST
@app.route('/')
def root():
    rootjson = {'status':'success','location':'/','developers':['tom','chase','brandon','dan']}
    #return json.JSONEncoder().encode(rootjson)
    return json.dumps(rootjson)


# REGISTER 
@app.route('/register', methods=['POST'])
def register():
    r_email = request.form['email']
    r_password = request.form['password']
    r_first_name = request.form['first_name']
    r_last_name = request.form['last_name']
    print('Email:{}\tPass:{}\tFirst:{}\tLast:{}'.format(r_email,r_password,r_first_name,r_last_name))
    if not (r_email and r_password and r_first_name and r_last_name):
        return json.loads({'status':'failure'})
    print('Token generating')
    u_token = easy_sec.easy_token()
#    print('Hashing password')
#    u_hash = easy_sec.hash_password(r_password)
    print('Generating User')
    new_user = user.AccountUser(email=r_email,
                       password=r_password,
                       token=u_token,
                       first_name=r_first_name,
                       last_name=r_last_name)
    try:
        print('Validated user info')
        print('Connecting to database')
        userColl = mdb.getCollectionConnection('user')
        print('Inserted document')
        result = userColl.insert_one(new_user.json())
        return json.loads({'token':new_user.get_token()})
    except Exception as e:
        return json.loads({'status':str(e)})
    #return access token
    

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    r_email = request.form['email']
    r_password = request.form['password']
    if email and password:
        #connect('users',host='gh-tcbd.dyladan.me',port=27019)
        userColl = mdb.getCollectionConnection('user')
        user = User.objects(email=r_email,password=r_password)
        try:
            return json.dumps({'token':user.token,
                               'first_name':user.first_name,
                               'last_name':user.last_name})
        except Exception as e:
            print(e)
            return
    #return access token
    

# HOUSEHOLD [ GET / POST ]
@app.route('/household', methods=['POST','GET'])
def household():
    error = None
    
    # insert data into the database for household
    if request.method is 'POST':
        # get user id based off access key
        # returns empty value if no key found in system
        userid = easy_sec.authenticate(request.form)
        if userid:
            # test data for consistency
            if validate_household(request.form):
                household_db = mdb.getInstance()['household']
                result = household_db.insert_one(
                    {
                        'location':{
                            'address':request.form['address'],
                            'state':request.form['state'],
                            'zipcode':request.form['zipcode']
                        },
                        'name':request.form['name'],
                        'user':request.form['user']
                    })
                return "Id for household is {}".format(result.inserted_id)
            else:
                return "Data invalid"
        else:
            return "Access key invalid"
    
    # retrieve data from the database for households
    elif request.method is 'GET':
        userid = easy_sec.authenticate(request.form)
    
if __name__ == '__main__':
    app.run()