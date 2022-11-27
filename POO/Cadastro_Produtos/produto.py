class Produto:
  '''Modelo para cadastrar produtos'''

  def __init__(self, nome: str, valor: float, categoria: str, descricao: str) -> None:
    self.nome: str = nome
    self.__preco: float = valor
    self.__categoria: str = categoria
    self.descricao: str = descricao

  @property
  def preco(self) -> float:
    '''Retorna o preço atual'''
    return self.__preco

  @preco.setter
  def preco(self, novopreco: float) -> float:
    '''Altera o preço'''
    if novopreco > 0:
      self.__preco = novopreco
    return self.preco

  @property
  def categoria(self) -> str:
    '''Retorna a categoria'''
    return self.__categoria

  @categoria.setter
  def categoria(self, novacategoria: str) -> str:
    self.__categoria = novacategoria
    return f'{self.nome} teve sua categoria alterada com sucesso'

  def reajustar_preco(self, percentual: int) -> str:
    '''Reajusta o preço do produto de acordo com o percentual informado'''
    self.preco = self.preco + self.preco * (percentual / 100)
    return f'{self.nome} teve seu preço reajustado em {percentual:.2f}%'

  def __repr__(self):
    return f'{self.nome}'

  def __str__(self):
    return f'{self.nome} : {self.categoria}'

if __name__ == '__main__':
  print('Classe de Produto. Rode o script cadastrar produtos')