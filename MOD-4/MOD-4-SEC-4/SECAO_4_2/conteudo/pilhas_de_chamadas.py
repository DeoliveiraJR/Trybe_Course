# Anota aí 🖊:

# Toda vez que chamamos uma função em um programa, o sistema operacional reserva memória para as variáveis e parâmetros da função;

# Sempre quando uma função é executada, ela é guardada na pilha;

# Quando a função termina de ser executada, ela sai da pilha.

# Vamos utilizar esse código com recursão e visualizar o funcionamento da pilha de chamadas:
def saudacao():
    print("Oi")


def despedida():
    print("Tchau")


def init():
    print("Inicio")
    saudacao()
    print("Fim")
    despedida()


init()

# Exercício de fixação:

# Exercício: Faça um algoritmo recursivo de soma. Esse algoritmo deve receber um número de parâmetro e deve somar todos os números antecessores a ele.


def sum_recursive(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + sum_recursive(n - 1)


sum_recursive(4)
