import sys
from dotenv import load_dotenv
from config.connection import Connection
from modulos.menu import Menu
from modulos.dmql import (
    DQL,
    DML
)

path = load_dotenv('./config/.env')
cnx = Connection()

conn = cnx.connect(path)
dql = DQL(conn)
dml = DML(conn, dql)
menu = Menu()


while True:
    print(menu.menu_principal())
    escolha = int(input('Escolha: '))
    match escolha:
        case 1:
            for login, nome in dql.busca_registros('USERS'):
                print(f'{login:<10} : {nome}')
        case 2:
            novo_login = input('Novo login: ').lower()
            while not dml.verifica_login('USERS', novo_login):
                novo_login = input('Novo login: ').lower()
            else:
                novo_nome = input('Novo nome: ').title()
                dml.insere_registros('USERS', novo_login, novo_nome)
                print('Registro inserido com sucesso')
        case 3:
            for pos, reg in enumerate(dql.busca_registros('USERS'), start=1):
                print(pos, reg[0], sep=') ')
            op = int(input('Opção: '))
            print('Que dado deseja atualizar?')
            print('1. Login', '2. Nome', sep='\n')
            op_campo = int(input('Escolha o campo: '))
            if op_campo == 1:
                novo_login = input('Novo login: ').lower()
                dml.atualizar_registro('USERS', 'LOGIN', op - 1 , op_campo - 1, novo_login)
            else:
                novo_nome = input('Novo nome: ').title()
                dml.atualizar_registro('USERS', 'FULL_NAME', op -1, op_campo - 1, novo_nome)
            print('Registro atualizado com sucesso')
        case 4:
            print('Deseja remover qual registro?')
            for pos, reg in enumerate(dql.busca_registros('USERS'), start=1):
                print(pos, reg[0], sep=') ')
            op = int(input('Opção: '))
            dml.remover_registro('USERS', op - 1)
            print('Registro removido com sucesso')
        case 5:
            sys.exit('Encerrando o programa')
        case _:
            print('Opção inválida')
