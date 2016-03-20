from mongoengine import *

class HouseholdUser(EmbeddedDocument):
    email = EmailField(required=True,unique=True)
    access_level = IntField(min_value=0,max_value=1,default=0)

class Household(Document):
    owner = EmailField(required=True) # authenticate against request token
    name = StringField(min_length=8,max_length=64,required=True)
    users = ListField(EmbeddedDocumentField(HouseholdUser))