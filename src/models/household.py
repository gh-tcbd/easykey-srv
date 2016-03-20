#class HouseholdUser(EmbeddedDocument):
#    email = EmailField(required=True,unique=True)
#    access_level = IntField(min_value=0,max_value=1,default=0)
#
#class Household(Document):
#    owner = EmailField(required=True) # authenticate against request token
#    name = StringField(min_length=8,max_length=64,required=True)
#    users = ListField(EmbeddedDocumentField(HouseholdUser))

class Household():
    def __init__(self,name="",users=None,services=None):
        if name:
        	if not validate_name(name):
        		self.name = "New User"
        	if not users:
        		self.users = {}
        	if not services:
        		self.services = {"wemo": False, "hue": False, "lockitron": False, "nest": False}
            return True
        return False
    