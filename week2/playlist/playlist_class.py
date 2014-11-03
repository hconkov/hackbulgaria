from song_class import *


class Playlist:

    def __init__(self, name):
        self.songs = []
        self.name = name

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        while song in self.songs:
            self.songs.remove(song)

    def total_length(self):
        totallen = 0
        for song in self.songs:
            totallen += int(song.length)
        return totallen

    def remove_disrated(self, rating):
        for song in self.songs:
            if song.rating < rating:
                self.songs.remove(song)

    def remove_bad_quality(self, quality):
        for song in self.songs:
            if song.bitrate < quality:
                self.songs.remove(song)

    def show_artists(self):
        artists = []
        for song in self.songs:
            if song.artist not in artists:
                artists.append(song.artist)
        return artists
