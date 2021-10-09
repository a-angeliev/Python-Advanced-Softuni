from project.wizard import Wizard


class DarkWizard(Wizard):
    pass


dw = DarkWizard("dw", 1)
print(dw.username)
print(dw.level)
print(str(dw))