# REQUISICOES_WEB :

# Abaixo vamos ver alguns exemplos de como utilizar a biblioteca requests:
import requests


# Requisição do tipo GET
response = requests.get("https://www.betrybe.com/", timeout=1)
print(response.status_code)  # código de status
print(response.headers["Content-Type"])  # conteúdo no formato html

# Conteúdo recebido da requisição
print(response.text)

# Bytes recebidos como resposta
print(response.content)

# Requisição do tipo post
resp = requests.post("http://httpbin.org/post", data="some content", timeout=1)
print(resp.text)

# Requisição enviando cabeçalho (header)
resp = requests.get(
    "http://httpbin.org/get",
    headers={"Accept": "application/json"},
    timeout=1)
print(resp.text)

# Requisição a recurso binário
response = requests.get("http://httpbin.org/image/png", timeout=1)
print(response.content)

# Recurso JSON
response = requests.get("http://httpbin.org/get",timeout=1)
# Equivalente ao json.loads(response.content)
print(response.json())

# Podemos também pedir que a resposta lance uma exceção caso o status não seja OK
response = requests.get("http://httpbin.org/status/404", timeout=1)
response.raise_for_status()
