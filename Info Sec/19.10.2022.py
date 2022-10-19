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