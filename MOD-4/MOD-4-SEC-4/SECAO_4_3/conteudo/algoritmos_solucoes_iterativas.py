# Merge Sort================================================================ :
# Vamos ver um exemplo de implementação?
def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    # se não reduzi o suficiente, continua
    if (end - start) > 1:
        # encontrando o meio
        mid = (start + end) // 2
        # dividindo as listas
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        # unindo as listas
        merge(numbers, start, mid, end)

# função auxiliar que realiza a mistura dos dois arrays


def merge(numbers, start, mid, end):
    left = numbers[start:mid] # indexando a lista da esquerda
    right = numbers[mid:end] # indexando a lista da direita

    left_index, right_index = 0, 0 # as duas listas começarão do início

    # percorrer sobre a lista inteira como se fosse uma
    for general_index in range(start, end):
        # se os elementos da esquerda acabaram, preenche o restante com a lista da direita 
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        # se os elementos da direita acabaram, preenche o restante com a lista da esquerda
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        # se o elemento do topo da esquerda for menor que o da direita, ele será o escolhido
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            # caso o da direita seja menor, ele será o escolhido
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


numbers = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort(numbers, 0, len(numbers))
print(numbers)

# Existem diversas implementações do merge sort. A implementação acima foi retirada do canal Programação Dinâmica, no YouTube, que foi escolhida por sua facilidade em comparação a outras implementações.

# Quick Sort================================================================ :
# Vamos ver um exemplo de implementação?


def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end) 
        # Os menores em relação ao pivô ficarão à esquerda
        quick_sort(numbers, start, p - 1)
        # Os maiores elementos em relação ao pivô ficarão à direita
        quick_sort(numbers, p + 1, end)

# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        # o índice será o elemento em análise no momento, ele passará por todos os elementos
        if numbers[index] <= pivot:
            delimiter = delimiter + 1
            numbers[index], numbers[delimiter] = numbers[delimiter], numbers[index]

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1


numbers = [6, 5, 3, 1, 8, 7, 2, 4]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
