import csv

# O módulo csv, contém duas principais funções:

# Um leitor (reader) que nos ajuda a ler o conteúdo, já fazendo as
# transformações dos valores para Python;

# E um escritor (writer) para facilitar a escrita nesse formato.
# import csv

# with open("graduacao_unb.csv", encoding="utf-8") as file:
#     graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
#     # Usando o conceito de desempacotamento
#     header, *data = graduacao_reader

# print(data)


# Podemos fazer uma análise e verificar quantos cursos são ofertados por departamento. Em seguida salvamos o resultado também no formato .csv:

with open("graduacao_unb.csv", encoding="utf8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

group_by_department = {}
for row in data:
    department = row[15]
    if department not in group_by_department:
        group_by_department[department] = 0
    group_by_department[department] += 1

# Escreve o relatório em .csv
# Abre um arquivo para escrita
with open("department_report.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Escreve o cabeçalho
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # Escreve as linhas de dados
    # Desempacotamento de valores
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = [
            department,
            grades,
        ]
        writer.writerow(row)

# Existem ainda o leitor e o escritor baseados em dicionários. A principal
# vantagem é que não precisamos manipular os índices para acessar os dados das
# colunas. A desvantagem é o espaço ocupado em memória
# (que é maior que o comum), devido à estrutura de dados utilizada.

# lê os dados
with open("graduacao_unb.csv", encoding="utf-8") as file:
    graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

    # a linha de cabeçalhos é utilizada como chave do dicionário
    # agrupa cursos por departamento
    group_by_department = {}
    for row in graduacao_reader:
        department = row["unidade_responsavel"]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1

# abre um arquivo para escrita
with open("new_department_report.csv", "w", encoding="utf-8") as file:
    # os valores a serem escritos devem ser dicionários
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    # É necessário passar o arquivo e o cabeçalho
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    # escreve as linhas de dados
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = {"Departamento": department, "Total de Cursos": grades}
        writer.writerow(row)
