class Song:
    max_rating = 5
    min_rating = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self):
        if self.rating < Song.min_rating:
            self.rating = Song.min_rating
        elif self.rating > Song.max_rating:
            self.rating = Song.max_rating
