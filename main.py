import csv
import os

def inicializar_arquivo():
    if not os.path.exists("gastos.csv"):
        with open("gastos.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["descricao", "valor", "data"])

def adicionar_gasto():
    descricao = input("Descrição do gasto: ")
    valor = input("Valor: ")
    data = input("Data: ")

    with open("gastos.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([descricao, valor, data])

    print("Gasto adicionado com sucesso!")

def listar_gastos():
    with open("gastos.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n--- LISTA DE GASTOS ---")
        for row in reader:
            print(f"{row[0]} - R$ {row[1]}")

def total_gastos():
    total = 0
    with open("gastos.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

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

