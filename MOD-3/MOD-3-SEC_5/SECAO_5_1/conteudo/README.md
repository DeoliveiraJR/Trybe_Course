## Introdução - Arquitetura de Software

### O que vamos aprender?

Começaremos a estudar sobre arquitetura de software que é um tópico muito importante quando falamos em desenvolvimento de software. Quando escrevemos um software seguindo algum modelo arquitetural, temos um ganho de qualidade e de facilidade de manutenção, pois o código é organizado agrupando as partes que possuem responsabilidades similares em um mesmo lugar.

Iremos aprender o modelo arquitetural baseado em camadas que organizará nosso código em três camadas: a Model, a Service e a Controller. Cada uma dessas será estudada com mais detalhes ao longo da seção e, para simplificar a nossa comunicação, iremos chamar este modelo como arquitetura MSC.

## Introdução

### O que vamos aprender?

Hoje vamos estudar como organizar o nosso código aplicando o conceito de arquitetura de software. Vamos aplicar ao nosso código uma arquitetura baseada em camadas onde trabalharemos com três camadas: a camada Model; a camada Service; a camada Controller, onde cada uma das camadas possui uma responsabilidade única e bem definida a qual acomodará o código relacionado a esta responsabilidade.

Também vamos aprender sobre testes de unidade utilizando o mocha, chai sinon e iremos aplicá-los para testar os nossos códigos da camada Model, a camada que iremos discutir com mais detalhes durante o dia.

## Você será capaz de:

- Definir o conceito de Arquitetura de Software;
- Aplicar a arquitetura baseada em camadas em um código de exemplo;
- Criar testes de unidade para componentes de software da camada Model;
- Identificar os componentes de software pertencentes a camada Model.

### Por que isso é importante?

À medida que um software cresce, sua complexidade aumenta e, eventualmente, adicionar ou mesmo dar manutenção a funcionalidades pode tornar-se uma atividade desafiadora. Por isso, é necessário que nosso código siga algum tipo de organização que facilite a modificação ou adição de novas linhas de código, além de facilitar a leitura do código, principalmente para pessoas recém-chegadas ao time de desenvolvimento, a responsabilidade de cada trecho.

Esta organização recebe o nome de arquitetura de software e existem diversas maneiras de se projetar um software, em outras palavras, existem diversas arquiteturas que podem ser utilizadas no processo de desenvolvimento de software. Cada modelo arquitetural possui vantagens e desvantagens que devem ser consideradas no processo de escolha.

Possuir esse tipo de conhecimento lhe colocará em uma posição de destaque em processos seletivos, aumentando significativamente suas chances de conseguir sua posição como pessoa desenvolvedora.

Ao longo do dia trabalharemos com um modelo de arquitetura baseado em camadas chamado MSC, sigla para Model, Service e Controller, que são justamente os nomes das camadas que iremos dividir nossa aplicação. Hoje nosso foco é entender melhor a camada Model e como escrever testes de unidade para seus componentes de software.
