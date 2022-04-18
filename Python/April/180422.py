from rich import print as rprint
from time import sleep
from rich.progress import track

def process():
    sleep(0.05)

for tick in track(range(100), description="[dark_blue]Loading..."):
    process()
list1=["Rick", "John","Jack", "Nick", "Dick"]
print(list1)
rprint(list1)
boolshith=[True, False]
rprint(boolshith)
