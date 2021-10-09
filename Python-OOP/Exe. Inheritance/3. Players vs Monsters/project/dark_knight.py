from project.knight import Knight


class DarkKnight(Knight):
    pass


dk = DarkKnight("dk", 1)
print(dk.username)
print(dk.level)
print(str(dk))
