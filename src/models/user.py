import re
import hashlib, uuid

#class AccountUser(Document):
#    email = EmailField(required=True,unique=True)
#    first_name = StringField(max_length=50,required=True)
#    last_name = StringField(max_length=50,required=True)
#    hash = StringField(max_length=50,required=True)
#    token = StringField(min_length=128,max_length=128,required=True)

class AccountUser():
    def __init__(self,email="",first_name="",last_name="",hash="",token=""):
        if email and first_name and last_name and passhash and token:
            if validate_email(email) 
            and validate_name(first_name) 
            and validate_name(last_name) 
            and validate_passhash(passhash):
                    self.email=email
                    self.first_name=first_name
                    self.last_name=last_name
                    self.passhash=passhash
                    self.token=token
                    return True
        return False
    
    def get_email(self):
        try:
            return self.email
        except:
            return None
        
    def get_first_name(self):
        try:
            return self.first_name
        except:
            return None
        
    def get_last_name(self):
        try:
            return self.last_name
        except:
            return None
        
    def get_hash(self):
        try:
            return self.passhash
        except:
            return None
        
    def get_token(self):
        try:
            return self.token
        except:
            return None
        
    def get_json(self):
        return json.loads({
                'email':self.email,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'passhash':self.passhash,
                'token':self.token
            })