import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email):
    
def validate_name(name):
    name_len = len(name)
    return type(name) is str and (name_len>1 and name_len<50) and re.match(r"[a-zA-Z]",name)

def validate_password(password):
    

