# EXERCICIO 1 ======================================================== :

# Faça uma chamada GET, utilizando o cURL.

# curl localhost:3000

# Ou use:

#  curl -X GET localhost:3000

# Faça uma chamada POST, utilizando o cURL, passando um JSON no body da requisição.
# curl -X POST \
#      -H 'Content-Type: application/json' \
#      -d '{ "foo": "bar" }' \
#      localhost:3000

# Faça uma chamada qualquer, utilizando o cURL, passando um header na requisição.
# curl --request POST \
#     --header 'Content-Type: application/json' \
#     --header 'Authorization: ApiKey EXAMPLE-TOKEN' \
#     --data '{ "foo": "bar" }' \
#     localhost:3000

# EXERCICIO 2 ======================================================== :
# 1. Faça uma chamada GET, utilizando o cURL, para “google.com”.
#  curl google.com

# 2. Faça uma nova chamada a “google.com”, porém agora utilizando o parâmetro -L ou --location, que serve para “seguir redirecionamentos”.
# curl -L google.com

# EXERCICIO 3 ======================================================== :
# Agora utilizando o wget, pegue o conteúdo da página do site da Trybe, depois abra o arquivo HTML baixado em seu navegador. Faça o mesmo processo com outras páginas web.
# wget betrybe.com
