from collections.abc import Iterable, Iterator

# Antes de começar, faz-se necessário o banco de dados. Para diminuir a complexidade deste exemplo, segue uma pseudo implementação de uma classe que faz a simulação do banco de dados:


class DbSimulator:
    def __init__(self):
        # Imagine que estes dados estão populados no banco de dados
        self.person_table = [
            {"name": "Morgana", "age": "22"},
            {"name": "Sarah", "age": "24"},
            {"name": "Will", "age": "33"},
            {"name": "Rick", "age": "23"},
            {"name": "John", "age": "22"},
            {"name": "Peter", "age": "35"},
            {"name": "Groove", "age": "48"},
            {"name": "Sam", "age": "19"},
        ]

    # Não se preocupe com este método apenas simula um retorno get do banco.
    def get(self, query, page):
        per_page = 2

        if query == "select * from person":
            first = (page * per_page) - per_page
            last = page * per_page
            return self.person_table[first:last]

# Para consultá-lo em partes menores, será criada uma classe chamada Iterable, que tem a coleção de objetos que pode ser iterada (no caso, o banco de dados para o relatório). Será implementado o método __iter__, padronizado pelo Python, responsável por fornecer um objeto iterador que veremos a seguir.
# Iterator e Iterable é a Interface padronizada pelo Python


class DatabaseIterable(Iterable):
    def __init__(self, db, query):
        self.db = db
        self.query = query

    """Aqui retornamos qual é o objeto que realiza a iteração"""
    def __iter__(self):
        return DatabaseIterator(self.db, self.query)

# O objeto iterador é uma instância da classe DatabaseIterator, em que será inserida a lógica para acessar o banco de dados e realizar as requisições por lotes (páginas). Implementa-se o método __next__, padronizado pelo Python, permitindo a iteração no DatabaseIterable.


class DatabaseIterator(Iterator):
    def __init__(self, db, query):
        """No construtor da classe iteradora, definimos o valor inicial do
        contador current_page, e também o(s) atributo(s) que será(ão)
        responsável(is) por armazenar/acessar a coleção de dados pela qual
        queremos iterar."""

        self.db = db
        self.query = query
        self.current_page = 1

    def get_page(self, page):
        return self.db.get(self.query, page)

    def __next__(self):
        """Este método busca no banco de dados a página que queremos e
        incrementa o contador current_page, para retornarmos a próxima página
        na próxima vez que o método for chamado."""

        data = self.get_page(page=self.current_page)

        """É uma boa prática a utilização da exceção StopIteration() para
        indicar que não foi possível avançar na iteração. Ou seja: tentamos
        acessar uma current_page que não existe."""

        if not data:
            raise StopIteration()

        self.current_page += 1
        return data

# Como respeitamos a interface do Python para escrever o padrão iterator, ele já libera o funcionamento do clássico for:
# Primeiro instanciamos o ITERÁVEL


record_paginator = DatabaseIterable(DbSimulator(), "select * from person")

# Em seguida podemos usar o for para iterar
# Nesse momento o ITERADOR é criado implicitamente
for page in record_paginator:
    # faz algo com a página, que é uma lista de resultados
    for record in page:
        print(record["name"])

