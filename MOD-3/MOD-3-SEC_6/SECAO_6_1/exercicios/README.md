## Exercícios - agora, a prática

#### Instruções para a realização dos exercícios

Neste exercício vamos criar uma API simples, onde será possível criar um livro ou listar todos os livros da base de dados. Vamos utilizar MySQL como banco de dados e Sequelize como nosso ORM.

Detalhes do projeto
Crie uma nova pasta e inicie um projeto com Express:

npm init -y

npm install -E express@4.17.1
Crie o arquivo index.js;

Instale o pacote sequelize e o mysql2:

npm install -E sequelize@6.3.4 mysql2@2.1.0
Instale o pacote sequelize-cli como uma dependência de desenvolvimento:

npm install --save-dev --save-exact sequelize-cli@6.2.0
Use o Sequelize-CLI para iniciar a configuração do ORM:

npx sequelize-cli init
Esse comando vai gerar as pastas models, seeder, config e migration dentro do seu projeto.

Garanta que tem um servidor MySQL rodando e coloque todas as configurações de acesso dentro do arquivo config/config.js;

Altere o arquivo models/index.js para carregar o arquivo config/config.js corretamente;

Crie o arquivo index.js com a estrutura básica de uma API com Express.

Copiar
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.listen(PORT, () => console.log(`Ouvindo na porta ${PORT}!`));

### 🚀 Exercício 1: Crie uma migration para criar uma tabela books com as seguintes colunas:

id: deve ser do tipo integer, não pode ser nula e ser a chave primária da tabela com auto incremento;
title: deve ser do tipo string e não pode ser nulo;
author: deve ser do tipo string e não pode ser nulo;
pageQuantity: deve ser do tipo integer e pode ser nulo;
createdAt: deve ser do tipo date e não pode ser nulo;
updatedAt: deve ser do tipo date e não pode ser nulo;
Obs: o método down da migration deve ser capaz de remover a tabela.

Obs 2: Execute o comando npx sequelize db:migrate e verifique se a tabela foi criada antes de continuar para os próximos exercícios.

### 🚀 Exercício 2: Crie o model Book utilizando a API do Sequelize. O model deve conter os seguintes campos:

title: deve ser do tipo DataTypes.STRING
author: deve ser do tipo DataTypes.STRING
pageQuantity: deve ser do tipo DataTypes.INTEGER
createdAt: deve ser do tipo DataTypes.DATE
updatedAt: deve ser do tipo DataTypes.DATE
Nos próximos exercícios você vai desenvolver uma API utilizando as camadas de service e controller.

## 🚀 Listando os livros

### Exercício 3: Crie um service BooksService com o método getAll para retornar uma lista de livros por meio do model Book.

### Exercício 4: Crie um controller BooksController com o método getAll sendo um middleware para retornar a lista de livros por meio do método getAll de BookService.

### Exercício 5: Vincule a rota GET /books para acessar seu controller.

## 🚀 Buscando um livro pelo id

### Exercício 6: No service BooksService crie um método getById que recebe um id como parâmetro e use o model Book para buscar esse livro. Retorne o objeto encontrado pelo model.

### Exercício 7: No controller BooksController crie o método getById sendo um middleware que recebe o id como parâmetro de rota e buscar o livro por meio do service. Se o livro não existir a resposta da requisição deve ter o status 404 e o json { "message": "Book not found" }.

### Exercício 8: Vincule a rota GET /books/:id para acessar seu controller.

## 🚀 Cadastrando um livro

### Exercício 9: No service BooksService crie um método create que recebe um objeto com os atributos title, author, pageQuantity e salve um novo livro utilizando o model Book.

### Exercício 10: No controller BooksController crie o método create sendo um middleware que recebe os atributos title, author, pageQuantity do body da requisição e salve os dados por meio do service.

### Exercício 11: Vincule a rota POST /books para acessar seu controller.

## 🚀 Editando um livro

### Exercício 12: No service BooksService crie um método update que recebe dois parâmetros: o id do livro a ser alterado e um objeto com os atributos title, author, pageQuantity e atualize o livro utilizando o model Book.

### Exercício 13: No controller BooksController crie o método update sendo um middleware que recebe o id como parâmetro de rota e os atributos title, author, pageQuantity do body da requisição e salve os dados por meio do service. A requisição deve retornar o status 200 e a mensagem ‘Book updated!’. Se o livro não for encontrado retornar a mensagem ‘Book not found!’.

### Exercício 14: Vincule a rota PUT /books/:id para acessar seu controller.

## 🚀 Removendo um livro

### Exercício 15: No service BooksService crie um método remove que recebe o id do livro a ser removido e remova o mesmo utilizando o model Book.

### Exercício 16: No controller BooksController crie o método remove sendo um middleware que recebe o id como parâmetro de rota e remova o livro por meio do service.

### Exercício 17: Vincule a rota DELETE /books/:id para acessar seu controller.

Faça um teste no Thunder Client para ver se o endpoint está funcional.

Em caso de erro, os endpoints devem retornar status code 500 com a mensagem: ‘Algo deu errado’.
