# Aplicando o Padrão Factory

# Vamos aplicar o padrão Factory Method para ajudar uma hamburgueria a impulsionar suas vendas! 🍔 A nossa intenção será estimular a aquisição de Combos por clientes. Para agilizar a produção dos combos e evitar erros, vamos desenvolver uma Fábrica de Combos, que facilitará a montagem dos mesmos.
# Basicamente, uma fábrica é uma classe de Interface Criadora, que é herdada por fábricas Criadoras Concretas, que veremos nos passos 3 e 4 a seguir:

# 1. Vamos começar criando uma classe abstrata, que será a interface base para as classes dos itens do cardápio:
from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __repr__(self):
        # __repr__ é o método que o Python chama quando realizamos um print() do objeto 
        pass

#  2. Criaremos agora as classes dos itens do cardápio, que possuem a interface Item, criada anteriormente, e implementa os métodos que a interface sugere (__repr__ em nosso caso):


class ItemHamburger(Item):
    def __repr__(self):
        return "Hamburguer"


class ItemRefrigerante(Item):
    def __repr__(self):
        return "Refrigerante"


class ItemSorvete(Item):
    def __repr__(self):
        return "Sorvete"


class ItemFritas(Item):
    def __repr__(self):
        return "Fritas"

# 3. Para finalmente implementarmos a nossa Fábrica, vamos criar uma Interface Criadora, que define a assinatura do método criar_combo, além de implementar os métodos exibe_itens e adicionar_itens que serão oferecidos para quem herdá-la:


class Combo(ABC):
    def __init__(self):
        self.items = []
        self.criar_combo()

    @abstractmethod
    def criar_combo(self):
        pass

    def exibe_itens(self):
        return self.items

    def adicionar_itens(self, item):
        self.items.append(item)


# 4. Por fim, implementaremos as classes Criadoras concretas, que possuem a responsabilidade final de fabricar o objeto desejado e tudo que é necessário para ele:

# Em nosso exemplo, temos três Combos: ComboTudo, ComboFeliz e ComboGelado. Cada um é fabricado conforme é desejado pelo restaurante.


class ComboTudo(Combo):
    def criar_combo(self):
        self.adicionar_itens(ItemHamburger())
        self.adicionar_itens(ItemSorvete())
        self.adicionar_itens(ItemFritas())
        self.adicionar_itens(ItemRefrigerante())


class ComboFeliz(Combo):
    def criar_combo(self):
        self.adicionar_itens(ItemHamburger())
        self.adicionar_itens(ItemFritas())
        self.adicionar_itens(ItemRefrigerante())


class ComboGelado(Combo):
    def criar_combo(self):
        self.adicionar_itens(ItemHamburger())
        self.adicionar_itens(ItemSorvete())


# 5. Agora podemos apenas usar nossa fábrica e teremos um código simples e objetivo:

if __name__ == "__main__":
    combo_escolhido = input(
        "Olá, qual seu pedido? [ComboTudo, ComboFeliz, ComboGelado]: "
    )
    
    #Para transformar uma string em código executável basta usar o método eval()
    # Equivalente a chamar ComboTudo(), ComboFeliz(), ComboGelado()
    combo = eval(combo_escolhido)()

    print(f"\nCriando o combo {type(combo).__name__}.")
    print(f"Combo fabricado com os seguintes itens: {combo.exibe_itens()}")
