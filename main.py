import pandas as pd
import csv

def csv_to_xlsx(csv_file, xlsx_file):
    try:
        # Lê o arquivo CSV usando csv.reader e ignora linhas com erros
        with open(csv_file, 'r', errors='ignore') as file:
            reader = csv.reader(file)
            lines = list(reader)

        # Converte a lista de linhas em um DataFrame
        df = pd.DataFrame(lines[1:], columns=lines[0])

        # Escreve o DataFrame no arquivo Excel
        df.to_excel(xlsx_file, index=False)

        print(f'O arquivo Excel "{xlsx_file}" foi gerado com sucesso.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
arquivo_csv = 'entrada.csv'

# Substitua 'saida.xlsx' pelo nome que deseja para o arquivo Excel de saída
arquivo_xlsx = 'saida.xlsx'

# Chama a função para converter o CSV para XLSX
csv_to_xlsx(arquivo_csv, arquivo_xlsx)
