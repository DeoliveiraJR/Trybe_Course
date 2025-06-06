## Introdução

### O que vamos aprender?

Já vimos como o Sequelize pode ser usado para modelar as relações entre tabelas, permitindo trabalhar dados relacionados no banco de dados do conforto do Javascript.

Hoje vamos focar na modelagem de relações N:N ou muitos-para-muitos, com tabelas intermediárias. Além disso vamos ver como transações nos permitem preservar a integridade dos dados no banco, revertendo operações que não puderam ser realizadas até o final.

### Você será capaz de:

Utilizar o conceito de transações para realizar operações atômicas no banco de dados com sequelize;

Utilizar o sequelize para criar relacionamento N:N entre tabelas;

### Por que isso é importante?

Nós estudamos anteriormente como podemos utilizar o Sequelize para expressar relacionamentos do tipo 1:1 e 1:N em nossas aplicações. Mas existe outro tipo de relacionamento entre tabelas que é muito importante e que ocorre com bastante frequência quando estamos desenvolvendo aplicações Web que utilizam banco de dados, o relacionamento N:N. 😍

Existem situações em que queremos alcançar um determinado objetivo em nossa aplicação que envolvem executar um conjunto de operações em nosso banco de dados de forma atômica. A esta situação damos o nome de transação e é muito comum utilizá-la no desenvolvimento de software que envolve banco de dados. 💚

Vamos que vamos! 🚀
