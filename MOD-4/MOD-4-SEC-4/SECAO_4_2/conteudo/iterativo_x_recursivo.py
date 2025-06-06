# Vamos começar olhando para a função recursiva de contagem regressiva. Conseguimos montar uma função iterativa para ela? Sim! Vamos ver como fazer isso:
def iterative_countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print("FIM!")


iterative_countdown(5)

# Vamos ver agora como fica o código iterativo de cálculo de fatorial:


def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


iterative_factorial(5)
