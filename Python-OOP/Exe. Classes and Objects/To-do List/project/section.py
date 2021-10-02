from task import *


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, tas: Task):
        if tas not in self.tasks:
            return f"Could not find task with the name {tas.name}"
        else:
            tas.completed = True
            return f"Completed task {tas.name}"

    def clean_section(self):
        count = 0
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                count +=1
        return f"Cleared {count} tasks."

    def view_section(self):
        cur_list = [el.details() for el in self.tasks]

        return f"Section {self.name}:\n" + "\n".join(cur_list)

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
