from unittest import TestCase, main
from project.mammal import Mammal

class TestMammal(TestCase):
    def test_make_instance(self):
        obj = Mammal("Alex", "monkey", "kwek kwek")
        self.assertEqual("Alex", obj.name)
        self.assertEqual("monkey", obj.type)
        self.assertEqual("kwek kwek", obj.sound)
        self.assertEqual("animals", obj._Mammal__kingdom)



    def test_make_sound(self):
        obj = Mammal("Alex", "monkey", "kwek kwek")
        a = obj.make_sound()
        self.assertEqual("Alex makes kwek kwek", a)

    def test_get_kingdom(self):
        obj = Mammal("Alex", "monkey", "kwek kwek")
        self.assertEqual("animals", obj.get_kingdom())

    def test_info(self):
        obj = Mammal("Alex", "monkey", "kwek kwek")
        self.assertEqual(f"Alex is of type monkey", obj.info())

if __name__ == "__main__":
    main()