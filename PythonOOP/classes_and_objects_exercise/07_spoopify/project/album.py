from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        # self.songs: list[Song] = []
        self.songs: list[Song] = list(songs)
        self.published: bool = False
        # for _song in songs:
        #     self.songs.append(_song)

    def add_song(self, song: Song) -> str:
        if self.published:
            return f"Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return f"Cannot remove songs. Album is published."
        for album_song in self.songs:
            if album_song.name == song_name:
                self.songs.remove(album_song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_result = [f"Album {self.name}"]
        for album_sng in self.songs:
            album_result.append(f"== {album_sng.get_info()}")
        return '\n'.join(album_result)




