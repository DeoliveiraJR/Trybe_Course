# COMPOSICAO ================================================================= ?
# Agora que temos nosso liquidificador funcionando, vamos associá-lo a uma pessoa cozinheira, dizendo assim que esta pessoa pode possuir um liquidificador.

# ⚠️ Aviso: Se atente ao fato de que uma pessoa não é da mesma classe que um liquidificador, ela possui um liquidificador. Neste caso, precisamos utilizar o conceito de Composição.

# Anota aí ✏️: Composição é atribuir o objeto de uma classe a um atributo da outra, gerando assim um relacionamento de pertencimento entre elas. Você pode ver mais aqui.

# Observe o exemplo abaixo que aplica esse conceito:
class Liquidificador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = int(preco)
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter  # Repare que é @cor.setter, e não @property.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    # Uma forma de melhorar esta apresentação, é implementar o método __str__ para a classe que deseja imprimir. Assim o Python substituirá o print padrão pelo retorno que você desejar. Veja esse exemplo:
    def __str__(self):
        return f"{self.nome} - possui {self.saldo_na_conta} reais em sua conta."


liquidificador = Liquidificador("Rosa", "110", "127", "200")
liquidificador.cor = "Vermelho"

pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador)

print(f'pessoa cozinheira = {pessoa_cozinheira}')
