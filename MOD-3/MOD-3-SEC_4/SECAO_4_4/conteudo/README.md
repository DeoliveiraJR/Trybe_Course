## Middlewares

O Express é um framework com um objetivo central: receber requisições e enviar respostas. Você já viu como ele usa funções que recebem requisição (req) e resposta (res) como parâmetros. Agora, você verá como essas funções podem ser decompostas em funções menores, que podem ser aproveitadas em diversas rotas.

Cada função terá uma responsabilidade única, se essa função capturar algum problema, uma resposta de erro será retornada para a pessoa usuária.

Exemplos:

Formato de e-mail não apropriado;
CPF com formato inválido;
Pessoa usuária não tem permissão de acesso.

Agora, se estiver tudo certo, será indicado no final dessa função, seguir para a próxima função da rota (fazendo uma validação diferente). Com isso, serão feitas quantas funções forem necessárias, até que uma delas devolva uma resposta a pessoa usuária. Esse é um estilo de composição de funções chamado middlewares.

A primeira coisa que você precisa saber sobre middlewares é: no Express toda função passada para uma rota é um middleware.

Calma aí, como assim? 🤔

Para o Express, um middleware é uma função que realiza o tratamento de uma requisição HTTP e que pode responder essa request ou chamar o próximo middleware.

🤫 Bom, para te contar um segredo: estamos usando middlewares desde o começo deste conteúdo, mas com outro nome! Até agora, nos referimos aos middlewares como callbacks ao falar sobre roteamento e definição de endpoints. Acontece que todos os callbacks que mostramos nessas rotas são middlewares.

Na prática, middlewares recebem três parâmetros: req, res e next, exatamente como as funções callback que usamos até agora para registrar rotas.

Middlewares não precisam retornar nada. O fato é que o Express ignora o retorno dos middlewares, visto que o importante é se aquele middleware chamou ou não um método que responda a request, e se ele chamou ou não a função next.

### Bora estudar como refatorar um middleware? 🚀

### Refatorando um middleware

Agora que você estudou o que são middlewares, o próximo passo será refatorar a API de times de futebol e aplicar na prática o aprendizado de middlewares.

Para isso, preste atenção especialmente nos métodos POST e PUT:

Vamos para o código?

## Para Fixar

🚀 Crie um middleware existingId para garantir que o id passado como parâmetro na rota GET /teams/:id existe no objeto teams. Refatore essa rota para usar o middleware.

🚀 Reaproveite esse middleware e refatore as rotas PUT /teams/:id e DELETE /teams/:id para usarem ele também.

🚀 Mova o middleware validateTeam para o arquivo src/middlewares/validateTeam.js, mas continue usando o middleware nas rotas POST /teams e PUT /teams/:id.

🚀 Mova o middleware existingId para o arquivo src/middlewares/existingId.js, mas continue usando o middleware nas rotas PUT /teams/:id e DELETE /teams/:id.
