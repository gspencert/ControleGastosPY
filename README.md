# 🐙 FinanceTrack: Gerenciador de Gastos Pessoais

Este repositório contém um simples projeto em **Python** para gerenciar despesas pessoais, salvando os dados em um arquivo CSV (`gastos.csv`).

---

## ⚙️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Módulo `csv`:** Utilizado para ler e escrever os dados no arquivo `gastos.csv`.
* **Módulo `os`:** Utilizado para verificar a existência e o estado do arquivo CSV.

---

## ✨ Funcionalidades

O programa oferece uma interface de menu simples para as seguintes operações:

1.  **Adicionar Gasto:** Registra a descrição, o valor e a data de uma nova despesa.
2.  **Listar Gastos:** Exibe todas as despesas registradas.
3.  **Total Gasto:** Calcula e mostra a soma total de todos os valores registrados.
4.  **Sair:** Encerra a aplicação.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina.

### Execução

1.  Clone este repositório ou baixe o arquivo `main.py` e `finance_tracker.py`.
2.  Abra o terminal na pasta do projeto.
3.  Execute o script Python:

    ```bash
    python main.py
    ```

4.  O menu interativo será exibido, e você poderá começar a gerenciar seus gastos.

---

## 📁 Estrutura do Arquivo CSV

O arquivo `gastos.csv` é criado automaticamente na primeira execução e usa o seguinte formato de cabeçalho:

| Coluna | Descrição |
| :--- | :--- |
| `descricao` | Texto descritivo do gasto (e.g., "Supermercado"). |
| `valor` | O valor monetário do gasto. |
| `data` | A data em que o gasto ocorreu. |
