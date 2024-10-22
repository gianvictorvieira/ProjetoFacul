from estoque import cadastrar_produto_manual, movimentar_estoque_manual
from relatorio import gerar_relatorio

def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Estoque ===")
        print("1. Cadastrar Produto")
        print("2. Movimentar Estoque")
        print("3. Gerar Relatório")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produto_manual()
        elif opcao == "2":
            movimentar_estoque_manual()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
