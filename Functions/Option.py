from Functions import NewAcc, Login
import sys

def option():
    option = str(input('Deseja logar em uma conta existente ("\033[1;32mL\033[m"), criar uma nova ("\033[1;34mC\033[m") ou Sair("\033[1;31mS\033[m") : ')).strip()
    while True:
        while option not in 'LlCcSs':
            print('insira uma opção Válida ("\033[1;32mL\033[m", "\033[1;34mC\033[m" ou "\033[1;31mS\033[m") ', end='')
            option = str(input()).strip()
        if option in 'Cc':
            NewAcc.create_acc()
        elif option in 'Ll':
            Login.login_acc()
        elif option in 'Ss':
            sys.exit()
