class Song:
    """
    Represents a single song and maintains global insights
    across all song instances (total count, genres, artists, etc.).
    """

    # Class attributes — shared across all instances
    count = 0            # Total number of Song objects created
    genres = []          # Unique list of all genres
    artists = []         # Unique list of all artists
    genre_count = {}     # Number of songs per genre  e.g. {"Rap": 5, "Rock": 1}
    artist_count = {}    # Number of songs per artist e.g. {"Beyonce": 17, "Jay-Z": 40}

    def __init__(self, name, artist, genre):
        """
        Initializes a Song instance and triggers all class-level
        tracking methods so global stats are always up to date.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level stats whenever a new Song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total number of songs by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds a genre to the genres list only if it isn't already
        present, ensuring the list contains only unique genres.
        """
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds an artist to the artists list only if it isn't already
        present, ensuring the list contains only unique artists.
        """
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Increments the count for the given genre in genre_count.
        If the genre doesn't exist yet, it is added with a value of 1.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Increments the count for the given artist in artist_count.
        If the artist doesn't exist yet, it is added with a value of 1.
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
