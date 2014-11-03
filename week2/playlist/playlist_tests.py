from playlist_class import Playlist
from song_class import Song
import unittest


class TestPlaylist(unittest.TestCase):

    def test_playlist_init(self):
        test_playlist = Playlist("Chalgata!")
        self.assertEqual(test_playlist.name, "Chalgata!")
        self.assertEqual(test_playlist.songs, [])

    def test_add_songs(self):
        test_playlist = Playlist("chalgata")
        song1 = Song("s", "s", "s", 1, 2, 3)
        test_playlist.add_song(song1)
        self.assertEqual(test_playlist.songs, [song1])

    def test_remove_songs(self):
        test_playlist = Playlist("chalgata")
        song1 = Song("s", "s", "s", 1, 2, 3)
        test_playlist.add_song(song1)
        self.assertEqual(test_playlist.songs, [song1])
        test_playlist.remove_song(song1)
        self.assertEqual(test_playlist.songs, [])

    def test_total_length(self):
        test_playlist = Playlist("chalgata")
        song1 = Song("s", "s", "s", 1, 2, 3)
        song2 = Song("a", "s", "s", 1, 3, 4)
        test_playlist.add_song(song1)
        test_playlist.add_song(song2)
        self.assertEqual(test_playlist.songs, [song1, song2])
        self.assertEqual(test_playlist.total_length(), 5)

    def test_disrated(self):
        test_playlist = Playlist("chalgata")
        song1 = Song("s", "s", "s", 1, 2, 3)
        test_playlist.add_song(song1)
        test_playlist.remove_disrated(2)
        self.assertEqual(test_playlist.songs, [])

    def test_bitrate(self):
        test_playlist = Playlist("chalgata")
        song1 = Song("s", "s", "s", 1, 2, 3)
        test_playlist.add_song(song1)
        test_playlist.remove_bad_quality(4)
        self.assertEqual(test_playlist.songs, [])

    def test_show_artists(self):
        test_playlist = Playlist("chalgata")
        song1 = Song("s", "s", "s", 1, 2, 3)
        test_playlist.add_song(song1)
        self.assertEqual(test_playlist.show_artists(), ["s"])

if __name__ == '__main__':
    unittest.main()
