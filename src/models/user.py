from mongoengine import *

class AccountUser(Document):
    email = EmailField(required=True,unique=True)
    first_name = StringField(max_length=50,required=True)
    last_name = StringField(max_length=50,required=True)
    password = StringField(max_length=50,required=True)
    token = StringField(min_length=128,max_length=128,required=True)
    