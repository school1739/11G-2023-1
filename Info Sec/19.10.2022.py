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

filename = "Decode.txt"

# Read file in binary mode
with open(filename, "rb") as file:
    # Command for Uploading the file "STOR filename"
    ftp.storbinary(f"STOR {filename}", file)

#Vizhinere
#YOU WILL DIE RIGHT NOW!
#SCHOOL
#RRC LUEO SXQ UQVWF QWLN

#CESAR
#We all will die
#5
#1j%fqq%Bnqq%inj