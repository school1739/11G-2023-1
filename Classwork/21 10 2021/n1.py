import datetime
day = int(input())
month = int(input())
year = int(input())
date = datetime.(year,month,day)
next_date = date + datetime.timedelta(days=1)

# Evaluation: SyntaxError: invalid syntax. >>>"Списал то, не знаю что".