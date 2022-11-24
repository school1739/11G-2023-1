from ftplib import FTP

HOST = 'vh388.timeweb.ru'
PORT = 21
USER = 'bormotoon_infosec'
PASSWORD = 'zfyLKkD3'

file_s = "encryption.txt"
file_l = "Decode.txt"

ftp = FTP()
ftp.connect(HOST, PORT)
ftp.login(USER, PASSWORD)
print("1. Отправить файл")
print("2. Скачать файл")
print("3. Посмотреть файлы на сервере")
action = int(input("Выберите действие: "))
if action=="1":
    with open(file_s, 'rb') as file:
        ftp.storbinary(f'STOR {file_s}', file)
if action=="2":
    with open(file_l, 'wb') as fp:
        ftp.retrbinary(f'RETR {file_l}', fp.write)
if action=="3":
    print(ftp.retrlines('LIST'))