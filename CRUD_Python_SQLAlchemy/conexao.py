import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv('./modulos/env')

engine = None


def conecta_bd():
    '''
    wer
    '''
    try:
        global engine
        if engine:
            return engine
        engine = create_engine(
                url=os.environ['strconexao'],
                echo=False
        )
    except Exception as err:
        raise err # ('Erro ao conectar')
    else:
        return engine


def abre_sessao(eng):
    '''
    qwe
    '''
    try:
        Session = sessionmaker(bind=eng)
    except Exception as err:
        raise err # ('Não foi possível abrir uma sessão')
    else:
        session = Session()
        return session
