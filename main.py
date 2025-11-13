import csv
import os

def inicializar_arquivo():
    if not os.path.exists("gastos.csv"):
        with open("gastos.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["descricao", "valor", "data"])
    else:
        if os.path.getsize("gastos.csv") == 0:
            with open("gastos.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["descricao", "valor", "data"])

def adicionar_gasto():
    descricao = input("Descrição do gasto: ")
    
    while True:
        valor = input("Valor: ").replace(",", ".")
        try:
            float(valor)
            break
        except ValueError:
            print("Valor inválido! Digite um número.")

    data = input("Data: ")

    with open("gastos.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data, valor, descricao])

    print("Gasto adicionado com sucesso!")

def listar_gastos():
    with open("gastos.csv", "r") as file:
        reader = csv.reader(file)

        try:
            next(reader)
        except StopIteration:
            print("Nenhum gasto cadastrado.")
            return

        print("\n--- LISTA DE GASTOS ---")
        vazio = True
        for row in reader:
            vazio = False
            print(f"{row[0]} - R$ {row[1]} - {row[2]}")
        if vazio:
            print("Nenhum gasto cadastrado.")

def total_gastos():
    total = 0
    with open("gastos.csv", "r") as file:
        reader = csv.reader(file)

        try:
            next(reader)
        except StopIteration:
            print("\nTotal gasto: R$ 0.00")
            return

        for row in reader:
            try:
                total += float(row[1])
            except ValueError:
                pass 

    print(f"\nTotal gasto: R$ {total:.2f}")

def menu():
    while True:
        print("\n=== FinanceTrack ===")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Total gasto")
        print("4. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            total_gastos()
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


inicializar_arquivo()
menu()
