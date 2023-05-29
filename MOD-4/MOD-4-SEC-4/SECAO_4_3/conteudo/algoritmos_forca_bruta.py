# SELECTION SORT =========================================================== :
# Vamos ver um exemplo de implementação:

# VERSAO 1 ================================================ :
def selection_sort(numbers):
    n = len(numbers)  # Quantidade de elementos da lista

    for index in range(n - 1):  # Precisamos ordenar N-1 elementos
        # Definimos a variável para buscar o menor elemento
        min_element_index = index

        # Início da busca pelo menor elemento
        for search_index in range(index + 1, n):
            if numbers[search_index] < numbers[min_element_index]:
                # Atualiza o índice atual do menor elemento
                min_element_index = search_index

        # Troca os elementos de posição
        current_element = numbers[index]
        numbers[index] = numbers[min_element_index]
        numbers[min_element_index] = current_element

    return numbers

# VERSAO 2 ================================================ :
# Outra maneira de implementar o Selection Sort (com mais recursos Pythônicos):


numbers = [7, 5, 9, 2, 6, 8]
print(f"Lista inicial: {numbers}")
ordered_numbers = selection_sort(numbers)
print(f"Lista final: {ordered_numbers}")


def search(numbers, start, end):
    min_element = numbers[start]
    min_element_index = start

    for i in range(start + 1, end):  # Busca pelo menor elemento
        if numbers[i] < min_element:
            min_element = numbers[i]
            min_element_index = i

    return min_element_index  # Retorna a posição do menor elemento


# def selection_sort(numbers):
#     n = len(numbers)

#     for index in range(n - 1): # Início da iteração para ordenar os N-1 elementos
#         min_element_index = search(numbers, index, n)
#         numbers[index], numbers[min_element_index] = numbers[min_element_index], numbers[index] # Trocando os elementos utilizando desempacotamento.

    return numbers

# INSECTION SORT =========================================================== :
# Vamos ver um exemplo de implementação:


def insertion_sort(numbers):
    n = len(numbers) # Quantidade de elementos na lista

    for index in range(1, n):  # Começaremos a ordenar pelo segundo elemento
        # Pegamos o segundo elemento e o definimos como chave
        key = numbers[index]

        # Tomamos a posição anterior para iniciar a comparação
        new_position = index - 1
        # Enquanto a chave for menor, remaneja o elemento para frente
        while new_position >= 0 and numbers[new_position] > key:
            # Remaneja o elemento
            numbers[new_position + 1] = numbers[new_position]
            new_position = new_position - 1

        numbers[new_position + 1] = key  # Insere a chave na posição correta

    return numbers


numbers = [7, 5, 9, 2, 6, 8]
print(insertion_sort(numbers))
