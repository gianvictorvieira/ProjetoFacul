from produto import Produto
from movimentacao import Movimentacao

estoque = []
movimentacoes = []

def cadastrar_produto_manual():
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço: "))
    localizacao = input("Localização no depósito: ")
    
    novo_produto = Produto(nome, categoria, quantidade, preco, localizacao)
    estoque.append(novo_produto)
    print(f"Produto '{nome}' cadastrado com sucesso.")

def consultar_produto(nome):
    for produto in estoque:
        if produto.nome == nome:
            return produto
    return None

def movimentar_estoque_manual():
    nome_produto = input("Nome do produto para movimentar: ")
    tipo = input("Tipo de movimentação ('entrada' ou 'saida'): ").lower()
    quantidade = int(input("Quantidade: "))
    
    produto = consultar_produto(nome_produto)
    
    if produto:
        if tipo == "entrada":
            produto.quantidade += quantidade
        elif tipo == "saida" and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
        movimentacoes.append(Movimentacao(produto, tipo, quantidade))
        print(f"Movimentação de {quantidade} '{produto.nome}' registrada.")
    else:
        print("Produto não encontrado.")
