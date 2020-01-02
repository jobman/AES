from model.task import *


class Client:

    DB_client = []
    def __init__(self, name):
        self.name = name
        self.DB_client.append(self)

    def create_task(self, description):
        task = Task(self, description)
        # until no DB
        Task.DB_tasks.append(task)
        return task
