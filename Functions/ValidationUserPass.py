users = list()
file = open('Login.txt', 'r')
lines = file.readlines()
file.close()
'''for x in count:
    if x % 2 == 0:
        users += file.readline()'''
for x, y in enumerate(lines):
    if x % 2 == 0:
        users.append(y.rstrip())

def user_validation():
    user = str(input('Digite o nome de usuário: '))
    while user in users:
        user = str(input('Nome de Usuário já existe tente outro :'))
    return user
