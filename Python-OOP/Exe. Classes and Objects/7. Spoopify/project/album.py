from song import *
class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False
        print(type(self.songs))

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
