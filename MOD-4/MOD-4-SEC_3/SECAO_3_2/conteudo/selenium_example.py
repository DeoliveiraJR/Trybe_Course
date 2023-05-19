# IMPORTACAO_1 ============================================================== :
# # importação do webdriver, que é o que possibilita a implementação para todos
# # os principais navegadores da web
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys  # Importa teclas comuns

# # criação de uma instância de navegador utilizando o Firefox
# # firefox = webdriver.Firefox()
# chrome = webdriver.Chrome('.venv/bin/chromedriver')

# # requisições para essa instância criada utilizando o método `get`
# # response = firefox.get("https://www.python.org/")
# # RESPONSE = chrome.get("https://www.python.org/")
# RESPONSE = chrome.get("https://www.google.com.br/")

# # pesquisa na instância aberta do navegador pela primeira ocorrência
# # do nome 'q'
# search_input = chrome.find_element("name", "q")

# # escreve selenium dentro do campo de pesquisa
# search_input.send_keys("selenium")

# # pressiona enter para realizar a busca
# search_input.send_keys(Keys.ENTER)

# sleep(10)
# chrome.quit()

# IMPORTACAO_2 ============================================================== :
# from selenium import webdriver

# # Importa o By
# from selenium.webdriver.common.by import By

# chrome = webdriver.Chrome()

# chrome.get("https://books.toscrape.com/")


# # Define a função que fará o scrape da URL recebida
# def scrape(url):
#     chrome.get(url)

#     # Itera entre os elementos com essa classe
#     for book in chrome.find_elements(By.CLASS_NAME, "product_pod"):
#         # Cria dict vazio para guardar os elementos capturados
#         new_item = {}

#         # Cria uma chave 'title' no dict que vai receber o resultado da busca
#         # O título está em uma tag anchor que está dentro de uma tag 'H3'
#         new_item["title"] = (
#             book.find_element(By.TAG_NAME, "h3")
#             .find_element(By.TAG_NAME, "a")
#             .get_attribute("innerHTML")
#         )

#         # O trecho do book está em um elemento da classe 'price_color'
#         new_item["price"] = book.find_element(
#             By.CLASS_NAME, "price_color"
#         ).get_attribute("innerHTML")

#         # O link está dentro de um atributo 'href'
#         new_item["link"] = (
#             book.find_element(By.CLASS_NAME, "image_container")
#             .find_element(By.TAG_NAME, "a")
#             .get_attribute("href")
#         )

#         print(new_item)


# scrape("https://books.toscrape.com/")

# IMPORTACAO_3 ============================================================== :
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

# Importa a classe 'Options' do browser
from selenium.webdriver.chrome.options import Options

# Instancia um objeto da classe 'Options'
options = Options()

# Adiciona um argumento passando o parâmetro '--headless'
options.add_argument('--headless')

# Define que a instância do navegador deve usar as options definidas
chrome = webdriver.Chrome(options=options)


def scrape(url):
    chrome.get(url)

    books = []

    for book in chrome.find_elements(By.CLASS_NAME, "product_pod"):
        new_item = {}

        new_item["title"] = (
            book.find_element(By.TAG_NAME, "h3")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("innerHTML")
        )

        new_item["price"] = book.find_element(
            By.CLASS_NAME, "price_color"
        ).get_attribute("innerHTML")

        new_item["link"] = (
            book.find_element(By.CLASS_NAME, "image_container")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("href")
        )

        books.append(new_item)
    return books


chrome.get("https://books.toscrape.com/")

all_books = []
url2request = "https://books.toscrape.com/"

next_page_link = (
    chrome.find_element(By.CLASS_NAME, "next")
    .get_attribute("innerHTML")
)

while next_page_link:

    all_books.extend(scrape(url2request))
    try:
        url2request = (
            chrome.find_element(By.CLASS_NAME, 'next')
            .find_element(By.TAG_NAME, 'a').get_attribute('href')
        )
    except NoSuchElementException:
        print("exception handled")
        break

print(all_books[0])
