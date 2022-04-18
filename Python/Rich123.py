from rich import print as rprint
from time import sleep
from rich.progress import track

def process():
    sleep(0.05)
for tick in track(range(100), description="[dark_blue]Loading")
list1=["Jack", "Mike", "Ben"]
print(list1)
rprint(list1)

boolshit=[True, False]
rprint(boolshit)

"""import time

from rich.progress import Progress
with Progress() as progress:
    task1 = progress.add_task("Main game", total=100)
    task2 = progress.add_task("Neural learning")
    task2 = progress.add_task("Player sucked")
    
    while not progress.finished:
        progress.update(task1, advanced)"""

