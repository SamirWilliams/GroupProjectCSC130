"""
class Task
- name String
- deadline Date

"""


class Task:
    def __init__(self, task_id, name, deadline):
        self.id = 0
        self.name = ""
        self.deadline = ""
        self.subtasks = dict() # dictionary type having subtask name as key and complete or incomplete as value.

    def create_subtask(self):
        pass

    def edit_task(self):
        pass

    def close_task(self):
        pass