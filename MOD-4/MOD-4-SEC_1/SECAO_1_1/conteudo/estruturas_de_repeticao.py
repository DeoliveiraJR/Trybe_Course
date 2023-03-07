# FOR:
# ------------------------------------------------------
# Imagine um sistema que faça a listagem de restaurantes.
# Estes restaurantes possuem uma nota proveniente da avaliação dos seus clientes.
restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

# Quando um cliente pede a listagem de restaurantes, ele pode escolher filtrar o resultado
#  de acordo com a nota. Essa filtragem pode ocorrer percorrendo a lista de restaurantes ou
#  criando uma nova lista com somente aqueles que atendem ao filtro, assim como mostra
#  o exemplo abaixo:
filtered_restaurants = []
MIN_RATING = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > MIN_RATING:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

for index in range(5):
    print(index)

# Quando uma nova lista é criada como resultado de uma iteração,
# podemos simplificar utilizando compreensão de listas.
MIN_RATING = 3.0
filtered_restaurants = [restaurant
                        for restaurant in restaurants
                        if restaurant["nota"] > MIN_RATING]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# A compreensão de listas também funciona com listas de strings. A seguinte cria uma nova
# lista de strings com os nomes que contém a letra ‘a’.
names_list = ['Duda', 'Rafa', 'Cris', 'Yuri']
new_names_list = [name for name in names_list if 'a' in name]

# Aqui o for percorre cada nome em "names_list", verifica se existe a letra "a" nele,
# o adiciona à variável "name", e então gera nossa nova lista "new_names_list"
print(new_names_list)

# Saída
# ['Duda', 'Rafa']

# O exemplo a seguir usa uma compreensão de listas para criar uma lista
# com o quadrado dos números entre 1 e 10.
# Isto é equivalente às operações de map e filter em JavaScript.
quadrados = [x*x for x in range(11)]
print(quadrados)

# Saída
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# WHILE:
# ------------------------------------------------------

# sequencia de fibonnaci:
N = 10
last, next = 0, 1
while last < N:
    print(last)
    last, next = next, last + next

# ENUMERATE:
# ------------------------------------------------------
# languages = ['Python', 'Java', 'JavaScript']

# enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
# print(list(enumerate_prime))

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# Você também pode desestruturar (unpack) os itens da lista ou tupla:
languages = ['Python', 'Java', 'JavaScript']

for index, language in enumerate(['Python', 'Java']):
    print(f'{index} - {language}')
# Saída:
# 0 - Python
# 1 - Java

# Exercício 12
# O Fatorial de um número inteiro é representado pela multiplicação de todos
# os números predecessores maiores que 0. Por exemplo, o fatorial de 5 é 120
# pois 5! = 1 * 2 * 3 * 4 * 5. Escreva um código que calcule o fatorial de um número inteiro.
NUMBER = 5
RESULT = 1
# Usamos NUMBER + 1 pro range ir até o NUMBER
for factor in range(1, NUMBER+1):
    RESULT *= factor
RESULT

# Exercício 13
# Um sistema de avaliações registra valores de 0 a 10 para cada avaliação.
# Após algumas mudanças estes valores precisam ser ajustados para avaliaçõesde 0 a 100.
# Dado uma sequência de avaliações ratings = [6, 8, 5, 9, 10].
# Escreva um código capaz de gerar as avaliações após a mudança. Neste caso o resultado deveria ser [60, 80, 50, 90, 100].
ratings = [6, 8, 5, 9, 10]
new_ratings = [10 * rating for rating in ratings]
print(new_ratings)

# Exercício 14
# Percorra a lista do exercício 13 e imprima “Múltiplo de 3” se o elemento for divisível por 3.
ratings = [6, 8, 5, 9, 10]

for rating in ratings:
    # o sinal % representa a operação "resto".
    if (rating % 3) == 0:  # se o resto é zero, é divisível
        print(f'{rating} é múltiplo de 3')
