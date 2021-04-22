import names
import random


class Developer:
    def __init__(self):
        self.name = names.get_full_name()
        self.skills = {"Database": random.randint(60, 95), "Middleware": random.randint(60, 95),
                       "UX": random.randint(60, 95), "Security": random.randint(60, 95),
                       "Documentation": random.randint(60, 95), "Testing": random.randint(60, 95)}

    def __str__(self):
        return str(self.name) + "\n" + str(self.skills)
