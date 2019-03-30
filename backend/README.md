### RESTful JSON Specification
| Resources          | GET                             | PUT                                           | POST                            | DELETE           |
|--------------------|---------------------------------|-----------------------------------------------|---------------------------------|------------------|
| /users             | Get list of all usernames       |                                               | Create new user                 |                  |
| /users/:uid        |                                 | Check if username and password are valid user | Update username or password     | Delete user      |
| /events/           | Get list of all events          | Find all events with any of the tags provided | Create new event                | Reset all events |
| /events/:eID       | Return event information of eID |                                               | Update even with given eID      | Remove eID event |
