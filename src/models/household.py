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
        				self.users[user] = auth_level
        	if not services:
        		self.services = {"wemo": False, "hue": False, "lockitron": False, "nest": False}
    
    def set_name(self, name=""):
    	if validate_name(name):
    		self.name = name
    		return True
    	else:
    		return False
        
    def set_user(self, user_id=""):
    	if not user_id in self.users:
    		self.users[user_id] = 0
            
    def set_auth(self, user_id="", auth_level=0):
    	if user_id in self.users:
    		self.users[user_id] = auth_level
    		return True
    	return False
    
    def set_service(self, service="", enable=False):
        if service in self.services:
            self.services[service]=enable
            return True
        return False
    
    def get_name(self):
    	try:
    		return self.name
    	except:
    		return

    def get_users(self):
        try:
            return self.users
        except:
            return {}
        
    def get_services(self):
        try:
            return self.services
        except:
            return {}