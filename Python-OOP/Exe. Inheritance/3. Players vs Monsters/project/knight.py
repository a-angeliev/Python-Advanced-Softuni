from project.hero import Hero


class Knight(Hero):
    pass


kn = Knight("kn", 1)
print(kn.username)
print(kn.level)
print(str(kn))