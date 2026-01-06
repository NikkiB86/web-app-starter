
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._
Use this Design Recipe to test-drive a new route POST /sort-names which receives a list of names (as a comma-separated string) and return the same list, sorted in alphabetical order.

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._
# Request:
POST http://localhost:5001/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

POST/sort-name
    names: string with commas seperating name.
```
# EXAMPLE


# Home route
GET /home


# Waving route
GET /wave?name=

# Submit message route
POST /submit
  name: string
  message: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._
POST/sort-name
names=Joe,Alice,Zoe,Julia,Kieran
expected response: 200 0K
Alice,Joe,Julia,Kieran,Zoe



POST/sort-name
names=Anna,Annnb, Annnd
expected response: 200 0K
Annna,Annnb, Annnd

POST/sort-name
names= no names
expected response: invalid
you did not submit any names
```python
# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

POST/sort-name
```python
def test_post_sortname(web_client):
    response = web_client.post('/sort-name', data={'names': 'Joe', 'Alice','Zoe', 'Julia','Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'


def test_post_sortname_if_last_letter_differs(web_client):
    response = web_client.post('/sort-name', data={'names': 'Anna,Annnb,Annnd'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Anna,Annnb,Annnd'

def test_post_sortname_no_names(web_client):
    response = web_client.post('/sort-name', data={NONE})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'you did not submit any names'
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

