from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    pass


bk = BladeKnight("bk", 1)
print(bk.username)
print(bk.level)
print(str(bk))