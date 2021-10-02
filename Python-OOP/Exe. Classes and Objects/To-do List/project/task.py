class Task:
    def __init__(self, name: str, due_data: str):
        self.name = name
        self.due_date = due_data
        self.comments = []
        self.completed = False

    def change_name(self,name: str):
        if name == self.name:
            return f"Name cannot be the same."
        self.name = name
        return self.name

    def change_due_date(self, due_data: str):
        if due_data == self.due_date:
            return f"Date cannot be the same."
        self.due_date = due_data
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if len(self.comments) < comment_number:
            return "Cannot find comment."
        else:
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


