from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/")
def root():
    json_thing = {'status':'success','location':'/'}
    return json.JSONEncoder().encode(json_thing)
    #return json.dumps()

@app.route("/Brandon")
def helloBrandon():
    return "Hello Brandon!"

@app.route("/hello")
def helloTo():
    name = request.args.get('name', '')
    if not name:
        return "No name was passed"
    # query database for `name`
    list_of_names = ['tom','chase','dan','brandon']
    if name in list_of_names:
        return "Hello {}".format(name)
    else:
        return "You are not in the system"

@app.route("/register")
def register():
    username = request.args.get('user', '')
    password = request.args.get('pass', '')
    
    print("Username={} Password={}".format(username,password))
    
    if not username or not password:
        return "Failed to register"
    
    if len(password)>=8:
        print("Password passed")
        userdb[username]=password
        return "Registered as {}".format(username)
    
@app.route("/signin")
def signin():
    username = request.args.get('user', '')
    password = request.args.get('pass', '')
    
    if not username or not password:
        return "Failed to sign in"
    
    if(userdb[username]==password):
        return "You have been signed in"
    else:
        return "Failed password verification"
    
if __name__ == "__main__":
    app.run()