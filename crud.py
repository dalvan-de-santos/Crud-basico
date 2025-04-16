import os

clientes = []

def menu():
    op = ['CRIAR', 'EXIBIR', 'ATUALIZAR', 'DELETAR']
    for i,v in enumerate(op):
        print(f'{i + 1}-{v}')
    print()


def criar():

    while True:
        cliente = []

        print('CADASTRAR CLIENTE')
        nome = input('Nome: ')
        email = input('Email: ')

        cliente.append(nome)
        cliente.append(email)
        clientes.append(cliente)
        print('Cliente cadastrado')

        print('Deseja cadastrar mais? S/N')
        op = input('>>>').upper()
        if op == 'N':
            os.system('cls')
            break
            
        os.system('cls')



def exibir():
    for v in clientes:
        print(v)
    input('>>>')


while True:
    menu()

    print('Escolha uma opção')
    op = int(input('>>>'))
    os.system('cls')
    if op == 1:
        criar()
    
    elif op == 2:
        exibir()

