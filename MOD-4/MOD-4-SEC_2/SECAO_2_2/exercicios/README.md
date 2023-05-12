# Exercícios, agora a prática

### Exercício 1:

Abaixo temos parte da implementação de um jogo do mundo de Star Wars. Porém, esse código está com um erro. Encontre-o e corrija-o sem alterar o código das classes de personagens (Soldier e Jedi).

```sh
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


class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def fight_enemy(self):
        print(f"You caused {self.character.attack()} of damage to the enemy")


StarWarsGame(Soldier(5)).fight_enemy()
```

### Exercício 2:

Dado o código de um baralho e suas cartas, você deve transformá-lo em um iterador sequencial que fornece as cartas em sua ordem tradicional, começando de <A de copas> até <K de paus>.

```sh
class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)

class Baralho:
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)
```
