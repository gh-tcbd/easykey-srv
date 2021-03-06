import re

def validate_email(email):
    print('Validating email')
    return re.match(r"[^@]+@[^@]+\.[^@]+",email)
    
def validate_name(name):
    name_len = len(name)
    print('Validating name {}'.format(name))
    return (type(name) is str and (name_len>1 and name_len<50) and re.match(r"[a-zA-Z]",name))

def validate_password(password):
    pass_len = len(password)
    print('Validating password')
    return (type(password) is str and (pass_len>1 and pass_len<50) and re.match(r"[a-zA-Z0-9_@#$%^&!]",password))