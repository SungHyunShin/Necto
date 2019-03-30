import hashlib

class userList:
    # private variables
    _uList = []
    def returnNames(self):
        u = []
        for user in self._uList:
            u.append({'name':user.get_username()})
        return u
    def checkUser(self,username):
        for user in self._uList:
            if user.get_username() == username:
                return True
        return False

    # returns user if part of list
    def findUser(self, username):
        for user in self._uList:
            if user.get_username() == username:
                return user
        return None

    def removeUser(self,username,password):
        if self.checkUserPW(username,password):
                user = self.findUser(username)
                self._uList.remove(user)
                return True
        return False
    
    def checkUserPW(self,username,password):
        for user in self._uList:
            if user.get_username() == username:
                if user.check_password(password):
                    return True
                else:
                    return False
        return False
    def addOldUser(self,username,hashedPassword):
        self._uList.append(user(username,hashedPassword))

    # adds user if not in database and returns true, returns false if already in database
    def addUser(self, username, password):
        search = self.findUser(username)
        if search == None:
            new = user(username,password)
            self._uList.append(new)
            return True
        return False
    def updateUsername(self,username,new,password):
        search = self.findUser(username)
        if search == None:
            return False
        if search.check_password(password):
            search.set_username(new)
            return True
        return False
    def updatePassword(self,username,password,new):
        search = self.findUser(username)
        if search == None:
            return False
        return search.update_password(password,new)
            
class user:
    _username = ""
    _password = ""
    _events = []
    def __init__(self,username,password):
        self._username = username
        self._password = hashlib.sha3_512(password.encode()).hexdigest()
    def get_username(self):
        return self._username
    def set_username(self, username):
        self._username = username
    def get_password(self):
        return self._password
    def set_password(self, password):
        self._password = hashlib.sha3_512(password.encode()).hexdigest()
    def set_pass_H(self,hashedPassword):
        self._password = hashedPassword
    def update_password(self, password,new):
        if self._password == hashlib.sha3_512(password.encode()).hexdigest():
            self._password = hashlib.sha3_512(new.encode()).hexdigest()
            return True
        return False
    def check_password(self,password):
        if self._password == hashlib.sha3_512(password.encode()).hexdigest():
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