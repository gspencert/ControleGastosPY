import csv
import os

NOME_ARQUIVO = "gastos.csv"
COLUNAS = ["data", "valor", "descricao"]

def inicializar_arquivo():
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:
        with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(COLUNAS)

def adicionar_gasto():
    descricao = input("Descrição do gasto: ")
    
    while True:
        valor_str = input("Valor (ex: 10.50): ").replace(",", ".")
        try:
            valor = float(valor_str)
            if valor <= 0:
                 print("O valor deve ser positivo.")
                 continue
            break
        except ValueError:
            print("Valor inválido! Digite um número.")

    data = input("Data (ex: DD/MM/AAAA): ")

    with open(NOME_ARQUIVO, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([data, f"{valor:.2f}", descricao])

    print("Gasto adicionado com sucesso!")

def listar_gastos():
    try:
        with open(NOME_ARQUIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            try:
                next(reader)
            except StopIteration:
                print("Nenhum gasto cadastrado.")
                return

            print("\n--- LISTA DE GASTOS ---")
            
            gastos_encontrados = False
            for row in reader:
                if len(row) >= 3:
                    gastos_encontrados = True
                    data, valor, descricao = row[0], row[1], row[2]
                    print(f"[{data}] - {descricao}: R$ {valor}")
                
            if not gastos_encontrados:
                print("Nenhum gasto cadastrado.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{NOME_ARQUIVO}' não encontrado. Execute a inicialização.")

def total_gastos():
    total = 0.0
    try:
        with open(NOME_ARQUIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            try:
                next(reader)
            except StopIteration:
                print("\nTotal gasto: R$ 0.00")
                return

            for row in reader:
                if len(row) > 1:
                    try:
                        total += float(row[1])
                    except ValueError:
                        print(f"Aviso: Ignorando valor inválido na linha: {row}") 
                        pass 

        print(f"\nTotal gasto: R$ {total:.2f}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{NOME_ARQUIVO}' não encontrado. Execute a inicialização.")