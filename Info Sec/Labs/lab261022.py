from ftplib import FTP

login = 'bormotoon_infosec'
password = 'zfyLKkD3'
ftp = FTP('vh388.timeweb.ru', login, password)
ftp.connect('vh388.timeweb.ru', port=21)
ftp.login(login, password)
with open('Secret_Caesar.txt', 'rb') as file:
    ftp.storbinary('STOR Secret_Caesar.txt', file)
with open('Secret_Vigenere.txt', 'rb') as file:
    ftp.storbinary('STOR Secret_Vigenere.txt', file)
with open('Decode.txt', 'wb') as file:
    ftp.retrbinary('RETR Decode.txt', file.write)
print(ftp.dir())
