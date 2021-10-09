from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    pass


sm = SoulMaster("sm", 1)
print(sm.username)
print(sm.level)
print(str(sm))