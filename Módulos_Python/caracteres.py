'''Este é um módulo que manipula strings de diferentes formas.

'''
# breakpoint()
from typing import Union

def conta_vogais(txt: str) -> int:
    '''
    Conta quantas vogais há em uma palavra, frase ou texto

    param:
        txt: string literal, ou seja, uma palavra, frase ou texto

    return:
        retorna o número total de vogais encontradas
    '''
    contagem = 0
    for letra in txt.lower():
        if letra in 'aeiou':
            contagem += 1
    return contagem

def conta_letras(txt: str, espaco=True) -> int:
    '''
    Conta quantas letras há numa palavra, frase ou texto

    params:
        txt: string literal, ou seja, uma palavra, frase ou texto
        espaco: booleano. Se True, considera na contagem os espaços, se False
        não considera

    return:
        retorna um inteiro positivo de quantas letras com ou sem espaços há
        numa palavra, frase ou texto
    '''
    contagem = 0
    if espaco:
        for ch in txt.strip():
            if ch.isalpha() or ch == ' ':
                contagem += 1
    else:
        for ch in txt:
            if ch.isalpha():
                contagem += 1
    return contagem

def tem_maiusculas(txt: str, inicio=False, contar=False) -> Union[bool, int]:
    '''
    Verifica se há letras maiúsculas numa palavra, frase ou texto

    params:
        txt: string literal, ou seja, uma palavra, frase ou texto
        inicio: booleano. Se True, verifica somente se a primeira letra da
        palavra, frase ou texto é maiúscula. Se False, verifica em todo a
        palvra, frase ou texto
        contar: booleano. Se True, conta quantas ocorrências de letras
        maiúsculas foram encontradas na palavra, frase ou texto

    return:
        retorna um inteiro se a contagem for habilitada ou um valor booleano de
        True ou False se a contagem estiver desabilitada
    '''
    contagem = 0
    if inicio and contar:
        if txt[0].isupper():
            contagem += 1
        return contagem
    elif inicio:
        if txt[0].isupper():
            return True
        return False
    elif contar:
        for ch in txt.strip():
            if ch.isupper():
                contagem += 1
        return contagem
    else:
        for ch in txt.strip():
            if ch.isupper():
                return True
        return False

def tem_minusculas(txt: str, inicio=False, contar=False) -> Union[bool, int]:
    '''
    Verifica se há letras minúsculas numa palavra, frase ou texto

    params:
        txt: string literal, ou seja, uma palavra, frase ou texto
        inicio: booleano. Se True, verifica somente se a primeira letra da
        palavra, frase ou texto é minúscula. Se False, verifica em todo a
        palvra, frase ou texto
        contar: booleano. Se True, conta quantas ocorrências de letras
        minúsculas foram encontradas na palavra, frase ou texto

    return:
        retorna um inteiro se a contagem for habilitada ou um valor booleano de
        True ou False se a contagem estiver desabilitada
    '''
    contagem = 0
    if inicio and contar:
        if txt[0].islower():
            contagem += 1
        return contagem
    elif inicio:
        return True
    elif contar:
        for ch in txt.strip():
            if ch.islower():
                contagem += 1
        return contagem
    else:
        for ch in txt.strip():
            if ch.islower():
                return True
        return False

def eh_palindromo(txt: str) -> bool:
    '''
    Verifica uma palavra é um palíndromo ou não. Um palíndromo, é uma palavra
    que quando lida normalmente e de trás pra frente é exatamente igual

    param:
        txt: string literal a ser verificada

    return:
        retorna um valor booleano. Se for um palíndromo retornará True, senão
        retornará False
    '''
    if txt.lower() == txt[::-1].lower():
        return True
    return False

if __name__ == '__main__':
    print('Este é um módulo apenas e me executou pelo terminal')
else:
    print('Me executou como módulo')
