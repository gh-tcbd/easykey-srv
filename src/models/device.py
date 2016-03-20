from mongoengine import * 

class APIDevice(Document):
    api_key = StringField(max_length=128)
    email = EmailField()
    password = StringField(max_length=128)
    meta = {'allow_inheritance': True}
    
class NestDevice(APIDevice):
    type = ""
    
class WemoDevice(APIDevice):
    type = ""
    
class HueDevice(APIDevice):
    type = ""
    
class LinkitronDevice(APIDevice):
    type = ""
    