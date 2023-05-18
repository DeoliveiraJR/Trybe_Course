# Para ajudar na didática, vamos utilizar o site http://books.toscrape.com/. Ele é um site próprio para o treinamento de raspagem de dados.
from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/", timeout=2)
selector = Selector(text=response.text)
print(selector)

# O título está no atributo title em um elemento âncora (<a>)
# Dentro de um h3 em elementos que possuem classe product_pod
titles = selector.css(".product_pod h3 a::attr(title)").getall()
# Estamos utilizando a::attr(title) para capturar somente o valor contido no texto do seletor

# Os preços estão no texto de uma classe price_color
# Que se encontra dentro da classe .product_price
prices = selector.css(".product_price .price_color::text").getall()

# Combinando tudo podemos buscar os produtos
# em em seguida buscar os valores individualmente
for product in selector.css(".product_pod"):
    title = product.css("h3 a::attr(title)").get()
    price = product.css(".price_color::text").get()
    print(title, price)


# RECURSOS PAGINADOS :

# Existe uma classe next, que podemos recuperar a url através do seu elemento âncora
next_page_url = selector.css(".next a::attr(href)").get()
print(next_page_url)

# Agora que sabemos como recuperar a próxima página, podemos iniciar na primeira página e continuar buscando livros enquanto uma nova página for encontrada.
# Cada vez que encontrarmos uma página, extraímos seus dados e continuamos até acabarem as páginas.
# Então vamos alterar tudo que tínhamos escrito no arquivo para o código abaixo:

# Define a primeira página como próxima a ter seu conteúdo recuperado
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'
while next_page_url:
    # Busca o conteúdo da próxima página
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    # Imprime os produtos de uma determinada página
    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)
    # Descobre qual é a próxima página
    next_page_url = selector.css(".next a::attr(href)").get()
