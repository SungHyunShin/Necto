class userList:
    # private variables
    _uList = []

    # returns user if part of list
    def findUser(self, username):
        for user in self._uList:
            if user.get_username() == username:
                return user
        return None

    def removeUser(self,username,password):
        for user in self._uList:
            if user.get_username() == username and user.get_password() == pasword:
                self._uList.remove(user)
                return True
        return False
    
    # adds user if not in database and returns true, returns false if already in database
    def addUser(self, username, password):
        search = self.findUser(username)
        if search == None:
            new = user(username,password)
            _uList.append(user)
            return True
        return False
            
class user:
    _username = ""
    _password = ""
    _events = []
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def get_username(self):
        return self._username
    def set_username(self, username):
        self._username = username
    def get_password(self):
        return self._password
    def set_password(self, password):
        self._password = password
    def update_password(self, password,new):
        if self._password == password:
            self._password = new
            return True
        return False
    def get_events(self):
        return self._events
    def set_events(self, eventsJoined):
        self._events = eventsJoined
    def add_membership(self,eID):
        self._events.append(eID)
    def check_ownership(self,eID):
        if eID in self._eventsO:
            return True
        return False