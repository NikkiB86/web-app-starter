# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


    # File: tests/test_app.py

# Note: you will need to do this in the starter codebase.

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'


def test_get_and_add_name(web_client):
    response = web_client.get('/names?add=Eddie', data={'name': 'Julia,Alice,Karim'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Eddie'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

# To run these tests (ensure your virtual environment is active first):
# ; pytest tests/test_app.py

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
POST/sort-name
names=Joe,Alice,Zoe,Julia,Kieran
expected response: 200 0K
Alice,Joe,Julia,Kieran,Zoe
"""

def test_post_sortnames(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

def test_post_sortname_if_last_letter_differs(web_client):
    response = web_client.post('/sort-names', data={'names': 'Anna,Annnb,Annnd'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Anna,Annnb,Annnd'

def test_post_sortname_no_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'you did not submit any names'


def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post('/albums', data={'title': 'Views', 'release_year': '2016' , 'artist_id' : '1'})
    assert post_response.status_code ==200
    assert post_response.data.decode('utf-8') == ""

    # get_response = web_client.get('/albums')
    # assert get_response.status_code ==200
    # assert get_response.data.decode('utf-8') == " Album(1, Take Care, 2011, 1),  Album(2, Views, 2016, 1)"

def test_get_album(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get('/albums', data={'title': 'Views', 'release_year': '2016' , 'artist_id' : '1'})
    assert response.status_code ==200
    assert response.data.decode('utf-8') == ""\
    " Album(1, Take Care, 2011, 1)"
    
def test_post_artist(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/artists', data={'name': 'wild nothing', 'genre': 'indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

    response = web_client.get('/artists')
    assert response.status_code ==200
    assert response.data.decode('utf-8') == ('Pixies, ABBA, Taylor Swift, Nina Simone, wild nothing')

    

def test_get_artist(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artists')
    assert response.status_code ==200
    assert response.data.decode('utf-8') == ('Pixies, ABBA, Taylor Swift, Nina Simone')


#    POST /albums
# title: Views
# release_year: 2016
# artist_id :1
# expected response 200 ok

# no content

# GET /albums
# expected response 200 ok

# Album(1, 'Take Care', 2011, 1)
# Album(2, 'Views', 2016, 1)


# POST /albums
# expected response 400 bad request

# "you need to submit a title, release_year and artist_id"

# === End Example Code ===
