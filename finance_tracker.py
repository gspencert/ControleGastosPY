import csv
import os

NOME_ARQUIVO = "gastos.csv"
CATEGORIAS = ["Comida", "Lazer", "Contas", "Moradia", "Cartão de Crédito"]
# 1. ATUALIZAÇÃO: Adicionando 'categoria' às colunas
COLUNAS = ["data", "valor", "categoria", "descricao"] 

def inicializar_arquivo():
    # Esta função agora cria o arquivo com as 4 colunas
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:
        with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(COLUNAS)
            print(f"Arquivo '{NOME_ARQUIVO}' inicializado com as colunas: {', '.join(COLUNAS)}")


def adicionar_gasto():
    # REMOVIDO: Linhas que redefinem CATEGORIAS e NOME_ARQUIVO (usando as globais)
    
    descricao = input("Descrição do gasto: ")
    
    # Validação do Valor
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

    # Seleção e Validação da Categoria (Usando a lista global CATEGORIAS)
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

    # Salva no arquivo CSV, incluindo a categoria
    with open(NOME_ARQUIVO, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Ordem das colunas: data, valor, categoria, descricao
        writer.writerow([data, f"{valor:.2f}", categoria_selecionada, descricao])

    print("\nGasto adicionado com sucesso!")


def listar_gastos():
    """Lista todos os gastos, exibindo a categoria."""
    try:
        with open(NOME_ARQUIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            try:
                # Pula o cabeçalho (que agora tem 4 colunas)
                next(reader) 
            except StopIteration:
                print("Nenhum gasto cadastrado.")
                return

            print("\n--- LISTA DE GASTOS ---")
            
            gastos_encontrados = False
            for row in reader:
                # ATUALIZAÇÃO: Verifica se há pelo menos 4 colunas (data, valor, categoria, descricao)
                if len(row) >= 4:
                    gastos_encontrados = True
                    # Desempacotamento correto dos dados
                    data, valor, categoria, descricao = row[0], row[1], row[2], row[3] 
                    
                    # Exibição com a categoria
                    print(f"[{data}] - {categoria} | {descricao}: R$ {valor}")
                # Adicionado tratamento para linhas antigas/incompletas
                elif len(row) >= 3: 
                    # Caso seja um gasto antigo sem categoria
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
                # O índice do valor (row[1]) não mudou, então esta função está ok, mas é bom manter a verificação.
                if len(row) > 1:
                    try:
                        total += float(row[1])
                    except ValueError:
                        print(f"Aviso: Ignorando valor inválido na linha: {row}") 
                        pass 

            print(f"\nTotal gasto: R$ {total:.2f}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{NOME_ARQUIVO}' não encontrado. Execute a inicialização.")
