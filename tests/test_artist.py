from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Artist(1, 'test artist', 'indie')
    assert artist.id == 1
    assert artist.name == "test artist"
    assert artist.genre == "indie"

"""
We can format albums to strings nicely
"""
def test_artist_format_nicely():
    artist = Artist(1, 'test artist', 'indie')
    assert str(artist) == "Artist(1, test artist, indie)"
    