# Exercícios - agora, a prática
Vamos juntar tudo o que aprendemos até aqui e exercitar mais ainda nosso aprendizado! Para isso, primeiro vamos criar servers com Python utilizando alguns dos protocolos vistos e, então, vamos explorá-los.

👀 De olho na dica: se tiver dúvidas ao utilizar alguma das ferramentas que mencionamos nos exercícios, exercite suas habilidades de busca no Google ou experimente o comando man!

## Exercício 1

O primeiro server que vamos utilizar é o nosso velho amigo HTTP, na camada de aplicação. Você pode tanto criar um, quanto utilizar um dos projetos ou exercícios dos módulos anteriores. A ideia é utilizarmos os conhecimentos do conteúdo e a ferramenta cURL para realizarmos uma chamada HTTP para ele. O projeto deve ter rotas GET e POST para que seja possível enviar requisições para os endpoints e receber respostas, assim como já nos acostumamos a receber via browser ou utilizando programas como o Postman.

Caso tenha dificuldades maiores, você pode utilizar o Postman para converter uma requisição em cURL, é só fazer a requisição nele como você já sabe e depois clicar no botão code (que fica embaixo do save) e escolher cURL.

1. Faça uma chamada GET, utilizando o cURL.

2. Faça uma chamada POST, utilizando o cURL, passando um JSON no body da requisição.

3. Faça uma chamada qualquer, utilizando o cURL, passando um header na requisição.

## Exercício 2

Ainda utilizando o cURL, vamos explorar mais alguns conceitos do HTTP. Relembre que falamos que o HTTP organiza e dá significado aos dados encapsulados nessa camada. Por exemplo: ao vermos um 200 tanto nós quanto um client HTTP sabemos que aquela request foi realizada com sucesso. Vamos explorar isso com o cURL.

1. Faça uma chamada GET, utilizando o cURL, para “google.com”.

Perceba que foi retornado um 301. Isso quer dizer que existem diversos redirecionamentos que nos encaminham para o lugar certo. No caso, o caminho certo para a página do google é www.google.com. Ao acessarmos pelo navegador, não percebemos isso porque ele faz o redirecionamento para a página certa ao encontrar o 301, porém se você inspecionar a network vai identificar esse redirecionamento.

2. Faça uma nova chamada a “google.com”, porém agora utilizando o parâmetro -L ou --location, que serve para “seguir redirecionamentos”.

## Exercício 3

Agora utilizando o wget, pegue o conteúdo da página do site da Trybe, depois abra o arquivo HTML baixado em seu navegador. Faça o mesmo processo com outras páginas web.

## Exercício 4

Agora vamos para a camada de transporte. Crie um servidor TCP usando o módulo socketserver que já vem embutido com o Python. Nosso servidor TCP deverá:

1. Responder com um “Olá, client”, logo quando estabelecer uma conexão.

2. Imprimir no console todo dado recebido.

3. Responder com os dados recebidos (como um eco).

4. Utilizar a porta 8085.

Perceba que o servidor sozinho não faz nada. Ele precisa que alguém se conecte a ele. Então para testá-lo você pode utilizar o comando telnet localhost 8085, onde telnet é a aplicação que vamos utilizar, localhost é o local onde o servidor está (no caso, o seu próprio PC) e 8085 é a porta em que o servidor está escutando conexões.

👀 De olho nas dicas:

- A documentação do módulo traz exemplos de como instanciar seu servidor TCP;
- Na mesma documentação temos exemplos de classes para responder as requisições;
- Os dados na requisição vem em bytes, não strings! bytes podem ser decodificados em string com a codificação correta;
- Do mesmo jeito, para responder você pode precisar codificar strings em bytes;
- telnet sempre envia ASCII, já o netcat envia no encoding do sistema (em Linux, geralmente utf-8, mas confirme com o comando locale).

## Exercício 5

Utilizando o comando telnet ou o Netcat (nc):

1. Conecte no server do exercício anterior e envie informações. O server deverá imprimir as mensagens enviadas no console.

2. Pare o servidor e verifique o que aconteceu com a conexão que estava aberta com o comando telnet ou nc.

## Exercício 6

Reinicie o servidor TCP e agora faça uma requisição utilizando o cURL (HTTP).

Perceba o que é exibido no console do server, já que não estamos utilizando o HTTP nele. Perceba também que o comando cURL não recebe uma resposta HTTP com sentido (um status code 200, por exemplo), de modo que ele não sabe que aquela requisição chegou ao fim.

## Exercício 7

Agora vamos explorar o outro protocolo de transporte que aprendemos. Crie um servidor UDP usando o mesmo módulo socketserver. Nosso servidor UDP deverá:

1. Imprimir no console toda mensagem recebida (não esqueça de converter também para string).

2. Responder com os dados recebidos (como um eco).

3. Utilizar a porta 8084.

👀 De olho nas dicas:

- Todas as dicas do exercício 4 se aplicam;
- telnet não funciona com udp – use netcat.

## Exercício 8

Envie pacotes para o servidor UDP utilizando o Netcat (nc). Em seguida pare o servidor e perceba que, como não há conexão, nada é sentido pelo client.

## Exercício 9

Faça uma chamada ao server utilizando o cURL. Lembre que, além do HTTP, o comando utiliza o protocolo TCP e não o UDP. Repare o que acontece.

## Exercício 10
Agora, vamos utilizar um tipo de proxy que pode ser bastante útil no nosso cotidiano como pessoas desenvolvedoras: o NGROK. Com ele conseguimos criar um túnel para o nosso localhost.

1. Crie um servidor HTTP em sua máquina executando na porta 80 (pode ser um front-end ou um back-end criado em aulas anteriores).

2. Baixe o ngrok e extraia o arquivo baixado em uma pasta de sua preferência, conforme instruções do site oficial.

3. Conforme instruções do site, crie um túnel para a porta 80 de sua máquina.

4. Acesse o link disponibilizado em seu navegador. Utilize-o para acessar de outros dispositivos, como seu smartphone ou outro computador 😎.

5. Crie um servidor HTTP em sua máquina executando na porta 80 (pode ser um front-end ou um back-end criado em aulas anteriores).