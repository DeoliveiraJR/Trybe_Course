# """
# high level support for doing this and that.
# """

# Teste 1:


# def is_odd(number):
#     "Retorna True se um número é ímpar, senão False."
#     return number % 2 != 0


# Teste 2:
# def divide(a_number, other_number):
#     "Retorna a divisão de a_number por other_number"
#     return a_number / other_number

# Quando escrevemos testes, pensamos em cenários distintos que podem ocorrer no nosso sistema: “dado um arquivo com as seguintes linhas”, “visto que temos um banco de dados com um dado registro” ou “a partir de um cliente web”. Damos o nome de test fixture (ou apenas fixture) às precondições ou estados necessários para a execução de um teste.


def get_most_ordered_dish_per_costumer(orders, customer):
    max_amount = 0
    most_ordered = ""
    customer_dishes = {}

    for order in orders:
        if order["customer"] == customer:
            customer_dishes[order["order"]] = (
                customer_dishes.get(order["order"], 0) + 1
            )
            if customer_dishes[order["order"]] >= max_amount:
                max_amount = customer_dishes[order["order"]]
                most_ordered = order["order"]
    return most_ordered


def get_order_frequency_per_costumer(orders, customer, order):
    counter = 0
    for current_order in orders:
        if (
            current_order["customer"] == customer
            and current_order["order"] == order
        ):
            counter += 1
    return counter
