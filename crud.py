import os

clientes = []

def menu():
    op = ['CRIAR', 'EXIBIR', 'ATUALIZAR', 'DELETAR']
    for i,v in enumerate(op):
        print(f'{i + 1}-{v}')
    print()


def criar():
    cliente = []

    print('CADASTRAR CLIENTE')
    nome = input('Nome: ')
    email = input('Email: ')

    cliente.append(nome)
    cliente.append(email)
    clientes.append(cliente)

    print('Cliente cadastrado')
    print(clientes)
    input('>>>')
    os.system('cls')



while True:
    menu()

    print('Escolha uma opção')
    op = int(input('>>>'))
    os.system('cls')
    if op == 1:
        criar()

