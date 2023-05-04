# Na literatura encontramos as técnicas de dublê com os nomes fakes, mocks,stubs e spies. De uma forma bem resumida, podemos defini-las da seguinte maneira:

# Fakes: Objetos que possuem implementações funcionais, porém normalmente simplificadas;

# Mocks: São pré programados para verificar as chamadas das funções que receberem;

# Stubs: Fornecem respostas predefinidas;

# Spies: São como stubs, mas também armazenam informações de como foram chamados.
# import json


# def retrieve_pokemons_by_type(type, reader):
#     # lê o conteudo de reader e o transforma de json
#     # para dicionário
#     pokemons = json.load(reader)["results"]
#     # filtra somente os pokemons do tipo escolhido
#     pokemons_by_type = [
#         pokemon for pokemon in pokemons if type in pokemon["type"]
#     ]
#     return pokemons_by_type

# Um segundo cenário é onde a função espera o nome de um arquivo e a abertura do mesmo acontece dentro da função.
import json


def retrieve_pokemons_by_type(type, filepath):
    with open(filepath) as file:
        pokemons = json.load(file)["results"]
        pokemons_by_type = [
            pokemon for pokemon in pokemons if type in pokemon["type"]
        ]
        return pokemons_by_type
