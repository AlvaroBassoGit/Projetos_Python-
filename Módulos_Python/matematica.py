'''Meu primeiro módulo repleto de funções bacanas!!!

'''
breakpoint()
from typing import Union

def soma_dois(numero1: int, numero2:int) -> int:
    '''
    Retorna a soma de dois números inteiros

    params:
        numero1 - número inteiro positivo
        numero2 - número inteiro positivo

    return:
        retorna um número inteiro positivo como a soma dos numeros
    '''
    return numero1 + numero2

def subtrai_dois(numero1: int, numero2: int) -> int:
    '''
    Retorna a diferença de dois números inteiros

    params:
        numero1 - número inteiro positivo
        numero2 - número inteiro positivo

    return:
        retorna um número inteiro positivo como a subtração dos números
    '''
    return numero1 - numero2

def multiplica_dois(numero1: int, numero2: int) -> int:
    '''
    Retorna a multiplicação de dois números inteiros

    params:
        numero1 - número inteiro positivo
        numero2 - número inteiro positivo

    return:
        retorna um número inteiro positivo como a multiplicação dos números
    '''
    return numero1 * numero2

def divide_dois(numero1: int, numero2: int) -> float:
    '''
    Retorna a divisão de dois números inteiros. Caso o divisor seja igual a
    zero, ele terá seu valor alterado para 1 e uma mensagem de aviso será
    impressa no terminal

    params:
        numero1 - número inteiro positivo
        numero2 - número inteiro positivo

    return:
        retorna um número de ponto flutuante como a divisão dos números
    '''
    if numero2 == 0:
        print('Valor do divisor alterado para 1')
        numero2 = 1
    return numero1 / numero2

def par_ou_impar(numero: int) -> str:
    '''
    Verifica se um número é par ou ímpar

    param:
        numero: inteiro positivo

    return:
        retorna PAR ou ÍMPAR
    '''
    if numero % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'

def media(numeros: list, decimais: int = 2) -> float:
    '''
    Calcula a média aritmética dos valores passados

    params:
        numeros: uma lista com valores inteiros ou ponto flutuante
        decimais: inteiro positivo que define as casas decimais da media

    return:
        retorna um número de ponto flutuante como média aritmética dos valores
        com apenas 2 casas decimais por padrão
    '''
    return round(sum(numeros) / len(numeros), decimais)

def potencia(base: int, expoente: int) -> Union[int, str]:
    '''Calcula a potência de um determinado número

    params:
        base: inteiro positivo e diferente de 0
        expoente: inteiro positivo

    return:
        retorna a exponenciação ou uma mensagem de erro'''
    if base == 0:
        return '[ ERRO ] A base tem que ser diferente de 0'
    else:
        return base ** expoente

def fatorial(numero: int) -> int:
    '''
    Calcula o fatorial de um número

    param:
        numero: inteiro positivo

    return:
        retorna o fatorial do número fornecido
    '''
    fat = 1
    if numero in [0, 1]:
        return fat
    else:
        for num in range(numero, 0, -1):
            fat *= num
        return fat

def calcula_percentual(valor: Union[int, float], porcento: int, decimais: int
                       = 2) -> str:
    '''
    Calcula o percentual de um valor inteiro ou ponto flutuante

    params:
        valor: inteiro ou ponto flutuante positivos
        porcento: inteiro positivo. Percentual que se deseja calcular
        decimais: inteiro positivo. Precisão do valor calculado, ou seja,
        quantas casas decimais serão consideradas

    return:
        retorna o valor correspondente ao percentual informado sobre o montante
    '''
    valor_calculado = valor * (porcento / 100)
    return f'{valor_calculado:.{decimais}f}'

def quantos_porcento(num1: float, num2: float, decimais: int = 2) -> float:
    '''
    Calcula quantos porcento um valor representa sobre o outro

    params:
        num1: ponto flutuante positivo. É o valor que se deseja saber quantos
        porcento representa sobre um montante
        num2: ponto flutuante positivo. É o montante total ao qual será
        calculado o percentual
        decimais: inteiro positivo. Precisão do valor calculado, ou seja,
        quantas casas decimais serão consideradas

    return:
        retorna o percentual que um valor representa sobre o outro
    '''
    percentual = num1 / num2
    return f'{percentual:.{decimais}%}'

if __name__ == '__main__':
    print(__doc__)
    print('É apenas o módulo de matemática')
