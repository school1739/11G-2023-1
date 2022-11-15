from ftplib import FTP

HOST = 'vh388.timeweb.ru'
PORT = 21
USER = 'bormotoon_infosec'
PASSWORD = 'zfyLKkD3'

file_to_send = "Ciphers/secrets_very_secret.txt"
file_to_load = "Ciphers/Decode.txt"

ftp = FTP()
ftp.connect(HOST, PORT)
ftp.login(USER, PASSWORD)

action = int(input('Выберите действие:\n'
                   f'1. Отправить файл {file_to_send}\n'
                   f'2. Скачать файл {file_to_load}\n'
                   '3. Посмотреть файлы на сервере\n'))

match action:
    case 1:
        with open(file_to_send, 'rb') as file:
            ftp.storbinary(f'STOR {file_to_send}', file)
    case 2:
        with open(file_to_load, 'wb') as fp:
            ftp.retrbinary(f'RETR {file_to_load}', fp.write)
    case 3:
        print(ftp.retrlines('LIST'))
