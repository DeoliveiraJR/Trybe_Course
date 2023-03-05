## ============================================ EXEMPLO 1:
## FROM alpine:3.14
## CMD ["echo", "Eu sou uma pessoa estudante da Trybe!"]d

## ============================================ EXEMPLO 2:
## FROM httpd:2.4
## COPY index.html /usr/local/apache2/htdocs/
## EXPOSE 80
## CMD ["httpd-foreground"]

## ============================================ EXEMPLO 3:
## FROM nginx:1.21-alpine AS primeiro-estagio
## WORKDIR /site

## COPY config.toml config.toml
## COPY index.html /site/layouts/index.html
## COPY _index.md /site/content/_index.md

## RUN apk add hugo
## RUN hugo --minify --gc
## RUN mv /site/public/* /usr/share/nginx/html

## ENTRYPOINT ["nginx", "-g", "daemon off;"]

## ============================================ EXEMPLO 4:
# Primeiro Estágio
FROM alpine:3.14 AS primeiro-estagio
#No primeiro estágio, não precisamos do nginx, pois vamos apenas executar a ferramenta Hugo. Logo, a imagem base escolhida foi a alpine:3.14. Ao copiar os arquivos necessários e executar o comando, conseguimos nossas páginas HTML prontas e presentes no caminho /site/public/
WORKDIR /site

COPY config.toml config.toml
COPY index.html /site/layouts/index.html
COPY _index.md /site/content/_index.md

RUN apk add hugo
RUN hugo --minify --gc

# Segundo Estágio
FROM nginx:1.21-alpine AS segundo-estagio
COPY --from=primeiro-estagio /site/public/ /usr/share/nginx/html
# Esse é o segredo principal de construção de múltiplos estágios;
# O COPY possui a capacidade de copiar arquivos entre os estágios;
# A flag --from indica que devemos copiar o seguinte arquivo ou pasta de um estágio para o estágio atual;
# Neste caso acima, estamos copiando as páginas HTML resultantes do Hugo diretamente para uma imagem Docker limpa de nginx!
ENTRYPOINT ["nginx", "-g", "daemon off;"]