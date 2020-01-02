from math import *


class Task:
    DB_tasks = []

    def __init__(self, client, description):
        self.client = client
        self.description = description

        self.estimated_usd = 0
        self.estimation_list = []

    def add_estimation(self, estimation):
        self.estimation_list.append(estimation)

        log_list = []
        for est in self.estimation_list:
            log_list.append(log10(est.usd))

        mean_log = sum(log_list) / len(log_list)
        self.estimated_usd = round(10 ** mean_log,2)
