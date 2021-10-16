class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for _ in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        full_pages = photos_count // 4
        full_pages = int(full_pages)
        last_pages = photos_count % 4
        if last_pages != 0:
            full_pages += 1
        return cls(full_pages)

    def add_photo(self, label: str):
        for index in range(len(self.photos)):
            if not len(self.photos[index]) == 4:
                self.photos[index].append(label)
                print(f"{label} photo added successfully on page {index + 1} slot {len(self.photos[index])}")
                break
        return "No more free slots"

    def display(self):
        string = "-----------\n"
        for el in self.photos:
            if len(el) == 4:
                string += "[] [] [] []\n"

            elif len(el) != 0:
                string += "[] " * len(el)
                string += "\n"
            else:
                string += "\n"
            string += "-----------\n"
        return string
#
# a = PhotoAlbum(10)
# print(a.photos)
# b = PhotoAlbum.from_photos_count(5)
# print(b.photos)
# a.add_photo("koki")
# a.add_photo("floki")
# a.add_photo("moki")
# a.add_photo("dooki")
# a.add_photo("yoki")
# a.add_photo("yoki")
# a.add_photo("yoki")
# a.add_photo("yoki")
# print(a.display())
# /////////////////////////////////////////////////////////////////////////
# import unittest
#
#
# class TestsPhotoAlbum(unittest.TestCase):
#     def test_init_creates_all_attributes(self):
#         album = PhotoAlbum(2)
#         self.assertEqual(album.pages, 2)
#         self.assertEqual(album.photos, [[], []])
#
#     def test_from_photos_should_create_instace(self):
#         album = PhotoAlbum.from_photos_count(12)
#         self.assertEqual(album.pages, 3)
#         self.assertEqual(album.photos, [[], [], []])
#
#     def test_add_photo_with_no_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.add_photo("prom")
#         self.assertEqual(result, "No more free slots")
#
#     def test_add_photo_with_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
#
#     def test_display_with_one_page(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
#
#     def test_display_with_three_pages(self):
#         album = PhotoAlbum(3)
#         for _ in range(8):
#             album.add_photo("asdf")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
#
#
# if __name__ == "__main__":
#     unittest.main()