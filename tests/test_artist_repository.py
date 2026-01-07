from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new BookRepository

    artists = repository.all() # Get all albums

    # Assert on the results
    assert artists == [
        Artist(1,'Pixies', 'Rock'), 
        Artist(2,'ABBA', 'Pop'),
        Artist(3,'Taylor Swift','Pop'),
        Artist(4, 'Nina Simone', 'Jazz')]
    
def test_create_artist(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")

    repository = ArtistRepository(db_connection) 
    artist = Artist(None, 'test artist', 'indie')
    repository.create(artist)

    assert repository.all() == [
        Artist(1,'Pixies', 'Rock'), 
        Artist(2,'ABBA', 'Pop'),
        Artist(3,'Taylor Swift','Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'test artist', 'indie')]