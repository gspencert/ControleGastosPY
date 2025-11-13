from finance_tracker import inicializar_arquivo, adicionar_gasto, listar_gastos, total_gastos

def menu():
    while True:
        print("\n=== FinanceTrack ===")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Total gasto")
        print("4. Sair")
        opcao = input("Escolha a opção: ")

        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            total_gastos()
        elif opcao == "4":
            print("Encerrando o FinanceTrack. Até logo!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")

if __name__ == "__main__":
    inicializar_arquivo()
    menu()