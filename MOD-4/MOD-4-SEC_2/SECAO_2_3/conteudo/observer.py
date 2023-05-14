# Aplicando o Padrão Observer

# Vamos implementar a representação de um sistema de notificação de uma rede social, de modo que, quando uma pessoa realizar uma nova postagem em seu perfil, todos as pessoas que a seguem serão notificadas. Entretanto, as pessoas seguidoras podem decidir se querem ser notificadas por mensagem, push notification ou e-mail.
# 1️. Precisaremos criar a classe Perfil, que ao adicionar um novo post (adicionar_post()), exibirá o mesmo (mostrar_post) e notificará todas as pessoas seguidoras ( notificar_todos) pelos sistemas (__sistemas de notificação) que possui. O método adicionar_sistema_de_notificacao() permitirá que o cadastro de novos sistemas seja feito de forma dinâmica:


class Perfil:
    def __init__(self):
        self.__sistemas_de_notificacao = []
        self.__new_post = None

    def adicionar_sistema_de_notificacao(self, sistema):
        self.__sistemas_de_notificacao.append(sistema)

    def notificar_todos(self):
        for sistema in self.__sistemas_de_notificacao:
            sistema.notificar()

    def adicionar_post(self, post):
        self.__new_post = post
        self.mostrar_post()
        self.notificar_todos()

    def mostrar_post(self):
        print(f"\nPost: {self.__new_post}\n")
    

# 2. Para implementar o padrão Observer, precisaremos criar as classes observadoras que acompanharão o objeto Perfil, observando se ele ganha um novo Post. Quando verdadeiro, cada observador vai disparar as notificações.

# Criaremos então, uma classe Observador para cada sistema de envio (E-mail, PushNotification, Mensagem). Como a estrutura dessas classes será parecida, nada mais justo que padronizá-las para uma Interface Abstrata, garantindo que exista o método notificar():


from abc import ABC, abstractmethod

# Interface Observer


class Notificador(ABC):
    @abstractmethod
    def notificar(self):
        pass


# Observador Mensagem


class NotificadorMensagem(Notificador):
    def __init__(self, perfil, seguidores):
        self.perfil = perfil
        self.seguidores = seguidores
        self.perfil.adicionar_sistema_de_notificacao(self)

    def notificar(self):
        print(f"Notificando via Mensagens: {self.seguidores}")


# Observador Push Notification


class NotificadorPushNotification(Notificador):
    def __init__(self, perfil, seguidores):
        self.perfil = perfil
        self.seguidores = seguidores
        self.perfil.adicionar_sistema_de_notificacao(self)

    def notificar(self):
        print(f"Disparando Push Notification para: {self.seguidores}")


# Observador Email


class NotificadorEmail(Notificador):
    def __init__(self, perfil, seguidores):
        self.perfil = perfil
        self.seguidores = seguidores
        self.perfil.adicionar_sistema_de_notificacao(self)

    def notificar(self):
        print(f"Disparando Email's para: {self.seguidores}")


# 3. Pronto, agora podemos usar nosso código com o padrão Observer! O código que vamos utilizar é conhecido na literatura como código Cliente:

# Agora, podemos ver como cada pessoa seguidora deseja ser notificada:

# Carlos quer ser notificado por mensagem
# Marcia e Claudia querem ser notificadas por mensagem e email
# Rodolfo quer ser notificado somente por mensagem

# Cliente
if __name__ == "__main__":
    seguidores_mensagem = ["Carlos", "Claudia", "Marcia", "Rodolfo"]
    seguidores_push_notification = ["Carlos"]
    seguidores_email = ["Claudia", "Marcia"]

    meu_perfil = Perfil()
    NotificadorMensagem(meu_perfil, seguidores_mensagem)
    NotificadorPushNotification(meu_perfil, seguidores_push_notification)
    NotificadorEmail(meu_perfil, seguidores_email)

    meu_perfil.adicionar_post("Olá universo da programação!")