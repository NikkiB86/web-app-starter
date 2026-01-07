import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
# Request:
# GET /hello?name=David

# @app.route('/hello', methods=['GET'])
# def hello():
#     name = request.args['name'] # The value is 'David'

#     # Send back a friendly greeting with the name
#     return f"Hello {name}!"

# # To make a request, run:
# # curl "http://localhost:5001/hello?name=David"

# # # Request:
# # # POST /goodbye
# # #   With body parameter: name=Alice

@app.route('/names', methods=['GET'])
def get_names():
    names = ['Julia', 'Alice', 'Karim']
    new_name = request.args.get('add')
    if new_name:
        names.append(new_name.capitalize())

    return ",".join(names)



@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"I am waving at {name}"


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # The value is 'Leo'
    message = request.form ['message'] # The value is 'Hello World'


    # Send back a fond farewell with the name
    return f'Thanks {name}, you sent this message: "{message}"'


@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text'] # The value is 'eee'
    vowels = 0
    for char in text:
        if char in "aeiou":
            vowels +=1
    return f'There are {vowels} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sortnames():
    if 'names' not in request.form:
        return "you did not submit any names", 400
    names = request.form['names'].split(",") 
    sorted_names = sorted(names)
    return ",".join(sorted_names)

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = Album(None, 
                    request.form ['title'],
                    request.form ['release_year'],
                    request.form ['artist_id'])
    repository.create(albums)
    return "", 200
        

@app.route('/albums', methods=['GET'])
def GET_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return "\n".join(
    f" {album}" for album in repository.all())

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre']
    )

    repository.create(artist)
    return "", 200

@app.route('/artists', methods=['GET'])
def GET_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return ", ".join(artist.name for artist in artists), 200

# # == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# # This imports some more example routes for you to see how they work
# # You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

