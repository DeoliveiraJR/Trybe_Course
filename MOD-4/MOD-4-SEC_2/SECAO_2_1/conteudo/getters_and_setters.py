# Um método setter implementa a lógica de como alterar um valor. Um método getter implementa a lógica de como recuperar um valor.
# class Liquidificador:
#     def get_cor(self):
#         return self.__cor.upper()

#     def set_cor(self, nova_cor):
#         if nova_cor.lower() == "turquesa":
#             raise ValueError("Não existe liquidificador turquesa")

#         self.__cor = nova_cor

#     def __init__(self, cor, potencia, tensao, preco):
#         # Observe que usamos o setter para já validarmos o primeiro valor
#         self.set_cor(cor)

#         # Demais variáveis omitidas para este exemplo


# liquidificador = Liquidificador("Azul", "110", "127", "200")

# # print(f"A cor atual é {liquidificador.__cor}")
# # AttributeError: 'Liquidificador' object has no attribute '__cor'

# print(f"A cor atual é {liquidificador.get_cor()}")
# # A cor atual é AZUL
# liquidificador.set_cor("Preto")
# print(f"Após pintarmos, a nova cor é {liquidificador.get_cor()}")
# # Após pintarmos, a nova cor é PRETO

# # ESPECIFICIDADS DO PYTHON
# # Métodos com prefixos get_ e set_ costumam, em Python, ser substituídos por uma forma de acesso mais transparente, para que possam ser utilizados como se fossem atributos públicos. Para isso são utilizados os decoradores (decorators) @property e @propriedade.setter, como no exemplo abaixo:


class Liquidificador:
    # Getter
    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter  # Repare que é @cor.setter, e não @property.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        # Observe que usamos o setter para já validarmos o primeiro valor:
        # usamos self.cor, que chama o setter, e não self.__cor que manipula
        # o atributo diretamente
        self.cor = cor

        # Demais variáveis omitidas para este exemplo


liquidificador = Liquidificador("Rosa", "110", "127", "200")

print(liquidificador.cor)  # ROSA
liquidificador.cor = "Vermelho"
print(liquidificador.cor)  # VERMELHO
