_Copy this recipe template to design and create a database table from a specification._

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone



## 1. Extract nouns from the user stories or specification

# Request:
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing



# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

Your test should assert that the new album is present in the list of records returned by GET /albums (you will also need to test drive this route!).
```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.
```

```
Nouns:

album, title, release year, artist_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| albums                | id, title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```


# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

# Request:
POST /albums



# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

Your test should assert that the new album is present in the list of records returned by GET /albums (you will also need to test drive this route!).

## 1. Design the Route Signature

POST /artists
name :string
genre: string

_Include the HTTP method, the path, and any query or body parameters._

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
GET /artists

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._
POST /artists
Name: Taylor Swift
Genre: Pop
expected response 200 ok

no content

GET /artists
expected response 200 ok

Artists('Taylor Swift', 'pop')



POST /al
expected response 400 bad request

"you need to submit a title, release_year and artist_id"



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

```python
"""
GET /artists
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_artists(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == Artist(1,'Pixies', 'Rock'), 
                                            Artist(2,'ABBA', 'Pop'),
                                            Artist(3,'Taylor Swift','Pop')
                                            Artist(4, 'Nina Simone', 'Jazz')

"""
POST/artists
 
"""
def test_post_artist(web_client):
    response = web_client.post('/artist', data={'title': 'Test title', 'genre': 'indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == Artist(5,Test title, 'indie')
```

