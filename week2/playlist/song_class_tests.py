import unittest

from song_class import Song


class TestSong(unittest.TestCase):

    def test_song_constructor(self):
        new_song = Song(
            "Fuel", "Metallica", "Reload", 5, 277, 320)
        self.assertEqual(new_song.title, "Fuel")
        self.assertEqual(new_song.artist, "Metallica")
        self.assertEqual(new_song.album, "Reload")
        self.assertEqual(new_song.rating, 5)
        self.assertEqual(new_song.length, 277)
        self.assertEqual(new_song.bitrate, 320)

if __name__ == '__main__':
    unittest.main()
