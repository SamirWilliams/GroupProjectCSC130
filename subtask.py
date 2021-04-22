from task import Task


class Subtask(Task):
    def __init__(self, task_id, name, deadline):
        super().__init__()