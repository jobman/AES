from model.client import *
from model.developer import *

dev1 = Developer("John Dou")
dev2 = Developer("Apu Ramanudjan")
dev3 = Developer("Dmitriy Smirnov")

client = Client("Viktor Panfilov")
task = client.create_task("Выкопать яму за сараем, глубина ямы 2 м, ширина 1 м, длина 1.5 м")

dev1.estimate_task(task,2000)
dev2.estimate_task(task,20)
dev3.estimate_task(task,40)

print("Задача оценена в",task.estimated_usd,"$")