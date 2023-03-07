# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre
# o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira,
# potenciação e módulo) envolvendo essas variáveis.
A = 10
B = 5
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A // B)
print(A ** B)
print(A % B)


# Exercício 2: Declare e inicialize uma variável: hours = 6. Quantos minutos têm em 6 horas?
# E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos
# resultados das contas. Depois, imprima cada uma delas.
HOURS = 6
MINUTES = HOURS * 60
SECONDS = MINUTES * 60
print(MINUTES)
print(SECONDS)

# Exercício 3: Teste e verifique o que acontece se você colocar um ponto e vírgula no final de uma instrução em Python.


# Exercício 4: Suponha que o preço de capa de um livro seja R$ 24, 20, mas as livrarias
# recebem um desconto de 40 % . O transporte custa 3, 00 para o primeiro exemplar e 75
# centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
#  Escreva uma expressão que receba o custo total e a imprima.
BOOKS = 60
BOOK_PRICE = (1 - 0.4) * 24.20
LOGISTIC = 3 + (BOOKS - 1) * 0.75
COST = BOOKS * BOOK_PRICE + LOGISTIC
print(COST)

# elementos são definidos separados por vírgula, envolvidos por colchetes
fruits = ["laranja", "maçã", "uva", "abacaxi"]

print(fruits[0])  # o acesso é feito por índices iniciados em 0

print(fruits[-1])  # o acesso também pode ser negativo

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("abacaxi")  # removendo uma fruta

# acrescenta uma lista de frutas a lista original
fruits.extend(["pera", "melão", "kiwi"])

# retorna o índice onde a fruta está localizada, neste caso, 1
fruits.index("maçã")

fruits.sort()  # ordena a lista de frutas

# Copie a lista abaixo para realizarmos os exercícios de fixação 5 e 6:
trybe_course = ["Introdução", "Front-end", "Back-end"]

# Exercício 5: Adicione o elemento “Ciência da Computação” à lista.
trybe_course.append("Ciência da Computação")

# Exercício 6: Acesse e altere o primeiro elemento da lista para “Fundamentos”.
trybe_course[0] = "Fundamentos"

# elementos separados por vírgula, envolvidos por chaves
permissions = {"member", "group"}

permissions.add("root")  # adiciona um novo elemento ao conjunto

# como o elemento já existe, nenhum novo item é adicionado ao conjunto
permissions.add("member")

permissions.union({"user"})  # retorna um conjunto resultado da união

# retorna um conjunto resultante da intersecção dos conjuntos
permissions.intersection({"user", "member"})

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# Exercício 7: Um conjunto ou set pode ser inicializado utilizando-se também o método set().
# Inicialize uma variável com essa função var = set() e adicione seu nome ao conjunto utilizando
#  um dos métodos vistos acima. Depois, imprima a variável e confira se o retorno é: {‘seu_nome’}.
var = set()
var.add("Lauro Cesar")
print(var)

# assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset
permissions = frozenset(["member", "group"])

# novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo
# não pode ser modificado
permissions.union({"user"})

# retorna um conjunto resultante da intersecção dos conjuntos
permissions.intersection({"user", "member"})

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# Utilizando o código abaixo, faça os exercícios 8 e 9:
info = {
    "personagem": "Margarida",
    "origem": "Pato Donald",
    "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

# vamos converter o range em uma lista para ajudar na visualização

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

# podemos utilizar valores negativos para as entradas também
list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Exercício 8: Insira no objeto uma nova propriedade com o nome de chave “recorrente”
# e o valor “Sim”. Em seguida, imprima o objeto no console.
info["recorrente"] = "Sim"

# Exercício 9: Remova a propriedade cuja chave é “origem” e imprima o objeto no console.
del info["origem"]

# vamos converter o range em uma lista para ajudar na visualização

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

# podemos utilizar valores negativos para as entradas também
list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Exercício 10: Após uma consulta do banco de dados, temos linhas que contém nome, sobrenome
# e idade como: "Thiago", "Nobre", 29.Que estrutura vista anteriormente seria recomendada dado
# que após esta consulta somente exibimos estes valores?

# Exercício 11: Realizar a contagem de quantas vezes cada elemento aparece em uma sequência é
#  uma técnica muito útil na solução de alguns problemas.
# Qual é a estrutura mais recomendada para o armazenamento desta contagem?
my_list = [20, 20, 1, 2]
count_elements = {
    20: 2,
    1: 1,
    2: 2
}
