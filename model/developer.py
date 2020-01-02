from model.estimation import *


class Developer:
    DB_developer = []

    def __init__(self, name):
        self.name = name
        self.DB_developer.append(self)

    def estimate_task(self, task, usd):
        estimation = Estimation(task, self, usd)
        task.add_estimation(estimation)
