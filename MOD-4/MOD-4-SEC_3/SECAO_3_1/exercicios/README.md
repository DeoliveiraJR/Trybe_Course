# Exercícios - agora, a prática
Vamos colocar tudo o que vimos até agora em prática.

## Exercício 1:
Faça uma requisição ao site https://httpbin.org/encoding/utf8 e exiba seu conteúdo de forma legível.

## Exercício 2:
Faça uma requisição ao recurso usuários da API do Github (https://api.github.com/users), exibindo o username e url de todos os usuários retornados.

```sh
mojombo https://api.github.com/users/mojombo
defunkt https://api.github.com/users/defunkt
pjhyett https://api.github.com/users/pjhyett
wycats https://api.github.com/users/wycats
```

### Exercício 3:

Às vezes, você precisa fazer com que o seu raspador da Web pareça estar fazendo solicitações HTTP como o navegador, para que o servidor retorne os mesmos dados que você vê no seu navegador. Faça uma requisição a https://scrapethissite.com/pages/advanced/?gotcha=headers e verifique se foi bem sucedida.

⚠️ Para verificar se a requisição foi bem sucedida, faça assert "bot detected" not in response.text. Se nada acontecer, seu código está funcionando. ⚠️ Faça a inspeção de como a requisição é feita pelo navegador para conseguir replicar através do código.

### Exercício 4:

Escreva um programa que se conecte ao banco de dados library e liste os livros da coleção books para uma determinada categoria recebida por uma pessoa usuária. Somente o título dos livros deve ser exibido.

### Exercício 5:
Faça o cálculo de quantos livros publicados (STATUS = PUBLISH) temos em nosso banco de dados por categoria. Ordene-os de forma decrescente de acordo com a quantidade.

⚠️ Você pode utilizar agreggation framework para auxiliar neste exercício.

Saída:

```sh
Java 95
Internet 41
Microsoft .NET 33
Web Development 16
Software Engineering 15
Business 12
Programming 12
Client-Server 11
Microsoft 8
Theory 7
```