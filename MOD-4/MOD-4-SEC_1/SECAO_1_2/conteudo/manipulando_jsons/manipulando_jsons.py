import json  # json é um modulo que vem embutido, porém precisamos importá-lo


# with open("pokemons.json") as file:
#     content = file.read()  # leitura do arquivo
#     # o conteúdo é transformadoem estrutura python equivalente, dicionário
#     # neste caso.
#     pokemons = json.loads(content)["results"]
#     # acessamos a chave results que é onde contém nossa lista de pokemons

# print(pokemons[0])  # imprime o primeiro pokemon da lista

# A leitura pode ser feita diretamente do arquivo, utilizando o método load
# ao invés de loads. O loads carrega o JSON a partir de um texto e o load
# carrega o JSON a partir de um arquivo.
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

print(pokemons[0])  # imprime o primeiro pokemon da lista

# A escrita de arquivos no formato JSON é similar à escrita de arquivos comuns,
# porém temos que transformar os dados primeiro.
import json

# Leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)

# Assim como a desserialização, que faz a transformação de texto em formato
# JSON para Python, a serialização (caminho inverso) possui um método
# equivalente para escrever em arquivos de forma direta.
# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)
