## Definindo os cenários de teste

Para exemplificar como funciona o teste de integração, iremos construir uma nova API chamada Cacau Trybe, uma API que fornece endpoints para gerenciar uma lista de chocolates de diferentes marcas da França 🍫.

Seguindo as premissas do TDD, a primeira questão que devemos nos preocupar são os cenários de teste. Esses cenários, além de validar o nosso código, irão representar os contratos definidos para essa API.

Bora conhecer esses contratos? 📄

A API Cacau Trybe será composta por três endpoints, representados pelos seguintes contratos:

👉 GET /chocolates

Objetivo: Retornar uma lista com todos os chocolates cadastrados.
Código HTTP: 200 - OK;
Body (exemplo):
Copiar
[
{ "id": 1, "name": "Mint Intense", "brandId": 1 },
{ "id": 2, "name": "White Coconut", "brandId": 1 },
{ "id": 3, "name": "Mon Chéri", "brandId": 2 },
{ "id": 4, "name": "Mounds", "brandId": 3 }
]

👉 GET /chocolates/:id

Objetivo: Buscar um chocolate específico pelo ID.
Código HTTP: 200 - OK;
Body (exemplo):
Copiar
[
{
"id": 4,
"name": "Mounds",
"brandId": 3
}
]

👉 GET /chocolates/brand/:brandId

Objetivo: Buscar uma lista de chocolates pelo ID (brandId) da marca.
Código HTTP: 200 - OK;
Body (exemplo):
Copiar
[
{
"id": 1,
"name": "Mint Intense",
"brandId": 1
},
{
"id": 2,
"name": "White Coconut",
"brandId": 1
}
]

Com os contratos definidos, é hora de escrever nossos testes.
