import hashlib
from Functions import ValidationUserPass, Option


def create_acc():
    user = ValidationUserPass.user_validation()
    password = str(input('Digite uma senha(8 caracteres e sem espaços): ')).strip()
    while True:
        if len(password) < 8:
            print('\033[1;31mA senha deve conter mais de 8 dígitos!\033[m')
            password = (input('Digite uma senha válida: '))
        else:
            break
    hashPassword = hashlib.md5(password.encode('utf-8')).hexdigest()
    file = open('Login.txt', 'a')
    file.write(user + '\n')
    file.write(hashPassword + '\n')
    file.close
    Option.option()

