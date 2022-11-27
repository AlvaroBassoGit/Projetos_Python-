from produto import Produto

num_produtos = int(input('Deseja cadastrar quantos produtos? '))

produtos = {}
dados_produto = {}

for _ in range(num_produtos):
  prod = Produto(
      input('Nome do produto: ').title(),
      float(input('Preço: ')),
      input('Categoria: ').title(),
      input('Descrição: ')
  )

  dados_produto['Preço'] = prod.preco
  dados_produto['Categoria'] = prod.categoria
  dados_produto['Descrição'] = prod.descricao

  produtos[prod.nome] = dados_produto.copy()
  dados_produto.clear()

print(produtos)