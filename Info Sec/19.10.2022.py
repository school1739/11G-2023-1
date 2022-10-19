import pyftpdlib

from ftplib import FTP

HOST = "vh388.timeweb.ru"
PORT = 21
USER = 'bormotoon_infosec'
PASSWORD = 'zfyLKkD3'

ftp = FTP()
print(f'Conecting to FTP\nHost: {HOST}\nPort: {PORT}')
ftp.connect(HOST, PORT)
print(f'Conecting sucess!\nLogin as: {USER},Pass: {PASSWORD}')
ftp.login(USER, PASSWORD)
print('Login Succes!')

"""filename = "Decode.txt"

# Read file in binary mode
with open(filename, "rb") as file:
    # Command for Uploading the file "STOR filename"
    ftp.storbinary(f"STOR {filename}", file)"""
with open("secrets_very_secret.txt", "wb") as fp:
    ftp = ftplib.FTP("192.168.2.222")
    ftp.login("test", "123qwe")
    remotefile = 'FirefoxInstaller.exe'
    download = 'https://d1ny9casiyy5u5.cloudfront.net/tmp/FirefoxInstaller.exe'
    with open(download, 'wb') as file:
        ftp.retrbinary('RETR %s' % remotefile, file.write)
    print(ftp.retrlines("LIST"))

#Vizhinere
#YOU WILL DIE RIGHT NOW!
#SCHOOL
#RRC LUEO SXQ UQVWF QWLN

#CESAR
#We all will die
#5
#1j%fqq%Bnqq%inj