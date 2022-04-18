import time
from rich.progress import Progress
with Progress() as progress:
    task1=progress.add_task("Maim game", total=100)
    task2=progress.add_task("Neural learning", total=100)
    while not progress.finished:
        progress.update()
