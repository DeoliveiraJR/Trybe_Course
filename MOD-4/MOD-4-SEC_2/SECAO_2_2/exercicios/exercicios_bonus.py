# Exercício 1: Dada uma lista, descubra o menor elemento. Por exemplo,
# [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.
def minimum(numbers):
    smaller = numbers[0]
    for number in numbers:
        if number < smaller:
            smaller = number
    return smaller


# Exercício 2: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um triângulo retângulo com n asteriscos de base. Por exemplo,
# para n = 5 o triângulo terá 5 asteriscos na base:
def draw_triangle(n):
    for row in range(1, n + 1):
        print(row * "*")


# Exercício 3: Crie uma função que receba um número inteiro N e retorne o
# somatório de todos os números de 1 até N. Por exemplo, para N = 5,
# o valor esperado será 15.
def summation(limit):
    return sum(range(1, limit + 1))


# Exercício 4: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
def fuel_price(type, liters):
    if type == "A":
        price = 1.90
        discount = 0.03
        if liters > 20:
            discount = 0.05
    elif type == "G":
        price = 2.50
        discount = 0.04
        if liters > 20:
            discount = 0.06
    total = price * liters
    total -= total * discount
    return total
