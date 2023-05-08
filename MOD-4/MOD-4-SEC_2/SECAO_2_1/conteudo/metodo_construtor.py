# Método Construtor/Inicializador :

# Após modelada nossa Classe do objeto, podemos partir para o construtor. O construtor é um método especial que roda automaticamente quando a gente cria (instancia) o objeto. Na maioria das linguagens, o construtor cria e devolve a instância do objeto e já inicializa os seus atributos.

# Em python, esta operação é dividida em dois métodos:

# __new__ (Construtor)
# __init__ (Inicializador)
class Exemplo:
    def __init__(self):
        print("Inicializando Exemplo")
        self.__privado = "Eu sou privado"

    def __new__(cls, *args, **kwargs):
        print("Criando uma nova instância de Exemplo")
        instance = super().__new__(cls)
        return instance

    def __metodo_privado(self):
        print("Este é um método privado")

    def metodo_publico(self):
        print("Este é um método público")
        self.__metodo_privado()


exemplo = Exemplo()
# exemplo.__metodo_privado()  # Erro: AttributeError: 'Exemplo' object has no attribute '__metodo_privado'
# print(f'"exemplo de metodo publico === {exemplo.metodo_publico()}')  # Erro: AttributeError: 'Exemplo' object has no attribute '__metodo_privado'
# print(f'"exemplo de metodo privado === {exemplo.__metodo_privado()}')  # Erro: AttributeError: 'Exemplo' object has no attribute '__metodo_privado'

# ⚠️ Importante: Apesar do método __init__ ser “apenas” o inicializador, é comum ver referências a ele como o construtor. Isso acontece pois são raras as vezes que precisamos alterar o __new__ para customizar nossas classes. Como a comunidade já adotou que “o __init__ é o construtor de objetos no Python“, também vamos seguir essa convenção por aqui 😉

# Com isso vamos para o segundo passo: basta recriar o método __init__ dentro de nossa classe, conforme exemplo a seguir:


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


# Agora podemos criar nossos primeiros liquidificadores:
meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador(
    cor="Vermelho", potencia=250, tensao=220, preco=100
)

print(f'meu_liquidificador COR = === {meu_liquidificador.cor}')
print(f'seu_liquidificador  COR = === {seu_liquidificador.cor}')

# Perceba que é possível ter atributos que não precisam ser passados por meio de parâmetros na chamada do construtor. Por exemplo, para o booleano __ligado e o inteiro __velocidade, o construtor vai iniciá-los sempre com os valores fixos (hard coded) False e 0, respectivamente.
