from project.elf import Elf


class MuseElf(Elf):
    pass


melf = MuseElf("MElf", 2)
print(melf.username)
print(melf.level)
print(str(melf))