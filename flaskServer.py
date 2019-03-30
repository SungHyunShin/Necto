from flask import request, Flask, jsonify

from backend.eventClasses import eventList
from backend.userClass import userList

server = Flask(__name__)

userL = userList()
eventL = eventList()
# listeners

@server.route('/')
def test():
    return "Usage: https://github.com/SungHyunShin/Necto/blob/master/backend/README.md"

# users
@server.route('/users',methods=['GET'])
def check_users():
    return jsonify({'response':200,'message':'OK','users':userL.returnNames()})

@server.route('/users',methods=['POST'])
def add_user():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if userL.addUser(request.json['username'],request.json['password']):
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
            return jsonify({'response':200,'message':'OK'})
        return jsonify({'response':400,'message':'permission denied'})
    if 'newUser' in request.json:
        if userL.updateUsername(username,request.json['newUser'],request.json['password']):
            return jsonify({'response':200,'message':'OK'})
        return jsonify({'response':400,'message':'permission denied'})

@server.route('/users/<username>',methods=['DELETE'])
def remove_user(username):
    if not request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if userL.removeUser(username,request.json['password']):
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
    if not request.json or not 'tags' in request.json:
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
        return jsonify({'response':400,'message':'missing parameters'})
    if not userL.checkUser(request.json['ownerName']):
        return jsonify({'response':400,'message':'owner does not exist'})
    returnD = dict()
    returnD['response']=200
    returnD['message']='OK'
    eID = eventL.addEvent(request.json['name'],request.json['location'],request.json['population'],request.json['tags'],request.json['ownerName'],request.json['description'])
    returnD['eventID'] = eID
    return jsonify(returnD)

# DELETE /events
@server.route('/events',methods=['DELETE'])
def reset_eventList():
    if not request.json or not 'ownerName' in request.json or not 'password' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    if request.json['ownerName'] != 'admin' or not userL.checkUserPW('admin',request.json['password']):
        return jsonify({'response':400,'message':'request denied'})
    eventL.resetList()
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
        return jsonify({'response':200,'message':'OK'})
    else:
        return jsonify({'response':400,'message':'Permission denied'})

# main run server
if __name__ == '__main__':
    # create classes

    server.run(debug=True)