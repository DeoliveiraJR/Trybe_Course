# O problema agora é outro: a ferramenta que compramos tem uma API pronta para integrar no nosso sistema, só que a interface é muito diferente da nossa. Ela exporta uma lista de cabeçalhos e uma lista de valores, não é como a nossa que já monta os dicionários direitinho…

# Ao analisar os códigos do sistema, já deparamos com um exemplo de classe que analisa o relatório e realiza um cálculo de média. Nota-se que o método average() espera que o retorno de load_data() contenha estruturas dict.
class ReportAnalyzer:
    def __init__(self, loader):
        self.loader = loader

    def average(self):
        # este é um dos métodos que espera uma lista de dicionários
        data = self.loader.load_data()
        # aqui ela soma o valor na chave final_price em cada item da lista
        total = sum(order['final_price'] for order in data)
        return total / len(data)

# Pelo que foi comentado na reunião, a nova ferramenta (gerenciator3000) não retorna uma estrutura com dicionários, o que é comprovado ao realizar os print de seu retorno:
# Código exemplo para simular a API Gerenciator3000


class ReportLoader:
    def __init__(self):
        self.headers = ["id", "date", "final_price"]
        self.rows = [
            [1337, "2020-11-20", 2350.5],
            [1338, "2020-11-21", 4800.5],
        ]


g3000_loader = ReportLoader()
print(g3000_loader.headers)   #  ['id', 'date', ..., 'final_price']
print(g3000_loader.rows[0])  #  [1337, '2020-11-20', ..., 2350.5]

# O time decidiu fazer uma classe responsável por “traduzir” esses dados do formato da ferramenta para o formato do sistema utilizado pela companhia. Essa classe poderá ser acoplada na ferramenta de relatórios. Tem-se então uma adaptação eficiente:


class G3000LoaderAdapter:
    # aqui o loader é uma instância do gerenciator3000.ReportLoader original
    def __init__(self, loader):
        self.loader = loader

    def load_data(self):

        # Em python, o zip() junta uma lista de chaves em uma lista de valores
        # e permite criar dicionário! Por exemplo:
        # dict(zip(['nome', 'idade'], ['Juliana', 27]))
        # {'nome': 'Juliana', 'idade': 27}

        data = []
        for row in self.loader.rows:
            data.append(dict(zip(self.loader.headers, row)))
        return data

# Feito! Foi utilizado outro padrão, o Adapter. Ele permite converter a interface de uma classe em outra interface, esperada pelo cliente (isto é, o código que usa a classe em questão). O Adapter permite que interfaces incompatíveis trabalhem em conjunto — o que, de outra forma, seria impossível.

# Veja só como fica o código que vai utilizá-lo:


loader = G3000LoaderAdapter(g3000_loader)
# o analyzer do nosso sistema recebe o adaptador como qualquer outro loader
analyzer = ReportAnalyzer(loader)
analyzer.average() # Agora funcionará

