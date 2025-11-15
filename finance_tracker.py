import csv
import os

NOME_ARQUIVO = "gastos.csv"
CATEGORIAS = ["Comida", "Lazer", "Contas", "Moradia", "Cartão de Crédito"]
COLUNAS = ["data", "valor", "categoria", "descricao"] 

def inicializar_arquivo():
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:
        with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(COLUNAS)
            print(f"Arquivo '{NOME_ARQUIVO}' inicializado com as colunas: {', '.join(COLUNAS)}")


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

  
    while True:
        print("\nSelecione uma categoria:")
        for i, categoria in enumerate(CATEGORIAS):
            print(f"[{i + 1}] - {categoria}")
        
        escolha_str = input("Digite o número da categoria: ")
        
        try:
            escolha_indice = int(escolha_str) - 1
            
            if 0 <= escolha_indice < len(CATEGORIAS):
                categoria_selecionada = CATEGORIAS[escolha_indice]
                break
            else:
                print(f"Escolha inválida. Digite um número entre 1 e {len(CATEGORIAS)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    data = input("Data (ex: DD/MM/AAAA): ")

   
    with open(NOME_ARQUIVO, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
       
        writer.writerow([data, f"{valor:.2f}", categoria_selecionada, descricao])

    print("\nGasto adicionado com sucesso!")


def listar_gastos():
    """Lista todos os gastos, exibindo a categoria."""
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
               
                if len(row) >= 4:
                    gastos_encontrados = True
                    
                    data, valor, categoria, descricao = row[0], row[1], row[2], row[3] 
                    
                   
                    print(f"[{data}] - {categoria} | {descricao}: R$ {valor}")
                
                elif len(row) >= 3: 
                    # caso seja um gasto antigo sem categoria
                    data, valor, descricao = row[0], row[1], row[2]
                    print(f"[{data}] - SEM CATEGORIA | {descricao}: R$ {valor}")
                
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
