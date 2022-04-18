import time

from rich.progress import Progress

with Progress() as progress:
    task1=progress.add_task("Main game", total=100)
    task2=progress.add_task("Neural learning", total=100)
    task3=progress.add_task("Player sucked", total=100)


