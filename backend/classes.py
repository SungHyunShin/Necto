# Class for list of events
class eventList:
    # private variables
    _eList = []
    # returns entire movie list in json format
    def jsonList(self):
        jsonL = []
        for event in self._eList:
            eventD = dict()
            eventD['name'] = event.get_name()
            eventD['eventID'] = event.get_eventID()
            eventD['location'] = event.get_location()
            eventD['population'] = event.get_population()
            eventD['tags'] = event.get_tags()
            jsonL.append(eventD)
        return jsonL
    def addEvent(self,event):
        self._eList.append(event)
    def findEvent(self,eID):
        found = False
        for event in self._eList:
            if event.get_eventID() == eID:
                found = True
                eventDict = {}
                eventDict['name'] = event.get_name()
                eventDict['eventID'] = event.get_eventID()
                eventDict['location'] = event.get_location()
                p = event.get_population()
                eventDict['population'] = [p[0],p[1]]
                eventDict['tags'] = event.get_tags()
                return eventDict
        return None

# class for events
class event:
    # private variables
    _name = ""
    _eventID = -1
    _location = ""
    _population = (-1,-1)
    _tags = [];
    # functions to access private variables
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name
    def get_eventID(self):
        return self._eventID
    def set_eventID(self,eventID):
        self._eventID = eventID
    def get_location(self):
        return self._location
    def set_location(self,location):
        self._location = location
    def get_population(self):
        return self._population
    def set_population(self,population):
        self._population = population
    def get_tags(self):
        return self._tags
    def set_tags(self,tags):
        self._tags = tags