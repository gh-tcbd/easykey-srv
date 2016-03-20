class Household():
    def __init__(self,name="",users=None,services=None):
        if name:
        	if not validate_name(name):
        		# Provide generic name if the field doesn't pass validation
        		self.name = "New Location"
        	if not users:
        		self.users = {}
        	else:
        		# Iterate through users dictionary
        		# if the user doesn't pass validation skip (TODO: Add feedback or ignore silently?)
        		# otherwise continue.
        		for user, auth_level in users:
        			if validate_email(user):
        				users[user] = auth_level
        	if not services:
        		self.services = {"wemo": False, "hue": False, "lockitron": False, "nest": False}
            return True
        return False
    def get_name(self):
    	try:
    		return self.name
    	except:
    		return None
   	def get_users(self):
   		try:
   			return self.users
   		except:
   			return {}
   	def get_services:
   		try:
   			return self.services
   		except:
   			return {}