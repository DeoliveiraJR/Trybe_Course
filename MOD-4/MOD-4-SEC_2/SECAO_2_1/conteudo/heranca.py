# Herança ================================================================= :
# Anota aí ✏️: Herança é especializar o comportamento de uma classe, ou seja, a classe herdeira é tudo que a classe ascendente é e talvez um pouco mais!

# Veja o exemplo a seguir:
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
    
# Em Python, para declarar que um objeto herda as características de outro, basta na declaração da classe “passarmos como parâmetro” a classe que será herdada. Várias classes podem ser passadas para realizar a herança múltipla, mas isso foge do escopo desta aula. 
# class Liquidificador(Eletrodomestico):
#     pass

# SUPER ================================================================ :
# Um método pode chamar um outro método já declarado na superclasse da seguinte maneira:


# class A:
#     def faz_algo(self, valor):
#         print(valor)


# class B(A):
#     def faz_outra_coisa(self):
#         print("Vou printar o valor pelo método criado em A")
#         # Chama o método da classe A, que neste caso é a superclasse, passando
#         # o `self` explicitamente
#         A.faz_algo(self, valor=1)


# b = B()
# b.faz_outra_coisa()
# Vou printar o valor pelo método criado em A
# 1

# Observação sobre a linha 61: dada uma classe X qualquer que possua um método y que recebe self, ou seja, uma classe normal com um método normal, e um objeto z que é uma instância dessa classe, as duas chamadas são equivalentes: z.y() e X.y(z). Normalmente utilizamos a primeira, que é um “açúcar sintático” para a segunda, para evitar a complexidade de chamar o nome da classe, bem como passar o objeto em questão como parâmetro.
#  O exemplo anterior pode ter a linha A.faz_algo(self, valor=1) alterada para super().faz_algo(valor=1)

# Herança multi-nível ================================================== :
# Uma classe pode herdar de outra que herda de outra, ou seja, A herda de B, B herda de C. Não há diferenças significativas no funcionamento, mas é interessante saber que é possível e relativamente normal. Por mais que você não escreva algo assim, é possível que veja bastante em códigos de outras pessoas.

# Exemplo:


class C:  # C 
    def x(self):  # método de exemplo
        print(1)


class B(C):  # B herda de C
    pass


class A(B):  # A herda de B
    pass


a = A()
a.x()
# 1

# Herança nultipla ===================================================== :
# Em Python existe também a chamada herança múltipla, não tão comum a outras linguagens, que é a capacidade que uma classe tem de herdar de mais de uma classe ao mesmo tempo. Ou seja, uma classe A pode herdar de B e C simultaneamente, sem que haja herança multi-nível.


# class A(B, C): 
#     pass
