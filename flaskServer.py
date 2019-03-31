import os
from flask import request, Flask, jsonify
from flask_cors import CORS, cross_origin
from backend.eventClasses import eventList
from backend.userClass import userList

server = Flask(__name__)
cors = CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'
userL = userList()
eventL = eventList()

uFile = os.path.isfile('backend/users.txt')
eFile = os.path.isfile('backend/events.txt')
if uFile:
    pass
    f = open('backend/users.txt',"r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line.isspace():
            continue
        line = line.split("/")
        if len(line) < 3:
            userL.addOldUser(line[0],line[1],[])
        else:
            events = line[2].split(",")
            userL.addOldUser(line[0],line[1],events)
if eFile:
    pass
    f = open('backend/events.txt',"r")
    lines = f.readlines()
    f.close()
    for line in lines[1:]:
        if line.isspace():
            continue
        line = line.split("/")
        population = line[3].split(',')
        tags = line[4].split(',')
        if len(line)<8:
            eventL.addOldEvent(line[0],line[1],line[2],population,tags,line[5],line[6],[])
        else:
            members = line[7].split(',')
            eventL.addOldEvent(line[0],line[1],line[2],population,tags,line[5],line[6],members)
    eventL.set_eIDC(int(lines[0]))
# listeners

#@server.route('/')
#@cross_origin()
#def test():
#    return "Usage: https://github.com/SungHyunShin/Necto/blob/master/backend/README.md"

# users

# ONLY ENABLED FOR DEVELOPER TESTING
#@server.route('/users',methods=['GET'])
#def check_users():
#    return jsonify({'response':200,'message':'OK','users':userL.returnNames()})

@server.route('/users',methods=['POST'])
def add_user():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if userL.addUser(request.json['username'],request.json['password']):
        userL.writeUserInfo()
        return jsonify({'response':200,'message':'OK','username':request.json['username']})
    return jsonify({'response':400,'message':'username exists'})

@server.route('/users/<username>',methods=['PUT'])
def check(username):
    if not request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if userL.checkUserPW(username,request.json['password']):
        return jsonify({'response':200,'message':'login correct'})
    return jsonify({'response':400,'message':'login incorrect'})

@server.route('/users/<username>',methods=['POST'])
def update(username):
    if not request.json or not 'password' in request.json or 'newPW' not in request.json and 'newUser' not in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if 'newPW' in request.json:
        if userL.updatePassword(username,request.json['password'],request.json['newPW']):
            userL.writeUserInfo()
            return jsonify({'response':200,'message':'OK'})
        return jsonify({'response':400,'message':'permission denied'})
    if 'newUser' in request.json:
        if userL.updateUsername(username,request.json['newUser'],request.json['password']):
            userL.writeUserInfo()
            return jsonify({'response':200,'message':'OK'})
        return jsonify({'response':400,'message':'permission denied'})

@server.route('/users/<username>',methods=['DELETE'])
def remove_user(username):
    if not request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if userL.removeUser(username,request.json['password']):
        userL.writeUserInfo()
        return jsonify({'response':200,'message':'OK'})
    return jsonify({'response':400,'message':'permission denied'})


# events
# GET /events
@server.route('/events', methods=['GET'])
def get_events():
    return jsonify({'response':200,'message':'OK','events': eventL.jsonList()})

# PUT /events
@server.route('/events', methods=['PUT'])
def find_tags():
    if not request.json:
        return jsonify({'response':400,'message':'missing request'})
    if not 'tags' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if 'all' in request.json['tags']:
        return jsonify({'response':200,'message':'OK','events': eventL.jsonList()})
    eventFound = eventL.findTags(request.json['tags'])
    return jsonify({'response':200,'message':'OK','events':eventFound})

# POST /events
@server.route('/events', methods=['POST'])
def create_event():
    # wrong response, return error code 400
    if not request.json or not 'name' in request.json or not 'location' in request.json or not 'population' in request.json or not 'tags' in request.json or not 'description' in request.json or not 'ownerName' in request.json:
        response = jsonify({'response':400,'message':'missing parameters'})
        return response
    if not userL.checkUser(request.json['ownerName']):
        response = jsonify({'response':400,'message':'owner does not exist'})
        return response
    returnD = dict()
    returnD['response']=200
    returnD['message']='OK'
    eID = eventL.addEvent(request.json['name'],request.json['location'],request.json['population'],request.json['tags'],request.json['ownerName'],request.json['description'])
    returnD['eventID'] = eID
    eventL.writeEventInfo()
    response =  jsonify(returnD)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DELETE /events
@server.route('/events',methods=['DELETE'])
def reset_eventList():
    if not request.json or not 'ownerName' in request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if request.json['ownerName'] != 'admin' or not userL.checkUserPW('admin',request.json['password']):
        return jsonify({'response':400,'message':'request denied'})
    eventL.resetList()
    eventL.writeEventInfo()
    return jsonify({'response':200,'message':'OK'})

# GET /events/eventID
@server.route('/events/<int:event_ID>',methods=['GET'])
def find_event(event_ID):
    search = eventL.eventJson(event_ID)
    if search == None:
        return jsonify({'response':404,'message':'EventID '+str(event_ID)+' not found'})
    else:
        return jsonify({'response':200,'message':'OK','event':search})

# POST /events/eventID
@server.route('/events/<int:eventID>', methods=['POST'])
def update_event(eventID):
    # wrong response, return error code 400
    if not request.json or not 'name' in request.json or not 'location' in request.json or not 'population' in request.json or not 'tags' in request.json or not 'description' in request.json or not 'ownerName' in request.json or not 'username' in request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    returnD = dict()
    new = eventL.findEvent(eventID)
    if new == None:
        return jsonify({'response':404,'message':'event '+str(eventID)+' not found'})
    if not userL.checkUser(request.json['ownerName']):
        return jsonify({'response':404,'message':'new owner '+request.json['ownerName']+' not found'})
    if eventL.checkOwner(eventID,request.json['username']) and userL.checkUserPW(eventL.getOwner(eventID),request.json['password']):
        eid = eventL.updateEvent(eventID,request.json['name'],request.json['location'],request.json['population'],request.json['tags'],request.json['ownerName'],request.json['description'])
        if eid == None:
            returnD['response']= 400
            returnD['message']='didn\'t update'
        else:
            eventL.writeEventInfo()
            returnD['response']=200
            returnD['message']='OK'
        returnD['eventID']=eventID
    else:
        returnD['response'] = 400
        returnD['message'] = 'Permission denied'
    return jsonify(returnD)

# DELETE /events/eventID
@server.route('/events/<int:eventID>', methods=['DELETE'])
def remove_event(eventID):
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if eventL.checkOwner(eventID,request.json['username']) and userL.checkUserPW(eventL.getOwner(eventID),request.json['password']):
        eventL.deleteEvent(eventID)
        eventL.writeEventInfo()
        return jsonify({'response':200,'message':'OK'})
    else:
        return jsonify({'response':400,'message':'Permission denied'})

# main run server
if __name__ == '__main__': 
    server.run(debug=True)