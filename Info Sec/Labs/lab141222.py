from ftplib import FTP

login = 'bormotoon_infosec'
password = 'zfyLKkD3'
ftp = FTP('vh388.timeweb.ru', login, password)
ftp.connect('vh388.timeweb.ru', port=21)
ftp.login(login, password)
with open('XXX365_parol.txt', 'rb') as file:
    ftp.storbinary('STOR XXX365_parol.txt', file)
with open('XXX365_parol.txt', 'rb') as file:
    ftp.storbinary('STOR XXX365_parol.txt', file)
print(ftp.dir())
