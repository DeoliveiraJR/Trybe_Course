# POLIMORFISMO ================================================================= :
# O polimorfismo é caracterizado quando duas ou mais classes distintas têm métodos de mesmo nome, de forma que uma função possa utilizar um objeto de qualquer uma das classes polimórficas, sem necessidade de tratar de forma diferenciada conforme a classe do objeto.

# Existem vários tipos de polimorfismo, mas dois são mais comuns: sobrecarga de métodos (method overloading) e sobrescrita de métodos (method overriding). Vamos ver cada um deles.

# POLIMORFISMO:Sobrecarga de metodos (OVERLOADING) ============================= :
# A sobrecarga de métodos é algo que nativamente não existe em Python, mas é comum em outras linguagens, portanto é interessante entender. Ela acontece quando mais de um método pode ser definido com o mesmo nome, mas aceitando parâmetros em quantidades ou tipos diferentes. Por exemplo, na linguagem C++ podemos ter duas funções com o mesmo nome, func, onde uma recebe um número inteiro e outra recebe um caractere.
# Código em C++
#include "stdio.h"

# int func(int a) { return a + 1; }
# int func(char b) { return 4; }

# int main() { printf("%d %d", func(1), func('a')); }
# // saída: 2 4


# POLIMORFISMO:Sobrescrita de metodos (OVERRIDING) ============================ :
# é mais comum em qualquer linguagem que possua orientação a objetos. A sobrescrita ocorre quando um método definido em uma superclasse é novamente definido (reescrito/sobrescrito) na subclasse.

# Vamos continuar de onde paramos na lição anterior, onde criamos a classe Liquidificador que herda da classe Eletrodoméstico. Se quisermos, podemos reescrever alguns métodos de forma a deixá-los mais convenientes para o nosso uso. Para realizar a sobrescrita, basta declarar novamente o método na subclasse. Vamos a um exemplo:

# CLASS ELETRODOMESTICO :
# ----------------------------------------------------------------
class Eletrodomestico:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


# CLASS LIQUIDIFICADOR :
# ----------------------------------------------------------------
# class Liquidificador(Eletrodomestico):
#     def esta_ligado(self):
#         return False

# SUPER ========================================================= :
# Talvez você já conheça o super, mas vamos ver como ele pode ser útil no contexto de sobrescrita de métodos. Imagine que você quer somente melhorar o método da superclasse, por exemplo mudando o valor que ele retorna. Não faz sentido, em diversas ocasiões, que você reescreva tudo e modifique só algumas coisas. As vezes você quer reaproveitar o que já foi feito e somente dar uma incrementada. É aí que entra o super.

# Por meio dessa referência, você pode acessar métodos da superclasse por meio da subclasse. Para isso utilizamos a notação super().método().
# class Liquidificador(Eletrodomestico):
#     def esta_ligado(self):
#         return "Sim" if super().esta_ligado() else "Não"

# Vamos ver um exemplo de como informar que o Ventilador e o Liquidificador herdam da classe Eletrodomestico:
class Liquidificador(Eletrodomestico):
    pass


class Ventilador(Eletrodomestico):
    def __init__(self, cor, potencia, tensao, preco, quantidade_de_portas=1):
        # Chamada ao construtor da superclasse
        super().__init__(cor, potencia, tensao, preco)
        
        # Faz outras coisas específicas dessa subclasse
        self.quantidade_de_portas = quantidade_de_portas


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    # Permite a aquisição de qualquer eletrodoméstico
    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomesticos.append(eletrodomestico)

# Classes Abstratas =========================================================== :
# Uma classe abstrata é aquela que não pode possuir instâncias a partir dela, existindo apenas para ser herdada.

# Para criar uma classe abstrata em Python, basta criar uma classe que herda de abc.ABC:
# from abc import ABC


# class Database(ABC):
#     pass

# Para declarar um método como abstrato, utilizamos o decorador @abc.abstractmethod, e preenchemos o corpo do método com um pass, com Ellipsis (...) ou com um raise NotImplementedError:
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def execute(self, query):
        ...


class MongoDatabase(Database):
    def execute(self, query):
        print(f"executando query '{query}' no mongo")


class MySQLDatabase(Database):
    def execute(self, query):
        print(f"executando query '{query}' no mysql")


# Interface =================================================================== :
# Interfaces são o equivalente a classes abstratas que somente possuem métodos abstratos, ou seja, nenhum método já é implementado. Em algumas linguagens de programação existe uma palavra reservada e uma sintaxe específica para a criação e uso de interfaces. Em Python são apenas classes abstratas comuns que são herdadas por classes normais.
def minha_func(database):   # repare que o d é minúsculo
    if isinstance(database, Database):
        database.execute("query qualquer")
    else:
        print(f"{database} não é um Database válido")


db1 = MongoDatabase()
db2 = MySQLDatabase()

minha_func(db1)
minha_func(db2)
minha_func("db_inválido")

# executando query 'query qualquer' no mongo
# executando query 'query qualquer' no mysql
# db_inválido não é um Database válido

# A função isinstance retorna se um objeto é instância de uma classe ou de qualquer uma de suas subclasses.
# Pode não parecer tão impressionante, mas Python possui type hints, e as tipagens poderiam ser avaliadas em tempo de checagem estática, e não de execução, como foi com o uso de isinstance:
# repare que coloco o tipo do parâmetro, ou seja, `database` é do tipo
# `Database`
# def minha_func(database: Database):
#     database.execute("query qualquer")
