from lib.album_repository import AlbumRepository
from lib.album import Album
"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/record_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, 'Take Care', 2011, 1)]

def test_create_album(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")

    repository = AlbumRepository(db_connection) 
    albums = Album(None, 'test title', '2000', 1)
    repository.create(albums)

    assert repository.all() == [
        Album(1, 'Take Care', 2011, 1),
        Album(2, 'test title', 2000, 1)]