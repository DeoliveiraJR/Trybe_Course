# Exercícios - teste seu conhecimento

## 🚀 POO em Python

Nesse exercício você implementará uma função em Python para resolver um teste técnico similar ao que já foi aplicado pelo Facebook e outras big techs! Tente desenvolver uma solução otimizada e escolha bem qual estrutura de dados será utilizada em termos de complexidade de tempo e espaço! Essa escolha tende a ser um diferencial em um processo seletivo desse tipo.

### Exercício
Implemente um sistemas de logs por nível de severidade, seguindo o diagrama abaixo

#### Classe Log

##### Atributos:

**manipuladores** - Será inicializado com um conjunto de subclasses de ManipuladorDeLog;
Métodos:

**adicionar_manipulador** - adiciona um manipulador ao conjunto de manipuladores do gerenciamento de logs (Log);

**info** - dispara logs com nível de severidade "INFO";

**alerta** - dispara logs com nível de severidade "ALERTA";

**erro** - dispara logs com nível de severidade "ERRO";

**debug** - dispara logs com nível de severidade "DEBUG";

**__log** - dispara os logs formatados para todos os manipuladores (invocado para cada nível de severidade, para evitar duplicação de código);

**__formatar** - formata os logs de acordo com o padrão “[ERRO - 01/01/2020 13:00:00]: ZeroDivisionError: division by zero”;

#### Classe ManipuladorDeLog:

A classe ManipuladorDeLog é uma interface (e, por consequência, uma classe abstrata) e deve declarar um método de classe (classmethod) e abstrato (abstractmethod) log que recebe um parâmetro mensagem ou msg.

#### Classes LogEmArquivo e LogEmTela:

As classes LogEmArquivo e LogEmTela devem herdar de ManipuladorDeLog e sobrescrever o método de classe log, salvando a mensagem em um arquivo ou a exibindo na tela, respectivamente.

🐦 Dica: Você pode utilizar a função print em tela ou em arquivo (que pode ter um nome padrão).