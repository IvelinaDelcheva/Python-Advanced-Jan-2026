from math import ceil

class PhotoAlbum:
    PHOTOS_COUNT = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for p in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        return cls(ceil(photos_count / cls.PHOTOS_COUNT))

    def add_photo(self, label: str) -> str:
        for i, p in enumerate(self.photos):
            if len(p) < PhotoAlbum.PHOTOS_COUNT:
                p.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {p.index(label) + 1}"
        return "No more free slots"

    def display(self) -> str:
        result = ["-----------"]
        for row in self.photos:
            result.append(f"{' '.join(['[]' for _ in range(len(row))])}\n-----------")

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


