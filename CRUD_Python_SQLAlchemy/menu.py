'''Este módulo refere-se ao menu da aplicação'''

import os
import platform


def limpa_tela() -> None:
    '''
    Limpa a tela independente do Sistema Operacional

    return:
        None
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cabecalho(txt) -> str:
    '''
    Exibe um cabeçalho personalizado

    return:
        string formatada
    '''
    return f'{txt:-^50}'


def menu_principal() -> int:
    '''
    Exibe o menu principal na tela

    return:
        None
    '''
    limpa_tela()
    print(cabecalho(" MENU PRINCIPAL "))
    print(f'''
          1) Cadastrar produto
          2) Atualizar produto
          3) Remover produto
          4) Listar todos os produtos
          5) Procurar por produto
          6) Criar tabela
          7) Sair
          ''')
    opcao = int(input('Opção: '))
    return opcao
