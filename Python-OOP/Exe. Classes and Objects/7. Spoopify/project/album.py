from song import *


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

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

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            for sng in self.songs:
                if sng.name == song_name:
                    self.songs.remove(sng)
                    return f"Removed song {song_name} from album {self.name}."
                else:
                    return "Song is not in the album."


    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        sng_details = ""
        for sng in self.songs:
            sng_details += f"{sng.get_info()}\n"
        return f"Album {self.name}\n" + sng_details


