from modulos.menu import (
    menu_principal,
    limpa_tela,
    cabecalho
)
from time import sleep
from modulos.tabela import (
    create_table,
    Product
)
from modulos.acoes import (
    cadastrar_produto,
    listar_produtos,
    remover_produto,
    procurar_produto,
    atualizar_produto
)
import sys

if __name__ == '__main__':
    while True:
        match menu_principal():
            case 1:
                limpa_tela()
                print(cabecalho(" Novo produto "))
                prd = Product(
                    name=input('Nome: ').strip().title(),
                    color=input('Cor: ').strip().title(),
                    price=float(input('Preço [R$]: ')),
                    quantity=int(input('Quantidade: ')),
                    description=input('Descrição: ').capitalize()
                )
                print(cadastrar_produto(prd))
                sleep(2)
            case 2:
                limpa_tela()
                print(cabecalho(" Atualizar produto "))
                for produto in listar_produtos(Product):
                    print(f'{produto.id}) {produto.name} {produto.color}')
                escolha = int(input('Qual produto deseja atualizar? '))
                print('[ nome | cor | preço | quantidade | descrição ]')
                opcoes = input('Qual campo ? ').strip().lower()
                campo = input('Digite a nova informação: ').strip()
                print(atualizar_produto(Product, escolha, opcoes, campo))
                input('\nPressione <enter> para voltar')
            case 3:
                limpa_tela()
                print(cabecalho(" Remover produto "))
                for produto in listar_produtos(Product):
                    print(f'{produto.name}')
                    prd = input('Qual produto deseja remover? ').title()
                print(remover_produto(Product, prd))
                input('\nPressione <enter> para voltar')
            case 4:
                limpa_tela()
                print(cabecalho(" Listagem de Produtos "))
                for produto in listar_produtos(Product):
                    print(f'\n{produto.name} {produto.color}')
                    print(f'R${produto.price}')
                    print(f'Estoque: {produto.quantity}')
                    print('-- X -- ')
                input('\nPressione <enter> para voltar')
            case 5:
                limpa_tela()
                print(cabecalho(" Procurar por produto "))
                produto = input('Qual produto deseja procurar? ').title()
                pesquisa = procurar_produto(Product, produto)
                if isinstance(pesquisa, list):
                    for prd in pesquisa:
                        print(f'\n{prd.name} {prd.color}')
                        print(f'R${prd.price}')
                        print(f'Estoque: {prd.quantity}')
                        print('-- X -- ')
                else:
                    print(f'\n{pesquisa.name} {pesquisa.color}')
                    print(f'R${pesquisa.price}')
                    print(f'Estoque: {pesquisa.quantity}')
                input('\nPressione <enter> para voltar')
            case 6:
                create_table()
                sleep(1)
            case 7:
                print('Encerrando o programa...')
                sleep(2)
                sys.exit('Programa encerrado com sucesso!')
            case _:
                print('Opção inválida')
                sleep(1)
