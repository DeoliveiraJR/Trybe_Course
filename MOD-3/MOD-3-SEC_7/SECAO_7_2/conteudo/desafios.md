# OPERADORES DE COMPARAÇÃO :

1. Selecione e faça a contagem dos restaurantes presentes nos bairros Queens, Staten Island e Bronx. (utilizando o atributo borough)

RES.:
db.restaurants.countDocuments({ borough: { $in: ["Queens", "Staten Island", "Bronx"] } });

2. Selecione e faça a contagem dos restaurantes que não possuem culinária do tipo American. (utilizando o atributo cuisine)

RES.:
db.restaurants.countDocuments({ cuisine: { $ne: "American" } });

3. Selecione e faça a contagem dos restaurantes que possuem avaliação maior ou igual a 8. (utilizando o atributo rating)

RES.:
db.restaurants.countDocuments({ rating: { $gte: 8 } });

4. Selecione e faça a contagem dos restaurantes que possuem avaliação menor que 4.

RES.:
db.restaurants.countDocuments({ rating: { $lt: 4 } });

5. Selecione e faça a contagem dos restaurantes que não possuem as avaliações 5, 6 e 7.

RES.:
db.restaurants.countDocuments({ rating: { $nin: [5, 6, 7] } });

# OPERADORES LÓGICOS :

1. Selecione e faça a contagem dos restaurantes que não possuem avaliação menor ou igual a 5, essa consulta também deve retornar restaurantes que não possuem o campo de avaliação.

RES.:
db.restaurants.countDocuments({ rating: { $not: { $lte: 5 } }});

2. Selecione e faça a contagem dos restaurantes em que a avaliação seja maior ou igual a 6, ou restaurantes localizados no bairro Brooklyn.

RES.:
db.restaurants.countDocuments({ $or: [{ rating: { $gte: 6 } }, { borough: "Brooklyn" }] });

3. Selecione e faça a contagem dos restaurantes localizados nos bairros Queens, Staten Island e Brooklyn e possuem avaliação maior que 4.

RES.:
db.restaurants.countDocuments({
$and: [
{ borough: { $in: ['Queens', 'Staten Island', 'Brooklyn'] } },
{ rating: { $gt: 4 } },
],
});

4. Selecione e faça a contagem dos restaurantes onde nem o campo avaliação seja igual a 1, nem o campo culinária seja do tipo American.

RES.:
db.restaurants.countDocuments({ $nor: [{ rating: { $eq: 1 } }, { cuisine: "American" }] });

5. Selecione e faça a contagem dos restaurantes que satisfaçam ambas as condições a seguir:

- A avaliação seja maior que 6 OU menor que 10.
- Estejam localizados no bairro Brooklyn OU não possuam culinária do tipo Delicatessen.

RES.:
db.restaurants.countDocuments({
$and: [
{ $or: [{ rating: { $gt: 6, $lt: 10 } }] },
{ $or: [{ borough: 'Brooklyn' }, { cuisine: { $ne: 'Delicatessen' } }] },
],
});

# Método sort()

Faça os desafios 1 e 2 abaixo sobre o sort() utilizando a coleção restaurants criada anteriormente.

1. Ordene alfabeticamente os restaurantes pelo nome (atributo name).

RES.:
db.restaurants.find().sort({ "name": 1 }).pretty();

2. Ordene os restaurantes de forma decrescente baseado nas avaliações.

RES.:
db.restaurants.find().sort({ "rating": -1 }).pretty();

# Removendo documentos

Faça os desafios 1 e 2 abaixo, sobre remoção de documentos utilizando a coleção restaurants criada anteriormente.

1. Remova o primeiro restaurante que possua culinária do tipo Ice Cream, Gelato, Yogurt, Ices.

RES.:
db.restaurants.deleteOne({ cuisine: "Ice Cream, Gelato, Yogurt, Ices" });

2. Remova todos os restaurantes que possuem culinária do tipo American.

RES.:
db.restaurants.deleteMany({ cuisine: "American" });
