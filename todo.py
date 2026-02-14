class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description}"