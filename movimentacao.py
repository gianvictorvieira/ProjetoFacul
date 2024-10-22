from datetime import datetime

class Movimentacao:
    def __init__(self, produto, tipo, quantidade):
        self.produto = produto
        self.tipo = tipo  # "entrada" ou "saida"
        self.quantidade = quantidade
        self.data = datetime.now()
