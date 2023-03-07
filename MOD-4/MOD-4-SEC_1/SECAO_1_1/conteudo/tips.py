import random
from collections import Counter

# ALL:
# =========================================

# valida se TODOS retornam true = EVERY
nomes_1 = ["Felps", "Carlos", "Will", "Bux"]
nomes_2 = ["Flavio", "Carlos", "Roni", ""]
numeros_1 = [1, 2, 3, 4]
numeros_2 = [0, 5, 6, 7]

all(nomes_1)
all(nomes_2)
all(numeros_1)
all(numeros_2)


# ANY:
# =========================================

# valida se ALGUM retorna true = SOME
any(nomes_1)
any(nomes_2)
any(numeros_1)
any(numeros_2)


# MAX, MIN, LEN:
# =========================================

# gera duas listas, uma com len definido, outro não.
random_list = random.sample(range(0, 100000), 1000)
random_list = random.sample(range(0, 100000), random.randint(50, 5000))


# COUNTER:
# =========================================

lista_de_numeros = []

# gera um conjunto de numeros aleatorio em um intervalo determinado
for x in range(10000):
    lista_de_numeros.append(random.randint(0, 10000))

# converte o resultado em um dict
counter = Counter(lista_de_numeros)
# print(counter)

# metodo que retorna a quantidade de elementos do conjunto em tuplas
mais_comuns = counter.most_common()
print(mais_comuns)

# destruturando o conjunto
elemento_mais_comum, numero_de_vezes = mais_comuns[0]
print(elemento_mais_comum)
print(numero_de_vezes)
