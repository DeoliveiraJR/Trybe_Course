#  COMPLEXIDADE QUADRATICA ========================== :
# Observe o algoritmo abaixo:
# Os arrays têm sempre o mesmo tamanho
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result

# No algoritmo acima, são recebidos dois arrays de tamanhos iguais e é retornado um novo array, cujos elementos são resultado da soma de cada um dos elementos do array1 com todos os elementos do array2.

# Qual seria a taxa de crescimento do tempo de execução desse algoritmo?

# Para cada número do array1 ser somado com todos os números contidos no array2, é necessário que o segundo seja percorrido por inteiro.

# Isso significa que para array1 e array2 com duas posições, serão necessárias 4 iterações (ou operações), para o algoritmo concluir sua execução. Se cada uma das entradas tiver 3 elementos, serão necessárias 9 operações para a conclusão da execução e assim sucessivamente.

# Rode o exemplo abaixo para conferir:
def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = [1, 2, 3, 4, 5]

multiply_arrays(meu_array, meu_array)
