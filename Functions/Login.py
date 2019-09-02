import sys, hashlib



def login_acc():
    file = open('Login.txt', 'r')
    lines = file.readlines()
    user = str(input('Digite o nome de usuário: '))
    for index, line in enumerate(lines):
        line = str(line).strip()
        if user == line:
            passwordToValidate = lines[index + 1].rstrip()
            password = str(input('Digite a senha: '))
            hashpassword = hashlib.md5(password.encode('utf-8')).hexdigest()
            while not hashpassword == passwordToValidate:
                print('\033[1;31mSenha incorreta!\033[m')
                password = str(input('Digite a senha: '))
                hashpassword = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashpassword == passwordToValidate:
                print('\033[1;32mLogin Aceito\033[m')
                sys.exit()
       #
    print('\033[1;31mUsuário não encontrado\033[m')

