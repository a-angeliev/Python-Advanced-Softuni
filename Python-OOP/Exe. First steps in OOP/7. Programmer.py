class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {course_name}"

    def change_language(self, new_language,  skilles_needed):
        if self.skills >= int(skilles_needed) and not new_language == self.language:
            current_lang = self.language
            self.language = new_language
            return f"{self.name} switched from {current_lang} to {new_language}"
        elif self.skills >= int(skilles_needed) and new_language == self.language:
            return f"{self.name} already knows {new_language}"
        else:
            return f"{self.name} needs {skilles_needed-self.skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
