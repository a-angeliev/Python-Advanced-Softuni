from project.hero import Hero


class Wizard(Hero):
    pass


wizard = Wizard("wizard", 1)
print(wizard.username)
print(wizard.level)
print(str(wizard))