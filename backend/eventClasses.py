import os
# Class for list of events
class eventList:
    # private variables
    _eList = []
    _eIDC = 0
    def __init__(self):
        _eIDC = 0
        _eList = []
    def writeEventInfo(self):
        f = open('backend/events.txt',"w")
        f.write(str(self._eIDC)+'\n')
        for event in self._eList:
            f.write(str(event.get_eventID())+'/'+event.get_name()+'/'+event.get_location()+'/'+str(event.get_population()[0])+','+str(event.get_population()[1])+'/'+','.join(event.get_tags())+'/'+event.get_ownerName()+'/'+event.get_description()+'/'+",".join(event.get_members()))
            f.write('\n')
    # returns entire movie list in json format
    def jsonList(self):
        jsonL = []
        for event in self._eList:
            jsonL.append(event.jsonEvent())
        return jsonL
    def set_eIDC(self,eIDC):
        self._eIDC = eIDC
    def addEvent(self,name,location,population,tags,ownerName,description):
        self._eIDC += 1
        new = event()
        new.set_eventID(self._eIDC)
        new.set_name(name)
        new.set_location(location)
        new.set_population((population[0],population[1]))
        new.set_tags(tags)
        new.set_description(description)
        new.set_ownerName(ownerName)
        self._eList.append(new)
        return self._eIDC
    def addOldEvent(self,eventID,name,location,population,tags,ownerName,description,members):
        new = event()
        new.set_eventID(int(eventID))
        new.set_name(name)
        new.set_location(location)
        new.set_population((int(population[0]),int(population[1])))
        new.set_tags(tags)
        new.set_description(description)
        new.set_ownerName(ownerName)
        new.add_members(members)
        self._eList.append(new)
        return self._eIDC
    def updateEvent(self,eID,name,location,population,tags,ownerName,description):
        for event in self._eList:
            if event.get_eventID() == eID:
                new = event
                new.set_name(name)
                new.set_location(location)
                new.set_population((population[0],population[1]))
                new.set_tags(tags)
                new.set_description(description)
                new.set_ownerName(ownerName)
                event.update(new)
                return eID
        return None
    def checkOwner(self,eID,name):
        for event in self._eList:
            if event.get_eventID() == eID:
                return event.isowner(name)
    def getOwner(self,eID):
        for event in self._eList:
            if event.get_eventID() == eID:
                return event.get_ownerName()
    def findEvent(self,eID):
        for event in self._eList:
            if event.get_eventID() == eID:
                return eID
        return None
    def eventJson(self,eID):
        for event in self._eList:
            if event.get_eventID() == eID:
                return event.jsonEvent()
        return None
    def deleteEvent(self,eID):
        for event in self._eList:
            if event.get_eventID() == eID:
                self._eList.remove(event)
    def resetList(self):
        self._eList = []
        return
    def findTags(self,tags):
        jsonL = []
        for event in self._eList:
            inside = False
            for tag in tags:
                if tag in event.get_tags():
                    inside = True
            if inside:
                jsonL.append(event.jsonEvent())
        print(jsonL)
        return jsonL

# class for events
class event:
    # private variables
    _name = ""
    _eventID = -1
    _location = ""
    _population = (-1,-1)
    _tags = []
    _description = ""
    _ownerName = ""
    _members = []
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
    def get_description(self):
        return self._description
    def set_description(self,desc):
        self._description = desc
    def get_ownerName(self):
        return self._ownerName
    def set_ownerName(self,name):
        self._ownerName = name
    def get_members(self):
        return self._members
    def reset_members(self):
        self._members = []
    def add_member(self,member):
        self._members.append(member)
    def add_members(self,members):
        self._members = self._members + members

    def isowner(self,username):
        if self._ownerName == username:
            return True
        else:
            return False

    def jsonEvent(self):
        returnD = dict()
        returnD['name']=self._name
        returnD['eventID']=self._eventID
        returnD['location']=self._location
        returnD['population']=[self._population[0],self._population[1]]
        returnD['tags'] =self._tags
        returnD['description'] = self._description
        returnD['ownerName'] = self._ownerName
        returnD['members'] = self._members
        return returnD

    def update(self,event):
        self._name = event.get_name()
        self._location = event.get_location()
        self._population = event.get_population()
        self._tags = event.get_tags()
        self._description = event.get_description()
        self._ownerName = event.get_ownerName()
        self._members = event.get_members()