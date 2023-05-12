# EXERCICIO-1 : Abaixo temos parte da implementação de um jogo do mundo de Star Wars. Porém, esse código está com um erro. Encontre-o e corrija-o sem alterar o código das classes de personagens (Soldier e Jedi).

class Soldier:
    def __init__(self, level):
        self.level = level

    def attack(self):
        return self.level * 1


class Jedi:
    def __init__(self, level):
        self.level = level

    def attack_with_saber(self):
        return self.level * 100


class JediAdapter:
    def __init__(self, jedi):
        self.jedi = jedi

    def attack(self):
        return self.jedi.attack_with_saber()


class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def fight_enemy(self):
        print(f"You caused {self.character.attack()} of damage in the enemy")


StarWarsGame(Soldier(5)).fight_enemy()
StarWarsGame(JediAdapter(Jedi(20))).fight_enemy()

# EXERCICIO-2 : Dado o código de um baralho e suas cartas, você deve transformá-lo em um iterador sequencial que fornece as cartas em sua ordem tradicional, começando de <A de copas> até <K de paus>.

from collections.abc import Iterator, Iterable


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return "<%s de %s>" % (self.valor, self.naipe)


class IteradorDoBaralho(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._pos = 0

    def __next__(self):
        try:
            carta = self._cartas[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos += 1
            return carta


class Baralho(Iterable):
    naipes = "copas ouros espadas paus".split()
    valores = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe) for naipe in self.naipes for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return IteradorDoBaralho(self._cartas)
    
    def __str__(self) -> str:
        return f"{[carta for carta in self]}"

# EXERCICIO-3 : Com o baralho tradicional pronto, implemente uma subclasse de Baralho chamada BaralhoInverso, que produz um iterador para fornecer as cartas na ordem inversa. Ou seja, sem embaralhar, a primeira carta deve ser o <K de paus> em vez do <A de copas>, como acontece na implementação atual.


class IteradorDoBaralhoInverso(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._pos = - 1

    def __next__(self):
        try:
            carta = self._cartas[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos -= 1
            return carta


class BaralhoInverso(Baralho):
    def __iter__(self):
        return IteradorDoBaralhoInverso(self._cartas)


# EXERCICIO-4 : Agora que você tem duas formas diferentes de dar cartas para o seu baralho, refatore o código para não precisar mais de dois baralhos e dois iteradores isolados, mas sim usar um único iterador com duas estratégias diferentes de iteração.


# from abc import ABC, abstractmethod
# from collections.abc import Iterator, Iterable



# class Carta:
#     def __init__(self, valor, naipe):
#         self.valor = valor
#         self.naipe = naipe

#     def __repr__(self):
#         return "<%s de %s>" % (self.valor, self.naipe)



# class IteradorDoBaralho(Iterator):
#     def __init__(self, cartas, estrategia):
#         self._cartas = cartas
#         self._estrategia = estrategia
#         self._pos = self._estrategia.posicao_inicial

#     def __next__(self):
#         try:
#             carta = self._cartas[self._pos]
#         except IndexError:
#             raise StopIteration()
#         else:
#             self._pos = self._estrategia.proxima_carta(self._pos)
#             return carta


# class EstrategiaIteracao(ABC):
#     posicao_inicial = 0

#     @abstractmethod
#     def proxima_carta(cls, index):
#         raise NotImplementedError


# class EstrategiaRegular(EstrategiaIteracao):
#     posicao_inicial = 0

#     @classmethod
#     def proxima_carta(cls, index):
#         return index + 1


# class EstrategiaReversa(EstrategiaIteracao):
#     posicao_inicial = -1

#     @classmethod
#     def proxima_carta(cls, index):
#         return index - 1


# class Baralho(Iterable):
#     naipes = "copas ouros espadas paus".split()
#     valores = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

#     def __init__(self, estrategia):
#         self._cartas = [
#             Carta(valor, naipe)
#             for naipe in self.naipes
#             for valor in self.valores
#         ]
#         self.estrategia = estrategia

#     def __len__(self):
#         return len(self._cartas)

#     def __iter__(self):
#         return IteradorDoBaralho(self._cartas, self.estrategia)
    
#     def __str__(self):
#         return f"{[carta for carta in self]}"


# baralho_regular = Baralho(EstrategiaRegular())
# baralho_inverso = Baralho(EstrategiaReversa())


# EXERCICIO-5 : Você tem a implementação de uma classe capaz de renderizar imagens através de uma interface que utiliza o método draw. Porém, no momento ela só suporta formato PNG e você também precisa ser capaz de renderizar imagens em SVG. Altere o código, sem modificar a classe SvgImage, para que isso seja possível.


from abc import ABC, abstractmethod


class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class PngImage(PngInterface):
    def __init__(self, png_path):
        self.png_path = png_path
        self.format = "raster"

    def draw(self):
        print(f"Drawing PNG {self.png_path} with {self.format}")


class SvgImage:
    def __init__(self, svg_path):
        self.svg_path = svg_path
        self.format = "vector"

    def get_image(self):
        return f"SVG {self.png_path} with {self.format}"


class SvgAdapter(PngInterface):
    def __init__(self, svg):
        self.svg = svg

    def draw(self):
        print(f"Drawing {self.svg.get_image()}")


# EXERCICIO-6 : Você está trabalhando em um sistema de orçamentos que faz cálculos de impostos e precisa ser refatorado para adicionar novos, que no caso são o PIS (0,65%) e o COFINS (3%). Mas durante a refatoração, você se depara com uma má prática de código. Encontre essa má prática e a solucione em conjunto com a refatoração.
from abc import ABC, abstractmethod


class EstrategiaDeImposto(ABC):
    @abstractmethod
    def calcular(cls, valor):
        raise NotImplementedError


class ISS(EstrategiaDeImposto):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.1


class ICMS(EstrategiaDeImposto):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.06


class PIS(EstrategiaDeImposto):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.0065


class COFINS(EstrategiaDeImposto):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.03


class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_imposto(self, imposto):
        return imposto.calcular(self.valor)


orcamento = Orcamento(1000)
print(f"ISS: {orcamento.calcular_imposto(ISS)}")
print(f"ICMS: {orcamento.calcular_imposto(ICMS)}")
print(f"PIS: {orcamento.calcular_imposto(PIS)}")
print(f"COFINS: {orcamento.calcular_imposto(COFINS)}")
