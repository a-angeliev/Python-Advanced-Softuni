from project.hero import Hero


class Elf(Hero):
    pass


elf = Elf("Elf", 1)
print(elf.username)
print(elf.level)
print(str(elf))
