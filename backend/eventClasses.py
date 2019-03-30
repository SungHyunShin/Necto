# Class for list of events
class eventList:
    # private variables
    _eList = []
    _eIDC = 0
    def __init__(self):
        _eIDC = 0
        _eList = []
    # returns entire movie list in json format
    def jsonList(self):
        jsonL = []
        for event in self._eList:
            jsonL.append(event.jsonEvent())
        return jsonL
    def addEvent(self,event):
        self._eIDC += 1
        event.set_eventID(self._eIDC)
        self._eList.append(event)
        return self._eIDC
        
    def findEvent(self,eID):
        found = False
        for event in self._eList:
            if event.get_eventID() == eID:
                return event
        return None
    def deleteEvent(self,eID):
        for event in self._eList:
            if event.get_eventID() == eID:
                self._eList.remove(event)
    def resetList(self):
        self._eList = []
        return
    def findTags(self,tags):
        returnL = []
        for event in self._eList:
            eTags = event.get_tags()
            for tag in tags:
                if tag in eTags and event not in returnL:
                    returnL.append(event)
        return returnL



# class for events
class event:
    # private variables
    _name = ""
    _eventID = -1
    _location = ""
    _population = (-1,-1)
    _tags = []
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
    def jsonEvent(self):
        returnD = dict()
        returnD ['name']=self._name
        returnD['eventID']=self._eventID
        returnD['location']=self._location
        returnD['population']=[self._population[0],self._population[1]]
        returnD['tags'] =self._tags
        return returnD
    def update(self,event):
        self._name = event.get_name()
        self._location = event.get_location()
        self._population = event.get_population()
        self._tags = event.get_tags()