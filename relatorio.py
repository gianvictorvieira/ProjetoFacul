from estoque import estoque

def gerar_relatorio():
    print("=== Relatório de Estoque ===")
    for produto in estoque:
        print(f"Produto: {produto.nome}")
        print(f"Categoria: {produto.categoria}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Preço: R${produto.preco}")
        print(f"Localização: {produto.localizacao}")
        print("---")
        if produto.quantidade < 10:
            print(f"Produto com baixo estoque: {produto.nome} ({produto.quantidade} unidades)")
        elif produto.quantidade > 100:
            print(f"Produto com excesso de estoque: {produto.nome} ({produto.quantidade} unidades)")
