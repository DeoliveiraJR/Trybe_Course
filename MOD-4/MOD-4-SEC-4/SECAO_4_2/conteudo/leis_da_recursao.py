# Podemos perceber que a recursividade é um excelente método para usarmos no dia a dia, entretanto, nada é perfeito! Quando formos escrever um código, temos que ter o cuidado para que não haja um loop infinito.

# Exemplo:

# A função countdown abaixo tem como objetivo fazer uma contagem regressiva partindo de n até zero.
# def countdown(n):
#     print(n)
#     countdown(n - 1)  # chamada recursiva

# countdown(5)

# Observe que dentro da implementação desta solução, a função chama ela mesma.
# Então, como seria a correção desse código para que ele funcione de acordo com esperado?🤔 Observe a resposta abaixo:
def countdown(n):
    if n == 0: # caso base
        print("FIM!")
    else:
        print(n)
        countdown(n - 1) # caso recursivo


countdown(5)

# Como vimos acima, não podemos construir um código recursivo sem validar algumas condições. Sendo assim, vamos a três leis importantes:

# 1) Um algoritmo recursivo deve ter um caso base: quando falamos de recursão, devemos sempre lembrar do caso base, pois sem ele nosso algoritmo ficará executando infinitamente.

# O caso base é a condição de parada do algoritmo recursivo, ele é o menor subproblema do problema, tornando-o possível de resolver de forma direta/trivial;

# 2) Um algoritmo recursivo deve mudar o seu estado e se aproximar do caso base: após o início da execução de um algoritmo recursivo, a cada nova chamada a ele mesmo, o seu estado deve se aproximar progressivamente do caso base.

# Vamos imaginar a seguinte situação: queremos criar um código que irá printar números a partir de 0 e terminar em 10. O caso base do algoritmo é 10, pois é onde nossa função recursiva deve parar a execução. A primeira chamada a função terá o número 0 passado de parâmetro. A cada nova chamada à função, nosso estado deve incrementar o valor 1 ao valor do estado anterior, até chegar ao número 10. Logo, o valor do estado na primeira chamada será 0, na segunda chamada será 1, na terceira chamada será 2, e assim por diante até chegar ao valor do caso base;

# 3) Um algoritmo recursivo deve chamar a si mesmo, recursivamente: Essa lei é a própria definição de recursão.

