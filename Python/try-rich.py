from rich import print as rprint
from time import sleep
from rich.progress import track

def process():
    sleep(0.05)

for tick in track(range(100), description="[green]Loading..."):
    process()




list1=["Jack", "John", "Rick", "Nick", "Dick"]
print(list1)
rprint(list1)

boolsith=[True, False]
rprint(boolsith)

