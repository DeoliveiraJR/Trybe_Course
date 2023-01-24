# Os parâmetros podem ser passados de forma:

# posicional: são aqueles definidos por meio da posição em que cada um é passado;
# nomeada: são definidos por meio de seus nomes.
def soma(x, y):
    return x + y


soma(2, 2)  # os parâmetros aqui são posicionais

soma(x=2, y=2)  # aqui estamos nomeando os parâmetros
