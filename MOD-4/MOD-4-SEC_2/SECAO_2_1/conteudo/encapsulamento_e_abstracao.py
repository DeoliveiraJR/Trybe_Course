# ENCAPSULAMENTO ================================================================= :
# O encapsulamento é um dos pilares da orientação a objetos. Por meio dele, é possível simplificar bastante a implementação da abstração. Assim, segmentamos nossos atributos e métodos em 3 categorias:

# Públicos: podem ser acessados livremente por qualquer parte da aplicação
# Protegidos: podem ser acessados apenas pela classe que os definem e, quando há herança envolvida, também pelas classes “abaixo” na hierarquia (veremos o tópico herança a seguir)
# Privados: podem ser acessados apenas pela classe que os definem

# Em Python não temos palavras reservadas como public, private e protected para declarar um atributo ou método como público, privado ou protegido, respectivamente. Para isso, existe uma convenção de nomenclatura para definir a acessibilidade de cada recurso:

# Nomes iniciados com _ (underline): são considerados “protegidos“, como os atributos _potencia e _tensao.

# ⚠️ Isso é apenas uma convenção entre pessoas desenvolvedoras Python, pois ainda será possível fazer um acesso direto por fora da classe;
# Nomes iniciados com __ (dunder/duplo underline): são considerados “privados“, como os atributos __ligado e __velocidade.
# ⚠️ Não será possível fazer o acesso diretamente por fora da classe, mas existem formas de burlar isso (caso queira saber mais pesquise name mangling);
# Quaisquer outros nomes válidos: são públicos.

# Podemos criar os métodos ligar e desligar e daremos poderes para que eles consigam manipular os atributos.

# Observe o código a seguir:
class Liquidificador:
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

# ABSTRAÇÃO ================================================================= :
# A abstração de dados é outro pilar da orientação a objetos, e oculta os detalhes da implementação mostrando apenas a funcionalidade para quem acessa os métodos, a fim de reduzir a complexidade do código.

# Perceba que, ao chamarmos o método ligar, não existe a necessidade de conhecer o cálculo interno. Aqui estamos aplicando a abstração, pois apenas o código da classe Liquidificador precisa se preocupar com a regra de negócio. Quando utilizarmos a classe em outra parte da aplicação, precisaremos apenas saber quais são os parâmetros necessários de cada método.


liquidificador_vermelho = Liquidificador("Vermelho", 250, 220, 100)
liquidificador_vermelho.ligar(1)
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? True
liquidificador_vermelho.desligar()
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? False
