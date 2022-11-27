from modulos.conexao import (
    conecta_bd,
    abre_sessao
)

session = abre_sessao(conecta_bd())


def cadastrar_produto(prd):
    session.add(prd)
    session.commit()
    return f'{prd.name} {prd.color} cadastrado com sucesso!'


def listar_produtos(tbl):
    query_prd = session.query(tbl).all()
    return query_prd


def atualizar_produto(tbl, produto, opcao, campo):
    query = session.query(tbl).get(produto)
    match opcao:
        case 'nome':
            query.name = campo
        case 'cor':
            query.color = campo
        case 'preço':
            query.price = float(campo)
        case 'quantidade':
            query.quantity = int(campo)
        case 'descrição':
            query.description = campo
        case _:
            ''
    session.commit()
    return f'{query.name} foi atualizado com sucesso!'


def remover_produto(tbl, produto):
    prd = session.query(tbl).filter_by(name=produto).first()
    session.delete(prd)
    session.commit()
    return f'{prd.name} foi removido com sucesso!'


def procurar_produto(tbl, produto):
    prd = session.query(tbl).filter_by(name=produto).all()
    return prd
