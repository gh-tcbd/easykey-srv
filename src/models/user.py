import re
from . import model_eval
from . import easy_sec

class AccountUser():
    def __init__(self,email="",first_name="",last_name="",password="",token=""):
        if model_eval.validate_email(email) \
            and model_eval.validate_name(first_name) \
            and model_eval.validate_name(last_name) \
            and model_eval.validate_password(password):
                    self.email=email
                    self.first_name=first_name
                    self.last_name=last_name
                    self.passhash=easy_sec.hash_password(password)
                    self.token=token
        else:
            raise Exception('Error building AccountUser')
    
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
        return json.loads(get_mongo_form)
    
    def get_mongo_form(self):
        return {
                'email':self.email,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'passhash':self.passhash,
                'token':self.token
        }
    
    def is_valid(self):
        return self.is_valid