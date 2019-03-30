from flask import request,Flask, jsonify

from eventClasses import event,eventList
from userClass import user,userList

server = Flask(__name__)

# listeners

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
    eventsReturn = []
    for event in eventFound:
        eventsReturn.append(event.jsonEvent())
    return jsonify({'response':200,'message':'OK','events':eventsReturn})

# POST /events
@server.route('/events', methods=['POST'])
def create_event():
    # wrong response, return error code 400
    if not request.json or not 'name' in request.json or not 'location' in request.json or not 'population' in request.json or not 'tags' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    returnD = dict()
    returnD['response']=200
    returnD['message']='OK'
    new = event()
    new.set_name(request.json['name'])
    new.set_location(request.json['location'])
    new.set_population((request.json['population'][0],request.json['population'][1]))
    new.set_tags(request.json['tags'])
    eID = eventL.addEvent(new)
    returnD['eventID'] = eID
    return jsonify(returnD)

# DELETE /events
@server.route('/events',methods=['DELETE'])
def reset_eventList():
    eventL.resetList()
    return jsonify({'response':200,'message':'OK'})

# GET /events/eventID
@server.route('/events/<int:event_ID>',methods=['GET'])
def find_event(event_ID):
    search = eventL.findEvent(event_ID)
    if search == None:
        return jsonify({'response':404,'message':'EventID '+str(event_ID)+' not found'})
    else:
        return jsonify({'response':200,'message':'OK','event':search.jsonEvent()})

# POST /events/eventID
@server.route('/events/<int:eventID>', methods=['POST'])
def update_event(eventID):
    # wrong response, return error code 400
    if not request.json or not 'name' in request.json or not 'location' in request.json or not 'population' in request.json or not 'tags' in request.json:
        return jsonify({'response':400,'message':'missing parameters'})
    returnD = dict()
    returnD['response']=200
    returnD['message']='OK'
    new = eventL.findEvent(eventID)
    if new == None:
        return jsonify({'response':404,'message':'event '+str(eventID)+' not found'})
    new.set_name(request.json['name'])
    new.set_location(request.json['location'])
    new.set_population((request.json['population'][0],request.json['population'][1]))
    new.set_tags(request.json['tags'])
    returnD['eventID']=eventID
    return jsonify(returnD)

# DELETE /events/eventID
@server.route('/events/<int:eventID>', methods=['DELETE'])
def remove_event(eventID):
    eventL.deleteEvent(eventID)
    return jsonify({'response':200,'message':'OK'})

# main run server
if __name__ == '__main__':
    # create classes
    userL = userList()
    eventL = eventList()
    server.run(debug=True)